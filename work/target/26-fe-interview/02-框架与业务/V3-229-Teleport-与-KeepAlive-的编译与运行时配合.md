---
title: [V3-229] Teleport 与 KeepAlive 在编译与运行时各是怎么配合的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-229：Teleport 与 KeepAlive 在编译与运行时各是怎么配合的？
**答**：
- Teleport：编译为 `createVNode(Teleport, { to, disabled }, children)`；运行时 mount 时把锚点 children 挂到目标容器，patch 时**children 在原位置 diff、DOM 挂载点在别处**，依赖 `targetAnchor` 保序。
- KeepAlive：不是编译糖而是**运行时内置组件**，包裹动态组件时拦截其 vnode，用缓存 map 保存 vnode.el 与实例，激活时把缓存 DOM 移回容器。
- 二者组合：`<Teleport><KeepAlive><Comp/></KeepAlive></Teleport>`，KeepAlive 缓存的 DOM 移回 Teleport 的目标容器，requiresProps/activated 钩子照常。
- 面试考点：KeepAlive 为什么必须独占 default slot（单子）？——缓存 key 唯一性；Teleport 的 disabled 切换是"移动 DOM"而非重挂载，状态不丢。
- SSR：Teleport 在服务端渲染为 teleports 缓冲区（`renderToString` 的 teleports 字段），客户端 hydrate 到指定容器。

```javascript
// KeepAlive 渲染核心（简化）
render() {
  const children = this.$slots.default();
  const rawVnode = children[0];
  const comp = rawVnode.type;
  const key = rawVnode.key ?? comp;
  const cached = cache.get(key);
  if (cached) { // 命中：复用 vnode 与 DOM，标记 SHAPE
    rawVnode.el = cached.el; rawVnode.component = cached.component;
    rawVnode.shapeFlag |= ShapeFlags.COMPONENT_SHOULD_KEEP_ALIVE;
  }
  rawVnode.shapeFlag |= ShapeFlags.COMPONENT_KEPT_ALIVE;
  return rawVnode;
}
// Teleport 挂载：mount children 到 target 容器 + 在父容器留 targetAnchor 占位
```
