---
title: [V3-466] KeepAlive 的编译与运行时衔接：缓存键如何确定
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-466：KeepAlive 的编译与运行时衔接：缓存键如何确定

**答**：
- KeepAlive 是编译器友好的内置组件：单 child 约束（编译器允许多个 child 但运行时只取第一个非注释节点）——「包裹多个元素只生效一个」的坑来自这里
- 缓存键确定逻辑： vnode.key（显式 key）→ vnode.type（组件对象/构造器）→ include/exclude 按组件 name 匹配——组件没 name 且在 KeepAlive 内时 dev 有告警
- include/exclude 的匹配时机：在 KeepAlive 的 render（update）里对 vnode.type.name 正则/字符串匹配——被排除的组件走普通渲染（不缓存）
- max 与 LRU：缓存 Map + max 上限，超出淘汰最旧（ eldest key）——淘汰组件实例触发 unmounted（不是 deactivated）
- 深水点：KeepAlive 的缓存是「vnode + 组件实例容器」双份——激活时把缓存 vnode 重新插入容器（move 移动 DOM 而不是重建），DOM 状态（滚动位置等非 Vue 管理的）因此保留

```javascript
// KeepAlive render 核心逻辑(简化)
const key = vnode.key == null ? comp : vnode.key;
if (include && !matches(include, name)) return vnode;   // 不缓存直接返回
const cached = cache.get(key);
if (cached) { vnode.el = cached.el; ... pendingCacheKey = key; }  // 复用 DOM
```
