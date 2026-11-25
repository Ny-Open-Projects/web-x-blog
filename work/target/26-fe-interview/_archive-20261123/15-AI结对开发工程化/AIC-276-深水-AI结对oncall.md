---
title: [AIC-276] AI Agent 参与 oncall 轮值（一级响应）的可行边界是什么？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-276：AI Agent 参与 oncall 轮值（一级响应）的可行边界是什么？
**答**：
- 可承担：告警初筛分级、上下文聚合（变更/面板/历史）、按 runbook 执行只读诊断、草拟报告。
- 不可承担：变更类操作（重启/扩容/回滚）、对外沟通、根因最终判断——误操作与误判代价过高。
- 分级响应：明确类告警（磁盘满）给完整处置建议，模糊类告警只做信息聚合。
- 人机接力协议：Agent 的诊断结论必须带证据链，人接手时可直接验证而不是从头查。

```javascript
const oncallAgent = {
  can: ['triage', 'ctx-aggregate', 'read-only-diagnose', 'draft-report'],
  cannot: ['mutating-ops', 'comms', 'final-root-cause'],
  handoff: '结论必附证据链（面板截图/日志行），人可直接验证',
};
r
```
