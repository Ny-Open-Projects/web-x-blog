---
title: [DP-086] Vue3 源码里能识别出哪些设计模式？（高频压轴）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-086：Vue3 源码里能识别出哪些设计模式？（高频压轴）
**答**：
- **代理模式**：`reactive()` 用 Proxy 拦截 get/set/delete；`ref` 的 get/set 拦截 `.value` 访问。
- **观察者**：effect/track/trigger——依赖收集与派发更新；watch/computed 都是订阅者。
- **策略 + 工厂**：`processElement/processText/processCommentary` 按 vnode 类型分派 patch 策略；`createRenderer` 接收节点操作对象生成平台渲染器（自定义渲染到 canvas/小程序）。
- **组合 + 迭代器**：vnode 树递归 patch；**备忘录**：keep-alive 缓存组件实例；**享元**：静态 vnode 提升与 patchFlag 复用。

```javascript
// Vue3 源码模式速览（简化对照 runtime-core/reactivity）
// 1. 工厂 + 策略：createRenderer 注入平台操作，生成渲染器
function createRenderer(nodeOps) {
  return {
    patch(n1, n2, container) {
      if (n1 && !isSameType(n1, n2)) unmount(n1);       // 策略1：不同类型 -> 替换
      if (typeof n2.type === 'string') processElement(n2, container, nodeOps);   // 策略2：元素
      else if (typeof n2.type === 'object') processComponent(n2, container);     // 策略3：组件
      else if (n2.type === Text) processText(n2, container, nodeOps);            // 策略4：文本
    },
  };
}
const nodeOps = { // DOM 平台的节点操作（可整体替换为 canvas/小程序实现）
  createElement: (tag) => document.createElement(tag),
  insert: (child, parent, anchor) => parent.insertBefore(child, anchor),
  remove: (el) => el.parentNode?.removeChild(el),
  setElementText: (el, text) => { el.textContent = text; },
};
const renderer = createRenderer(nodeOps);
console.log(typeof renderer.patch); // function

// 2. 代理 + 观察者：reactive/ref 双通道（见 DP-032/DP-046 细节）
function ref(value) {
  return {
    get value() { trackRef(this); return value; },       // 代理模式：拦截 .value 读
    set value(nv) { value = nv; triggerRef(this); },     // 观察者：通知 effect
  };
}
// 3. 备忘录：keep-alive 缓存组件 vnode（快照复用，LRU 淘汰）
function createKeepAlive(max = 10) {
  const cache = new Map(); // key -> 缓存的 vnode/组件实例（快照）
  return {
    cacheVNode(key, vnode) {
      if (cache.size >= max) cache.delete(cache.keys().next().value); // LRU
      cache.set(key, vnode);
    },
    getCached(key) { return cache.get(key); },
  };
}
const ka = createKeepAlive(2);
ka.cacheVNode('a', { type: 'A' });
console.log(ka.getCached('a')); // { type: 'A' } —— 切换回来无需重建
```
