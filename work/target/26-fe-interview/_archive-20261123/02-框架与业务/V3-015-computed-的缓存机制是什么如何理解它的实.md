---
title: [V3-015] computed 的缓存机制是什么？如何理解它的实现？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-015：computed 的缓存机制是什么？如何理解它的实现？
**答**：
- computed 依赖不变时返回缓存值，不会重复计算 getter。
- 内部用 dirty 标记：依赖变更时只把 dirty 置 true 并通知外层 effect，真正读取时才重算。
- computed 也是 effect，惰性求值 + 缓存使它天然适合派生状态。
- 链式 computed 的更新也遵循"先标脏、再按需计算"的调度。

```javascript
// computed 核心特征：依赖不变时返回缓存值（简化实现）
function computed(getter) {
  let value;
  let dirty = true; // 标记是否需要重新计算
  const runner = () => {
    if (dirty) {
      value = getter();
      dirty = false;
    }
    return value;
  };
  // 依赖变化时（trigger 回调）：把 dirty 置回 true，并通知订阅者重新读取
  return {
    get value() {
      trackSelf(); // 把 computed 自身作为依赖收集给外层 effect（示意）
      return runner();
    },
  };
}

function trackSelf() {} // 示意占位
```
