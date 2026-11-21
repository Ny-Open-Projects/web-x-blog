---
title: [AIC-263] AI 评审发现的「疑似高危」需要人确认，如何设计升级（escalation）流程不造成积压？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-263：AI 评审发现的「疑似高危」需要人确认，如何设计升级（escalation）流程不造成积压？
**答**：
- 升级三要素：具体位置 + 怀疑理由 + 需要谁确认（按模块映射 owner）。
- 限时处理：高危确认 4 小时 SLA，超时自动升级到 tech lead；未确认不能合入。
- 降级出口：owner 可标记「误报」或「接受风险」，两者都入库训练检测模型。
- 积压监控：待确认队列长度进日报，> 10 条触发流程复盘（说明误报过多或人手不足）。

```javascript
const escalation = {
  payload: (f: Finding) => ({ where: f.loc, why: f.reason, owner: moduleOwner(f.file) }),
  sla: { high: '4h', timeout: 'escalate to tech-lead' },
  exits: ['confirm-fix', 'false-positive', 'accepted-risk'],
  backlog: 'queue > 10 → 流程复盘',
};
r
```
