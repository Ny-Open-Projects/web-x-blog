---
title: [WCN-247] Signals 的内存模型：依赖收集的 WeakMap/引用管理与泄漏场景？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-247：Signals 的内存模型：依赖收集的 WeakMap/引用管理与泄漏场景？
**答**：
- 依赖收集在「计算期」临时图（全局当前订阅者栈），计算完存到节点——不保留中间栈。
- 泄漏场景 1：effect 永不销毁（组件卸载未 dispose）→ 图越来越大。
- 泄漏场景 2：动态分支依赖（if 内读取）导致依赖集只增不减——需 reset 机制（每次计算重建依赖）。
- WeakMap 缓存 computed 缓存：宿主对象被 GC 时缓存自动清理。

```javascript
let currentSubs: Sub[] = [];
function track(node) { if (currentSubs.length) currentSubs[currentSubs.length - 1].deps.add(node); }
function compute(fn) {
  currentSubs.push(node);
  node.deps = new Set();          // 每次重建：动态分支依赖自然清理
  const v = fn();
  currentSubs.pop();
  return v;
}
r
```
