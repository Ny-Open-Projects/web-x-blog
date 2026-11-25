---
title: [SOFT-836] 手写 grayTaskAssign：灰色任务按契约→效率→发现者起草的决策树路由、补契约提醒？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-836：手写 grayTaskAssign：灰色任务按契约→效率→发现者起草的决策树路由、补契约提醒

**需求与边界**：
- 实现 grayTaskAssign(task, contracts, capabilities)。
- 边界要求：① 决策树：契约有归属→按契约；无→按效率（能力匹配分+上下文持有+依赖位置三者算分最高者）；都无法判→发现者起草+确认归属；② 任务反复出现计数（同 key ≥3 次→触发补契约提醒 SOFT-811）；③ 归属确认必须书面留痕（返回 confirmRequired 标志）。

**答**：
```javascript
function grayTaskAssign(task, contracts, capabilities) {
  const inContract = contracts.find(c => task.key.match(c.pattern));
  if (inContract)
    return { owner: inContract.owner, basis: '契约' };
  const scored = capabilities.map(p => ({
    id: p.id,
    score: (p.skills.includes(task.skill) ? 2 : 0)
      + (p.contextHolds(task) ? 2 : 0)
      + (p.upstreamOf(task) ? 1 : 0),             // 能力+上下文+依赖位
  })).sort((a, b) => b.score - a.score);
  if (scored[0] && scored[0].score > 0)
    return { owner: scored[0].id, basis: '效率',
      confirmRequired: true };                   // 书面确认留痕
  return { owner: task.discoveredBy, basis: '发现者起草',
    confirmRequired: true,
    note: '归属需正式确认，防长期默认偏移' };
}
function recurrenceWatch(tasks, { threshold = 3 } = {}) {
  const counts = {};
  for (const t of tasks)
    counts[t.key] = (counts[t.key] ?? 0) + 1;
  return Object.entries(counts).filter(([k, n]) => n >= threshold)
    .map(([k]) => ({ key: k,
      action: `反复出现${threshold}次——触发补契约（SOFT-811）` }));
}
```

**评分点**:
- 决策树三段（契约→效率→发现者起草——SOFT-826 落地）。
- 效率评分三维（能力/上下文/依赖位）。
- 反复出现触发补契约（灰色根源=契约缺口的闭环）。

