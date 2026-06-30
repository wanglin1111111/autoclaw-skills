# 重复命令问题诊断 — 2026-06-30

## 问题现象
用户每天看到重复的 `/approve` 命令和类似的工作流输出，体验极差。

## 根因链

```
Agent 多步工作流 (6 步安装)
  → 每步独立 exec
    → Safety Guard 逐条拦截
      → 每步需 /approve
        → 用户不在时超时拒绝
          → 下次重新触发整条链
            → 又来一轮
```

## 已修复

| 修复项 | 改动 | 效果 |
|--------|------|------|
| 飞书监控频率 | 30min → 4h | 48次/天 → 6次/天 |
| 市场信息超时 | 300s → 600s | 不再 timeout 假死 |
| 研报抓取 | 禁用 | 停止撞 rate limit |
| 监控 delivery | announce → none | 消除无意义路由失败 |
| 3个残留 cron | 删除 | clawoss-heartbeat/manual-start/exec-fix-test |

## 待解决：审批风暴

**核心矛盾：** Safety Guard 设计为单步高危拦截，Agent 设计为多步编排，两者不兼容。

**建议：**
1. 给 auto-designer 的 AGENTS.md 加规则：「多步安装必须合并为一条脚本，单次批准」
2. 考虑：在现有 `exec.ask: "off"` 之上，是否需要调整 Safety Guard 的高风险判定阈值
3. 用户侧：用 `allow-always` 时给一整条合并脚本批准，而不是逐条批准
