---
title: [JS-224] WeakMap/WeakSet 为什么能防泄漏
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 内存]
type: 面试题
---

## JS-224：WeakMap/WeakSet 为什么能防泄漏

**答**：
- 弱引用：键对象不被 WeakMap 计入可达性——其他引用全消失时，键值对自动被 GC 收走
- 对比 Map：Map 键是强引用，DOM 元素即使已从页面移除，只要还在 Map 里就永远不能回收
- 典型场景：给 DOM/对象附加元数据（缓存计算结果、事件绑定标记）、私有数据、对象池标记
- 限制：键只能是对象；不可遍历、无 size、无 clear——「弱」的代价就是无法枚举
- 面试话术：WeakMap 是「给对象挂标签但不延长它的命」的数据结构

```javascript
const sizes = new WeakMap();
function measure(el) {
  if (!sizes.has(el)) sizes.set(el, el.getBoundingClientRect().width);
  return sizes.get(el);
}
// el 从页面移除并失去其他引用后，缓存条目自动消失——无需手动清理
```
