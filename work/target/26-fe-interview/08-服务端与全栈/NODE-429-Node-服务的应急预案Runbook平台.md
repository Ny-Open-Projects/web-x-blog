---
title: [NODE-429] Node 服务的应急预案（Runbook）平台化如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-429：应急预案 Runbook 平台化
**答**:
- Runbook 的失败模式：写在 wiki 里没人更新、故障时找不到、写了不验证。平台化三要素：与告警绑定（每条告警注解强制 runbook 链接 NODE-404）、可执行化（步骤带一键操作：回滚按钮/开关链接/查询链接直达）、验证机制（演练触发 runbook 实际走一遍，过期自动标记）。
- 结构模板：症状识别（看什么图确认是这个故障）→ 影响面（用户看到什么）→ 止血步骤（按序，每步可执行）→ 根因排查（止血后再查）→ 恢复验证。
- 与值班体系闭环（ARC-477）：值班手册索引所有 runbook；每次故障复盘更新对应 runbook（ARC-407）；使用统计（哪些 runbook 从未演练 → 高危）。
- 内容治理：owner 制（每 runbook 有维护人）、简化（超 2 页的拆分——故障时没人读长文档）、截图与链接有效性校验（自动化巡检）。
- 高级形态：常见场景自动化（runbook 步骤编排成一键剧本：自动诊断 → 建议动作 → 人工确认执行）。
```yaml
# runbook: api-5xx-spike
symptom: "API 5xx 率 > 1%（看板 link）"
impact: "下单失败率上升"
steps:
  - "查看发布：最近 30min 是否有发布 → {rollback-link}"          # 一键回滚
  - "查依赖健康：DB/Redis → {dep-dashboard}"
  - "查连接池等待 → {pool-metrics}，>0 持续 → 杀慢查询 {kill-slow}"
verify: "5xx 回落 < 0.1% 持续 5min"
owner: trade-fe
lastDrill: 2026-11-10
```
