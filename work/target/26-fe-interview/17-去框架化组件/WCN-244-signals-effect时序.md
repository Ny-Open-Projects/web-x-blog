---
title: [WCN-244] effect 的执行时机与「读取到的值」一致性如何保证？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-244：effect 的执行时机与「读取到的值」一致性如何保证？
**答**：
- effect 在 flush 尾部执行，此时所有 computed 已重算——effect 读到的全是新值。
- 多个 effect 之间按注册顺序（或拓扑序）执行——依赖其他 effect 副作用时要声明顺序。
- untracked 读取：effect 内读取不建立依赖的信号（快照语义）。
- 坑：effect 内写 signal 会触发新一轮 flush——规范上禁止/或作为下一轮处理。

```javascript
effect(() => {
  const total = totalPrice();          // 新值（computed 已重算）
  const prev = untracked(() => lastSaved());  // 不建立依赖
  if (total !== prev) save(total);
});
r
```
