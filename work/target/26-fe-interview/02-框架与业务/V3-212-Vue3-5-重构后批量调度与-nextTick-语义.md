---
title: [V3-212] Vue 3.5 重构后批量更新调度与 nextTick 语义有没有变化？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-212：Vue 3.5 重构后批量更新调度与 nextTick 语义有没有变化？
**答**：
- 语义不变：同 tick 多次修改仍合并为一次更新，`nextTick` 仍在微任务 flush 后 resolve，这是 3.5 重构明确保持的兼容点。
- 内部变化：调度队列从数组（`queue.push + sort`）优化为**基于优先级的链表插入**，去重靠 effect 的 `next` 指针，免去 sort。
- 效果：一次 flush 中大量 effect 入队时不再有 O(n log n) 排序开销，父子组件更新顺序仍按 uid 保证。
- flushJobs 时序：pre flush（组件更新前）→ 渲染 → post flush（updated 钩子），三层队列顺序与 3.4 一致。
- 追问钩子：为什么调度链表不需要显式排序？——插入时按 id 找位置，天然有序。

```javascript
// 链表式调度队列（3.5 思想）
let queueHead, queueTail;
function queueJob(effect) {
  if (effect.flags & QUEUED) return;   // 已在队列，去重
  effect.flags |= QUEUED;
  // 按 id（创建顺序）插入到链表正确位置，保证父先于子
  if (!queueHead || effect.id < queueHead.id) {
    effect.next = queueHead; queueHead = effect;
    if (!queueTail) queueTail = effect;
  } else {
    let cur = queueHead;
    while (cur.next && cur.next.id < effect.id) cur = cur.next;
    effect.next = cur.next; cur.next = effect;
    if (!effect.next) queueTail = effect;
  }
}
```
