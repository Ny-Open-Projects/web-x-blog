---
title: [JS-060] WeakMap/WeakSet 的弱引用有什么用途？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-060：WeakMap/WeakSet 的弱引用有什么用途？

**答**：
- 键必须是对象且为弱引用：键对象在别处无引用时可被 GC，WeakMap 不阻止回收。
- 不可遍历、没有 size/clear，正因为生命周期不可预测。
- 典型用途：给 DOM/组件实例附加元数据、私有数据存储、对象级缓存。
- 拿 WeakMap 当“对象 → 数据”侧表，避免污染对象本身。

```javascript
const metadata = new WeakMap();
const dom = document.querySelector('#app'); // 浏览器环境示例
metadata.set(dom, { mountedAt: Date.now() });
console.log(metadata.get(dom)); // {mountedAt: ...}
// dom 被移除且无其他引用后，metadata 中的条目可被整体回收

class Component {
  #state = new WeakMap(); // 实例私有状态（防止外部访问实例时顺带暴露）
  bind(el) {
    this.#state.set(el, { clicks: 0 });
  }
}

// 缓存场景：结果随 key 对象生命周期
const cache = new WeakMap();
function compute(obj) {
  if (!cache.has(obj)) cache.set(obj, heavyCalc(obj));
  return cache.get(obj);
}
function heavyCalc(o) { return Object.keys(o).length; }
```
