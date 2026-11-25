---
title: [FRP-134] 自定义指令的生命周期在 patch 时序中如何安排？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-134：自定义指令的生命周期在 patch 时序中如何安排？

**答**：
- 编译期 `v-focus` 变成 `withDirectives(h(...), [[resolveDirective('focus')], value, arg, modifiers])`，指令对象数组挂到 `vnode.dirs`。
- 运行时在 **mountElement / patchElement 的固定钩子点**同步调用：元素挂载前 `created`，挂载后 `beforeMount→mounted`；更新时 `beforeUpdate`（patch 前，此时能拿到旧 vnode 的 binding）→ patch 后 `updated`。
- `oldValue` 的来源就是"上一次 vnode.dirs 里同位置指令的 value"——patchElement 时先保存旧 dirs 再复用新 dirs。
- 卸载在 `unmount` 时调用 `beforeUnmount/unmounted`；注意指令钩子拿到的 el 都是真实 DOM，没有组件语义（不能在指令里等子组件挂载完）。

```javascript
// 简化实现，帮助理解指令钩子在 patch 中的插入点
function mountElement(vnode, container) {
  const el = (vnode.el = document.createElement(vnode.type));
  // ... 设置 props、children ...

  // created：属性初始化前（此时 el 还没进 DOM）
  if (vnode.dirs) invokeDirectiveHook(vnode, null, 'created');
  // beforeMount：插入前
  if (vnode.dirs) invokeDirectiveHook(vnode, null, 'beforeMount');
  container.appendChild(el);
  // mounted：插入后
  if (vnode.dirs) invokeDirectiveHook(vnode, null, 'mounted');
}

function patchElement(n1, n2) {
  const el = (n2.el = n1.el);
  // 先保留旧 dirs —— oldValue 的来源
  const oldDirs = n1.dirs, newDirs = n2.dirs;
  if (newDirs) invokeDirectiveHook(n2, n1, 'beforeUpdate'); // patch 前：oldValue = 旧 value
  // ... 真正的 props/children patch ...
  if (newDirs) {
    for (const dir of newDirs) dir[0].updated?.(copyBinding(n2, dir, oldDirs)); // patch 后
  }
}

function unmount(vnode) {
  if (vnode.dirs) invokeDirectiveHook(vnode, null, 'beforeUnmount');
  vnode.el?.remove();
  if (vnode.dirs) invokeDirectiveHook(vnode, null, 'unmounted');
}

function invokeDirectiveHook(vnode, prevVNode, name) {
  for (const [dir, value, arg, modifiers] of vnode.dirs) {
    const hook = dir[name];
    hook?.(vnode.el, {
      dir, value,
      oldValue: prevVNode?.dirs?.[vnode.dirs.indexOf([dir, value, arg, modifiers])]?.[1] ?? void 0,
      arg, modifiers,
    }, vnode, prevVNode);
  }
}

// 实战：v-permission 思路 —— 钩子时序决定你能拿到什么
const vFocus = {
  mounted(el) { el.focus(); },                 // 必须在 mounted：insert 前 focus 无效
  updated(el, { value, oldValue }) { if (value !== oldValue) el.focus(); },
};
```

## 二十、Vue3.3+ 新特性原理
