---
title: [FRP-102] Signals 提案（TC39）的核心思想是什么？它与 Vue 的 ref 有何异同？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-102：Signals 提案（TC39）的核心思想是什么？它与 Vue 的 ref 有何异同？

**答**：
- 共同模型：**信号 = 值 + 订阅者集合 + 自动依赖追踪**。读取信号时（在 effect/computed 上下文中）记录依赖，写入时通知，可按拓扑序传播（先算 computed 再通知 effect）。
- Signals 提案的核心增强：**图调度与状态标记**——写入只做"标脏"（dirty/clean 状态机），effect 的重算推迟到统一 flush；computed 只在**有活跃消费者**时才被重新计算（无订阅即释放），依赖变化但**计算结果相等时通知会中断**（`equal` 比较短路，避免无谓重渲染）。
- 与 Vue ref 的差异：Vue ref 依赖收集是"运行时即时收集 + 同步触发重跑（组件更新走队列）"，没有内建的图状态机与相等短路；Signals 提案把**惰性求值 + 相等中断**作为一等公民。
- 借鉴关系：Vue 3.4+ 的 Dep 类重构、Solid/Preact Signals 都收敛到这一模型；掌握它等于掌握了新一代响应式的公共内核。

```javascript
// 简化实现，帮助理解 Signals 的图调度与相等短路
let active = null;
function signal(value, isEqual = (a, b) => a === b) {
  const s = {
    subs: new Set(), dirty: false, value,
    get() { if (active) s.subs.add(active); return s.value; },
    set(v) {
      if (isEqual(v, s.value)) return;        // 相等短路：传播在源头中断
      s.value = v;
      s.subs.forEach((sub) => sub.markDirty?.() ?? sub()); // 标脏或直接通知
    },
  };
  return s;
}
function computed(fn) {
  const c = {
    subs: new Set(), value: undefined, dirty: true,
    get() {
      if (this.dirty) {                       // 惰性：有消费者读取才重算
        active = c;
        this.value = fn();
        active = null;
        this.dirty = false;
      }
      if (active) c.subs.add(active);         // computed 也能被下游依赖
      return this.value;
    },
    markDirty() {
      if (this.dirty) return;                 // 已脏：去重，防止重复传播
      this.dirty = true;
      // 关键：先重算自己，若结果相等则不再打扰下游（通知中断）
      const prev = this.value;
      const next = (() => { active = c; const v = fn(); active = null; return v; })();
      if (next !== prev) {
        this.value = next;
        this.subs.forEach((sub) => sub.markDirty?.() ?? sub());
      }
      this.dirty = false;
    },
  };
  return c;
}
function effect(fn) { const run = () => { active = run; fn(); active = null; }; run(); return run; }

const a = signal(1);
const b = computed(() => a.get() * 2);
effect(() => console.log('effect sees b =', b.get())); // effect sees b = 2
a.set(2);                                              // effect sees b = 4
a.set(3); b.get();                                     // 惰性：无人读 b 时不重算
b.get();                                               // 已缓存 6，不再执行 fn
```
