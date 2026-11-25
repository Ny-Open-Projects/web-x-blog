---
title: [AIC-916] 把商品详情的 20 个改造任务并行扔给多个 Agent，「写集」应该如何划分才不会互相踩踏？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-916：把商品详情的 20 个改造任务并行扔给多个 Agent，「写集」应该如何划分才不会互相踩踏？
**答**：
- 按「模块/目录边界」垂直切分而非按「功能横向」切：让每个 Agent 负责完整的一个模块（自己的组件+样式+测试），避免多个 Agent 都改同一批公共文件。
- 公共文件（配置、路由入口、全局类型）单独分配给「协调者 Agent」或人工，其他任务通过 import 使用，不直接写。
- 写集要在任务分派时显式声明并登记（哪个 Agent 可写哪些路径），运行前做重叠预检，有重叠就调整分派。
- 追问钩子：能提出「写集划分本质是架构的模块边界问题，模块耦合度高时再怎么切分都会冲突，要先解耦」的候选人看到了更深一层。

```typescript
// 写集登记与重叠预检
const tasks = [
  { id:1, agent:'a', writes:['ui/Card.tsx','ui/Card.css'] },
  { id:2, agent:'b', writes:['ui/Card.tsx','api/get.ts'] }, // 与任务1重叠!
];
function precheck(tasks) {
  const owner = new Map(), overlaps = [];
  for (const t of tasks) for (const p of t.writes) {
    if (owner.has(p)) overlaps.push({ path:p, tasks:[owner.get(p), t.id] });
    else owner.set(p, t.id);
  }
  return { ok: !overlaps.length, overlaps };
}
const r = precheck(tasks);
// 不 ok → 重新分派：让任务2只写 api，Card.tsx 由任务1独占
console.log(r);
```
