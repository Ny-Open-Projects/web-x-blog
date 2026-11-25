---
title: [1205] 笔试手写：实现按能力与负载的任务分配
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent]
type: 笔试题
---

## 1205：笔试手写：实现按能力与负载的任务分配

**需求**：实现 assign(agents, tasks)：agents 为 { id, caps: string[], load: number, maxLoad: number }[]，tasks 为 { id, cap }[]。按序分配：优先选「支持该 cap 且当前 load < maxLoad 中 load 最小」的 agent（并列按 id 字典序）；分配后 load+1；无可用 agent 的任务进 unassigned。返回 { assignments: [{ task, agent }], unassigned }。

```js
function assign(agents, tasks) {
  const st = agents.map(a => ({ ...a }));
  const assignments = [], unassigned = [];
  for (const t of tasks) {
    const cands = st.filter(a => a.caps.includes(t.cap) && a.load < a.maxLoad)
      .sort((a, b) => a.load - b.load || (a.id < b.id ? -1 : 1));
    if (!cands.length) { unassigned.push(t.id); continue; }
    const pick = cands[0];
    pick.load++;
    assignments.push({ task: t.id, agent: pick.id });
  }
  return { assignments, unassigned };
}
const agents = [
  { id: 'a1', caps: ['code', 'test'], load: 2, maxLoad: 3 },
  { id: 'a2', caps: ['code'], load: 0, maxLoad: 2 },
  { id: 'a3', caps: ['test'], load: 1, maxLoad: 1 },
];
console.log(assign(agents, [
  { id: 't1', cap: 'code' },   // a2 (load 0)
  { id: 't2', cap: 'code' },   // a2 (load 1, a1 load2)
  { id: 't3', cap: 'code' },   // a1 (a2 满)
  { id: 't4', cap: 'test' },   // a3? load1<1 否 -> a1 (load2<3) 
  { id: 't5', cap: 'code' },   // unassigned
]));
```

**评分点**：
- 负载最小优先 + caps 过滤 + maxLoad 容量约束三条件齐
- 并列 id 字典序稳定
- unassigned 收集（拒绝静默丢弃任务）
- 能讨论：贪心的局限（全局最优需回溯/拍卖算法）、负载估计的进阶（按预估 token 而非任务数）

