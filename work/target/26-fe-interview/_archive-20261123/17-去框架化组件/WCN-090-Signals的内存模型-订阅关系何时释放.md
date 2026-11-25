---
title: [WCN-090] Signals 的内存模型：订阅关系何时释放？computed 缓存何时失效回收？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-090：Signals 的内存模型：订阅关系何时释放？computed 缓存何时失效回收？

**答**：
- 显式释放：effect.dispose() 清空其 deps（从每个 signal 的 subs 集移除自己）；这是主通道。
- 隐式释放：effect 重跑时重建依赖——先从旧依赖集移除再重新收集，动态分支自动瘦身。
- computed 无引用时：如果没有任何订阅者也不被 effect 读取，其缓存值与 deps 在下次 GC 后可回收（弱引用实现）或实现里主动在"无订阅者时丢弃缓存"（如 Solid 的 onCleanup 语义）。
- 风险：全局 signal 挂着大量 effect 引用 → 每次写入通知所有订阅者（性能），detached DOM 的 effect 未 dispose → 泄漏；模块级 computed 缓存大对象也会滞留内存。
- 工程约定：组件级 effect 必须随生命周期 dispose；全局 store 的 effect 数量纳入性能预算；大对象缓存加 LRU 或改为按需 computed。

```javascript
// 依赖重建瘦身示例：分支切换后旧分支 signal 不再被订阅
const a = signal(1), b = signal(2), mode = signal('a');
effect(() => {
  console.log(mode() === 'a' ? a.value : b.value);
});
mode.value = 'b';
// 下次 run：先移除对 a 的订阅，再订阅 b —— a 的 subs 集不再包含该 effect
// 若此后 a 无任何订阅者且无引用，a 的缓存可被回收
```
