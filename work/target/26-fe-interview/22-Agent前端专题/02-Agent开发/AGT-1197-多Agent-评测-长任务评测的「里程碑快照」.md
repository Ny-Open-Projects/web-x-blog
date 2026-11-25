---
title: [1197] 长任务评测里，怎么记录里程碑快照支持中断续评
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 评测]
type: 面试题
---

## 1197：长任务评测里，怎么记录里程碑快照支持中断续评

**答**：
- 快照设计：每里程碑达成时落快照（产物状态 + 已通过标准 + 消耗），评测中断（预算/超时）后从最近快照续评——不必从头重跑（长任务重跑成本高）。
- 快照的三个断言点：产物完整性（文件都在）、里程碑判定可重放（判定函数纯函数化）、资源账（到该里程碑为止的成本——效率评测的分段数据）。
- 快照复用：同任务的多次评测（改了 reviewer prompt 重评）可复用前半段快照（前半段不受改动影响）——增量评测的基础。
- 追问钩子：快照复用的前提是什么？——「改动影响面分析」：改了 reviewer 只影响后段里程碑，前段快照有效；影响面判断错了快照就是错误前提，所以影响面判定本身要保守（不确定就全量重跑）。

```ts
async function evalWithSnapshots(task, { resumeFrom }) {
  const snaps = resumeFrom ? await loadSnapshots(task.id) : [];
  for (const m of task.milestones) {
    const hit = snaps.find(s => s.id === m.id);
    if (hit && !affected(hit, changeScope)) { reuse(hit); continue; } // 未受影响复用
    const s = await reachMilestone(m, { save: snapOf(m) });  // 达成即快照
    snaps.push(s);
  }
  return grade(snaps, task.acceptance);
}
```

