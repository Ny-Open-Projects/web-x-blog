---
title: [V3-206] Vue 3.5 响应式重构对 Effect 内部结构做了哪些精简？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-206：Vue 3.5 响应式重构对 Effect 内部结构做了哪些精简？
**答**：
- 字段瘦身：ReactiveEffect 从携带 `deps: Dep[]`（数组的数组）+ 多个标志位，精简为 `deps/depsTail`（链表头尾）+ 少量位标志。
- 位标志（flag）合并：`RUNNING/DIRTY/PAUSED` 等状态压缩进一个 number 字段按位读写，减少对象字段数量。
- 去掉独立 cleanup 函数数组：cleanup 改为 `unlink` 链表节点，不再维护 `onCleanup` 回调数组（用户层 `onWatcherCleanup` API 仍保留）。
- 递归转迭代：依赖收集与触发链路用迭代替代部分递归，减少调用栈深度。
- 收益量化：官方数据内存 -56%，`reactive` 创建速度更快；对万级组件应用（如中后台大表格）收益最直观。

```javascript
// 结构对比（示意）
// 3.4 ReactiveEffect
{ active, running, deps: [], cleanup: [], scheduler, fn }
// 3.5 ReactiveEffect
{
  deps: null, depsTail: null,   // 依赖链表头尾
  flags: 0,                     // RUNNING|NOTIFIED|PAUSED|DIRTY 位标志
  next: null,                   // 调度队列链表（替代数组 queue）
  fn, scheduler,
}
// 位标志操作
const DIRTY = 1 << 2;
if (effect.flags & DIRTY) { effect.flags &= ~DIRTY; effect.run(); }
```
