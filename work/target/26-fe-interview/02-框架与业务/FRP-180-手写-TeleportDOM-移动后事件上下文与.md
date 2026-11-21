---
title: [FRP-180] 手写 Teleport：DOM 移动后事件上下文与 patch 如何保持正确？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-180：手写 Teleport：DOM 移动后事件上下文与 patch 如何保持正确？

**答**：
- 核心三步：正常创建子树的 DOM → **appendChild 到目标容器**（真实移动）→ unmount 时从目标容器移除。
- patch 正确性的关键：vnode.el 引用不因移动失效（el 是 DOM 引用，位置无关），后续 patch 沿 vnode 走，更新的是"内容"不是"位置"。
- 事件上下文：DOM 移动后事件按**新位置**冒泡——teleport 到 body 后事件不再经过原父组件的 DOM 层级，但 Vue 的合成依赖是 vnode 树不是 DOM 树，所以 @click 仍正常。
- props 变化（to 改变）：需要把已挂载的 DOM 移到新容器；disabled=true 时回移到原位置。

```javascript
// 简化实现，帮助理解 Teleport
const Teleport = {
  __isTeleport: true,
  process(n1, n2, container, anchor, ...args) {
    const { to, disabled } = n2.props;
    if (n1 == null) {
      // mount：先渲染到占位容器，再移动到目标
      const target = typeof to === 'string' ? document.querySelector(to) : to;
      if (disabled) {
        // disabled：留在原位置（行为同普通渲染）
        mountChildren(n2.children, container, anchor);
        n2.el = container.lastChild?.parentNode; // 简化
      } else {
        const placeholder = document.createComment('teleport-start');
        mountChildren(n2.children, placeholder /* 临时容器 */);
        n2.children.forEach(child => target.appendChild(child.el)); // 移动！
        n2.el = n2.children[0]?.el;
        n2.target = target;
        n2.anchor = anchor;                      // 记录原位置锚点，disabled 切换时回移
      }
    } else {
      // update：children 照常 patch（el 引用不变），props 变化则移动
      patchChildren(n1, n2, n1.target ?? container);
      if (n1.target !== n2.target && n2.target) {
        n2.children.forEach(child => n2.target.appendChild(child.el)); // 换目标
      }
      if (n1.props.disabled !== n2.props.disabled) {
        // disabled 切换：在原位置与目标之间往返
        const dest = n2.props.disabled ? n2.anchor.parentNode : n2.target;
        n2.children.forEach(child => dest.insertBefore(child.el, n2.props.disabled ? n2.anchor : null));
      }
    }
  },
  remove(vnode) {
    // unmount：从目标容器移除（不是从原位置）
    vnode.children.forEach(child => vnode.target?.removeChild(child.el));
  }
};

// 渲染器分发：
function patch(n1, n2, container) {
  if (n2.type.__isTeleport) return n2.type.process(n1, n2, container); // 特殊类型单独 process
  // ...
}
// 用法：
// <Teleport to="body">
//   <Modal @close="show = false" />   事件仍走 vnode 树 -> 正常
// </Teleport>
// 移动后 Modal 的 DOM 在 body 下，点击它的事件按 body 层级冒泡——
// 但 Vue 的组件事件链基于 vnode/instance，不受 DOM 移动影响
```
