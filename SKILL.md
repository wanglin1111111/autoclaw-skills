---
name: system-health-optimization
description: Agent 系统健康诊断与全局优化。当用户反映「重复命令」「审批风暴」「cron 噪音」「系统卡顿」等问题时使用。基于第一性原理排查 cron 配置、Safety Guard 摩擦、Agent 行为规则、delivery 路由等全链路瓶颈，输出诊断报告并执行修复。
---

# 系统健康诊断与优化

## 概述

多 Agent 系统中，性能问题往往不是单一 bug，而是多层子系统设计假设冲突的叠加效应。本 Skill 提供结构化排查流程——从 cron 审计到审批链路到 Agent 行为注入——系统性定位根因而非修修补补。

## 触发条件

- 用户反馈「重复发命令」「一直刷屏」
- 审批风暴（连续 /approve 刷屏）
- 系统响应变慢、cron 任务堆积
- 定期健康检查

## 排查流程

### 第一阶段：Cron 审计

```
1. cron list（含 includeDisabled:true）
2. 逐一检查：
   - 频率是否过高（<1h 的 every 任务重点审查）
   - 是否有连续错误（consecutiveErrors ≥ 2）
   - delivery 路由是否断裂
   - 是否有残留的 disabled 任务
3. 输出审计报告表格
```

### 第二阶段：审批链路分析

当用户粘贴 /approve 刷屏日志时：

```
1. 确认 Safety Guard 状态：gateway config.get safety → blockHighRiskToolCalls
2. 确认 exec 配置：exec.security + exec.ask
3. 判断是否为「多步工作流 × 逐条拦截」冲突
4. 检查是否有批量合并的空间
```

**常见问题模式**：Safety Guard 设计为单步高危拦截，Agent 在编排多步工作流时逐条 exec，形成 N 步 × N 次批准。

### 第三阶段：Agent 行为注入

当确认是 Agent 行为导致时，修改目标 Agent 的 AGENTS.md：

```markdown
### Command Bundling — Prevent Approval Storms

- 3 步以上连续 exec 必须合并为单条 PowerShell 脚本
- 一次批准跑完整条工作流
- 例外：步骤间存在运行时依赖时拆分
```

### 第四阶段：Session 排查

```
1. sessions_list 查活跃 session
2. subagents list 查子 agent 状态
3. 确认是否有僵尸 session 占用资源
```

## 修复清单

| 问题 | 修复 |
|------|------|
| Cron 频率过高 | 拉长间隔，everyMs 调大 |
| Cron 超时 | 增加 timeoutSeconds 或拆分任务 |
| Cron 限流 | 暂停（enabled:false），恢复后重新启用 |
| Delivery 路由断裂 | mode 改 none 或修正 target |
| 残留僵尸 cron | remove |
| 审批风暴 | Agent AGENTS.md 注入合并规则 |
| 僵尸 session | kill |

## 输出规范

每次诊断必须产出：
1. 根因链（从现象到根因的分层描述）
2. 修复前后对比表
3. 诊断报告文件（workspace/diagnosis-YYYY-MM-DD.md）
