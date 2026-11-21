---
title: [FRP-017] Teleport 是如何实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-017：Teleport 是如何实现的？

**答**：
- `<Teleport to="#modal">` 让子树渲染到指定容器，但**逻辑上仍留在组件树中**（props/inject/事件链不断）。
- 实现要点：Teleport 是特殊 vnode（shapeFlag = TELEPORT），编译/运行时生成一个**注释占位符**锚点插在原位置，真实 children 挂载到 target 容器。
- 更新时通过锚点找到真实位置做 patch；`disabled` 属性可切回原位挂载；SSR 时直接渲染进目标容器字符串。
- 价值：modal/tooltip 逃逸 `overflow: hidden`、`z-index` 层级上下文的限制，而组件通信不中断。

```javascript
// 简化实现，帮助理解 Teleport 的锚点与跨容器挂载
function mountTeleport(vnode, container) {
  // 1. 原位置插入注释锚点：占位 + 更新时定位用
  const anchor = document.createComment('teleport start');
  container.appendChild(anchor);

  vnode.el = anchor;
  vnode.anchor = anchor;

  // 2. 真实 children 挂到目标容器，而不是当前父容器
  const target = document.querySelector(vnode.props.to);
  vnode.target = target;
  vnode.children.forEach((child) => mount(child, target));

  vnode.props.onMounted?.();
}

function patchTeleport(n1, n2) {
  n2.el = n1.el;
  n2.target = n1.target;
  // 子树更新仍然基于原 anchor 与 target，逻辑父子关系不受影响
  if (n1.props.disabled !== n2.props.disabled) {
    // disabled 从 true 变 false 等：把 children 移回原位/移回目标
    moveChildren(n2, n2.props.disabled ? n1.el.parentNode : n2.target);
  }
  diffChildren(n1.children, n2.children, n2.target);
}

function unmountTeleport(vnode) {
  vnode.children.forEach((child) => unmount(child)); // 从目标容器卸载
  vnode.el.parentNode.removeChild(vnode.el);         // 移除锚点
}
```
