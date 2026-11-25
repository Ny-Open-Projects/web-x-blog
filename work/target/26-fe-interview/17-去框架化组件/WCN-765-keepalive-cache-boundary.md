---
title: [WCN-765] 编译器如何处理动态组件与 keep-alive 的缓存边界？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-765：编译器如何处理动态组件与 keep-alive 的缓存边界？

**答**：
- 结论：动态组件（`<component :is>`）编译为运行时按 is 值解析构造函数的代码；keep-alive 编译为带 cache（Map by key）与 LRU 的包裹节点，命中缓存则复用 vnode 与组件实例。
- 缓存边界由 include/exclude/max 决定，编译期可常量化的条件提前计算；被缓存组件 activate/deactivate 生命周期由运行时触发。
- 追问钩子：缓存的组件如何感知 props 变化？考察「activated 时用新 props 更新实例而非重新创建」。

```javascript
function KeepAlive(renderChild) {
  const cache = new Map(), MAX = 5;
  return (key, props) => {
    if (cache.has(key)) {
      const cached = cache.get(key);
      cached.instance.updateProps?.(props);        // 复用实例，更新 props
      cached.vnode.activated = true;
      return cached.vnode;
    }
    const vnode = renderChild(key, props);
    cache.set(key, { vnode, instance: vnode.instance });
    if (cache.size > MAX) cache.delete(cache.keys().next().value); // LRU
    return vnode;
  };
}
const render = KeepAlive((key) => ({ tag: key, instance: { updateProps() {} } }));
console.log(render('PageA', {}).tag);
```
