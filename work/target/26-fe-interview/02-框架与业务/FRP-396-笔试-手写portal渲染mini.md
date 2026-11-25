---
title: [FRP-396] 笔试：手写 Portal 渲染（mini 实现）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-396：笔试：手写 Portal

**答**：在 mini vdom 上实现 Portal：① `createPortal(vnode, container)`：特殊 vnode（$$portal 标记）；② mount：children 挂到目标 container（DOM 位置分离）；③ patch：portal 子树正常 diff（只是挂载点不同）；④ 卸载：从目标 container 清理；⑤ 事件语义说明：DOM 事件在目标容器冒泡（不回到 React 树的父级 DOM）——但逻辑树 parent 关系保留（Context 穿透）。写出实现。

```javascript
const PORTAL = Symbol('portal');
function createPortal(vnode, container) {
  return { $$portal: PORTAL, vnode, container };
}
function mountVNode(vnode, container) {
  if (vnode.$$portal === PORTAL) {
    mount(vnode.vnode, vnode.container);            // 挂到目标容器
    vnode._mountedIn = vnode.container;              // 记录(卸载用)
    return;
  }
  /* ...普通 mount... */
}
function patchVNode(n1, n2) {
  if (n1.$$portal && n2.$$portal) {
    n2.el = n1.el;                                   // 复用子树
    patch(n1.vnode, n2.vnode);                       // 子树正常 diff
    if (n1.container !== n2.container) {             // 目标容器变化: 迁移
      n2.container.appendChild(n1.vnode.el);
      n2._mountedIn = n2.container;
    }
    return;
  }
  /* ... */
}
function unmountVNode(vnode) {
  if (vnode.$$portal) {
    unmount(vnode.vnode);                            // 从目标容器清理
    return;
  }
  /* ... */
}
// 事件语义: DOM 冒泡在目标容器链(不回 React 树父 DOM)
//           逻辑树(parent fiber/vnode)不变 → Context/provide 穿透正常
```

**评分点**：
- $$portal 标记的分派（mount/patch/unmount 三处）
- 子树复用 diff（portal 不阻碍正常更新）
- 目标容器变更的迁移处理
- 「DOM 冒泡 vs 逻辑树」两层语义的准确表述
