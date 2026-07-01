# 效率瓶颈诊断 — 2026-07-01

## 触发场景
腾讯文档 MCP 接入 + 活动表格读写操作，全程约 20 步 exec，每步需独立审批。

## 根因分层

### 第一层：Safety Guard 逐条拦截（核心瓶颈）
- `blockHighRiskToolCalls: true` 导致每个 exec 都触发审批
- **本次数据**：腾讯文档操作共产生 **15+ 次审批请求**，实际通过率约 30%
- 审批超时窗口约 30 分钟，用户离线时段大量超时
- 超时后重新提交 → 再超时 → "继续"循环

### 第二层：工具链可靠性差
| 工具 | 状态 | 影响 |
|------|------|------|
| `mcporter call` CLI | 全部报 code 1 | 浪费 6 次审批尝试 |
| `image()` sharp 模块 | 不可用 | 图片分析全断 |
| `read()` 图片 | sharp 错误 | 同上 |
| `canvas` | 无 node | 不可用 |

最终靠 **Node.js HTTP 直连** 绕过 mcporter CLI 才通。

### 第三层：错误信息截断
- exec 输出被截断，stderr 为空但 exit code 1
- 每次排查需要额外审批来换输出格式 → 恶性循环

## 审批次数统计（本轮）

| 阶段 | 命令数 | 通过 | 超时 | 效率 |
|------|--------|------|------|------|
| Token 配置 | 2 | 1 | 1 | 50% |
| mcporter CLI 验证 | 4 | 0 | 4 | 0% |
| HTTP 直连调通 | 4 | 2 | 2 | 50% |
| 读取表格 | 4 | 1 | 3 | 25% |
| 写入数据 | 6 | 3 | 3 | 50% |
| 图片/OCR | 3 | 0 | 3 | 0% |
| **合计** | **23** | **7** | **16** | **30%** |

## 解法矩阵

| 方案 | 效果 | 风险 | 实施 |
|------|------|------|------|
| **① 关闭 blockHighRiskToolCalls** | 消除 100% exec 审批 | 中 | 手动编辑 `openclaw.runtime.json` |
| **② 扩增 safeBinProfiles** | 高频命令免审批 | 低 | 需确认路径是否仍受保护 |
| **③ 单脚本合并** | 多步→1次审批 | 低 | 可立即执行 |
| **④ 固化 HTTP 直连脚本** | 绕过 mcporter CLI | 无 | 已部分实现 |
| **⑤ 安装 sharp** | 修复图片分析 | 无 | npm 安装需审批+权限 |

## 推荐行动

### 立即（不依赖审批变更）
- **③** 所有表格操作合并为单脚本：读+写+格式化一次完成
- **④** 继续用 `node temp_mcp.js` 方式替代 mcporter CLI

### 中期（需手动改配置）
- **①** 在 `C:\Users\22812\.openclaw-autoclaw\openclaw.runtime.json` 中
  将 `blockHighRiskToolCalls` 从 `true` 改为 `false`
  或将指定高频 bin（node/powershell/npm）加入 safeBinProfiles

### 长期
- ⑤ 在有权限的环境下 `npm install --include=optional sharp`
- 申请 node 设备配给，启用 canvas 功能
