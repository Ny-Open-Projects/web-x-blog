---
title: [FRP-128] VNode 与组件实例之间是如何互相引用的（instance.vnode / subTree）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-128：VNode 与组件实例之间是如何互相引用的（instance.vnode / subTree）？

**答**：
- 三条核心指针：**组件 vnode.component** 指向组件实例；**instance.vnode** 指向"代表该组件的那个 vnode"（携带 props/children/=key）；**instance.subTree** 指向组件 render 产出的**子树根 vnode**。
- 组件本身没有 `el`——真实 DOM 在子树的叶子 vnode 上，所以取"组件根元素"是 `instance.subTree.el` 一路下探。
- 更新时：新组件 vnode 与 `instance.vnode` 比对 → 更新 `instance.vnode`（指向新 vnode，保持最新 props）→ 重渲染出新 subTree → `patch(旧subTree, 新subTree)` → subTree 指针前移。
- `next` 指针（instance.next = 新 vnode）是异步更新队列里的"待更新目标"，updateComponent 时消费它。

```javascript
// 简化实现，帮助理解 vnode 与组件实例的双向指针
function createComponentInstance(vnode) {
  return {
    vnode,          // 指向"我"这个组件 vnode
    subTree: null,  // 指向 render 产出的子树根 vnode
    props: shallowReactiveProps(vnode.props),
    isMounted: false,
    update: null,   // 自己的渲染 effect
  };
}

function mountComponent(vnode, container) {
  const instance = createComponentInstance(vnode);
  vnode.component = instance;                        // 指针1：vnode -> instance
  const subTree = instance.render(instance.props);   // 执行 render 得到子树
  instance.subTree = subTree;                        // 指针2：instance -> subTree
  patch(null, subTree, container);
  vnode.el = subTree.el;                             // 组件的 el 从子树根借来
  instance.isMounted = true;

  // 更新 effect：响应式数据变化时重新执行
  instance.update = effect(() => {
    if (!instance.isMounted) return;
    const nextTree = instance.render(instance.props);          // 新子树
    patch(instance.subTree, nextTree, subTree.el.parentNode);  // patch 子树
    instance.vnode.el = nextTree.el;
    instance.subTree = nextTree;                               // 指针前移！
  });
}

function updateComponent(n1, n2) {   // 父组件 patch 到一个"组件 vnode"时
  const instance = (n2.component = n1.component);
  instance.next = n2;                              // 暂存新 vnode
  instance.vnode = n2;                             // 更新 vnode 指针（新 props 生效）
  instance.next = null;
  // 触发子组件自身的更新 effect（等价源码里 updateComponentPreRender + effect.run）
  instance.update();
}

// 关键验证：组件的 el 是"借"的
const vnode = { type: Child, props: { msg: 1 }, component: null, el: null };
// mount 后：vnode.el === vnode.component.subTree.el（子树根元素）
```
