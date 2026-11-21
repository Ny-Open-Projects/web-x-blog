---
title: [FRP-066] 一个组件从创建到挂载 DOM 的完整初始化流程是怎样的（setup → render → patch）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-066：一个组件从创建到挂载 DOM 的完整初始化流程是怎样的（setup → render → patch）？

**答**：
- 主链路：`createVNode(Comp)`（shapeFlag 标记 COMPONENT）→ `patch(old, vnode)` → `processComponent → mountComponent` → **setupComponent**（initProps → initSlots → setup() 执行，拿到 render 上下文）→ **setupRenderEffect**。
- setupRenderEffect 里创建组件**更新 effect**：`effect(() => instance.subTree = render.call(proxy), { scheduler: queueJob(update) })`——render 期间读响应式数据完成依赖收集，数据变化后走 scheduler 入队而不是同步重跑。
- 得到 subTree 后 `patch(null, subTree, container)` 递归挂载子树（子组件递归 processComponent，元素走 processElement 真正建 DOM），DOM 创建完成后 `queuePostFlushCb` 执行 mounted 钩子。
- 更新时序：数据变 → scheduler 入队 → nextTick flush → 组件 effect 重跑 render → 得到新 subTree → `patch(oldSubTree, newSubTree)` 增量更新。

```javascript
// 简化实现，帮助理解组件初始化全流程
function createVNode(type, props = {}, children = null) {
  return { type, props, children, el: null,
    shapeFlag: typeof type === 'string' ? 1 /* ELEMENT */ : 4 /* COMPONENT */ };
}

function mountComponent(vnode, container) {
  const instance = {
    vnode, props: vnode.props, setupState: null, subTree: null,
    isMounted: false, hooks: { mounted: [] },
  };
  // 1. setupComponent：执行 setup，拿到渲染上下文/返回值
  const setupResult = instance.vnode.type.setup?.(instance.props) || {};
  instance.setupState = typeof setupResult === 'function' ? null : setupResult;
  // 2. setupRenderEffect：组件级更新 effect
  const render = typeof setupResult === 'function'
    ? setupResult
    : instance.vnode.type.render;
  effect(() => {
    if (!instance.isMounted) {
      // 首次：render 生成子树 -> 递归 patch 挂载
      instance.subTree = render(instance.setupState);
      patch(null, instance.subTree, container);
      instance.isMounted = true;
      instance.hooks.mounted.forEach((h) => h()); // post 队列时机
    } else {
      // 更新：新子树与旧子树 diff
      const nextTree = render(instance.setupState);
      patch(instance.subTree, nextTree, container);
      instance.subTree = nextTree;
    }
  }, { scheduler: queueJob }); // 数据变化先入队，微任务统一 flush
  vnode.component = instance;
}

function patch(n1, n2, container) {
  if (n2.shapeFlag & 4) return mountComponent(n2, container); // 简化：不处理 n1 更新分支
  n2.el = document.createElement(n2.type);
  n2.el.textContent = n2.children;
  container.appendChild(n2.el);
}

// 用法：Comp.setup 里读 reactive 数据 -> render 重跑由调度器驱动
const Comp = { setup() { const s = reactive({ n: 1 }); return () => createVNode('p', {}, String(s.n)); } };
mountComponent(createVNode(Comp), document.querySelector('#app'));
```
