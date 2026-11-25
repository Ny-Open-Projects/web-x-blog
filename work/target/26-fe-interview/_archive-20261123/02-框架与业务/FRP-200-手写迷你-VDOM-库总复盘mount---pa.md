---
title: [FRP-200] 手写迷你 VDOM 库总复盘：mount / patch / unmount 全流程如何收束？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-200：手写迷你 VDOM 库总复盘：mount / patch / unmount 全流程如何收束？

**答**：
- 收束前 120 题的手写核心：一个 renderer 只需要四个入口——`mountVNode`（首次挂载）、`patchVNode`（同类型更新）、`diffChildren`（列表变化）、`unmountVNode`（清理）。
- patch 的决策树：类型不同 → unmount 旧 + mount 新（key 重置的底层）；同类型 → 复用 el，比对 props/children；children 按有无 key 走"快速路径"或 keyed diff。
- 组件 vnode 是递归入口：mount 时创建实例并执行 render effect，patch 时 updateProps + 触发自身 effect（FRP-128/129）。
- unmount 的完整性：DOM 移除、组件 scope.stop（FRP-125）、指令 unmounted、ref 置 null、缓存组件真正驱逐——一条链不落就会泄漏。

```javascript
// 简化实现，帮助理解迷你 VDOM 全流程收束
function h(type, props = {}, ...children) {
  return { type, props, children: children.flat(), key: props.key ?? null };
}

// —— mount：入口 ——
function mount(vnode, container) {
  if (typeof vnode.type === 'string')  mountElement(vnode, container);
  else if (typeof vnode.type === 'function') mountComponent(vnode, container);
  else mountText(vnode, container);
}
function mountElement(vnode, container) {
  const el = (vnode.el = document.createElement(vnode.type));
  for (const [k, v] of Object.entries(vnode.props)) {
    if (k.startsWith('on')) el.addEventListener(k.slice(2).toLowerCase(), v);
    else el.setAttribute(k, v);
  }
  vnode.children.forEach(c => mount(typeof c === 'object' ? c : { type: 'text', children: c }, el));
  container.appendChild(el);
}

// —— patch：决策树 ——
function patch(n1, n2, container) {
  if (n1 && !sameType(n1, n2)) {                 // 1. 类型不同：替换
    unmount(n1);
    mount(n2, container);
    return;
  }
  if (typeof n2.type === 'function') return patchComponent(n1, n2);
  const el = (n2.el = n1.el);                    // 2. 同类型：复用 el
  patchProps(el, n1.props, n2.props);
  patchChildren(n1, n2, el);
}

function patchChildren(n1, n2, container) {
  const c1 = normalize(n1.children), c2 = normalize(n2.children);
  // 3. keyed diff：建映射表，双指针 + key 查找（简化版，完整版见 FRP-119）
  const keyed = new Map(c1.map(c => [c.key ?? c, c]));
  let maxIndex = 0;
  for (const child of c2) {
    const old = keyed.get(child.key ?? child);
    if (old) {
      patch(old, child, container);              // 复用：递归 patch
      keyed.delete(child.key ?? child);
    } else {
      mount(child, container);                   // 新增
    }
  }
  for (const leftover of keyed.values()) unmount(leftover); // 删除
}

// —— 组件的 mount/patch：递归入口 ——
function mountComponent(vnode, container) {
  const instance = { vnode, props: reactive(vnode.props), subTree: null };
  vnode.component = instance;
  instance.update = effect(() => {
    const subTree = vnode.type(instance.props);
    if (instance.subTree) patch(instance.subTree, subTree, instance.subTree.el.parentNode);
    else mount(subTree, container);
    instance.vnode.el = subTree.el;
    instance.subTree = subTree;                  // subTree 指针前移
  });
}
function patchComponent(n1, n2) {
  const instance = (n2.component = n1.component);
  updateProps(instance, n1.props, n2.props);     // 父更新 props（FRP-129）
  instance.update();                             // 子自己的 effect 负责重渲染
}

// —— unmount：清理链的完整性 ——
function unmount(vnode) {
  if (typeof vnode.type === 'function') {
    const instance = vnode.component;
    instance.scope?.stop();                      // 响应式清理（FRP-125）
    unmount(instance.subTree);                   // 递归卸载子树
    instance.update.stop?.();
  } else {
    vnode.children?.forEach(c => c.el && unmount(c));
    vnode.el?.parentNode?.removeChild(vnode.el); // DOM 移除
  }
  vnode.ref && (vnode.ref.value = null);         // ref 置空
  if (vnode.dirs) invokeDirectiveHook(vnode, null, 'unmounted');
}

// 验证全流程：
// mount(h('ul', {}, h('li', { key: 1 }, 'a'), h('li', { key: 2 }, 'b')))
// patch(旧, h('ul', {}, h('li', { key: 2 }, 'B'), h('li', { key: 3 }, 'c')))
//   -> key=2 复用 patch（文本 a->B... 此例为 b->B），key=3 mount，key=1 unmount
// 至此：reactive/effect -> 组件模型 -> VDOM diff -> 卸载清理，全部收束为一个 renderer
```
