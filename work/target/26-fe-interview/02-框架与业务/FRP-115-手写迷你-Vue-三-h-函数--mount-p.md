---
title: [FRP-115] 手写迷你 Vue（三）：h 函数 + mount/patch 渲染器？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-115：手写迷你 Vue（三）：h 函数 + mount/patch 渲染器？

**答**：
- 渲染器接口：`h(type, props, children)` 造 vnode（记录 shapeFlag）；`render(vnode, container)` 首次 mount、之后拿新旧 vnode 走 `patch(n1, n2)`。
- patch 三分支：**同类型元素** → patchProps（新旧 props 双向 diff）+ patchChildren；**类型不同** → unmount 旧 + mount 新（无跨类型复用）；**文本** → 直接改 textContent。
- children 的三态处理：字符串文本 ↔ 数组子节点 ↔ null，两两组合九种情况中最关键的是"数组→数组"（交给 keyed diff，见 FRP-119）与"文本↔数组"的清理。
- 事件 props 约定 `onXxx` → addEventListener；其余走 setAttribute / DOM property。

```javascript
// 简化实现，帮助理解：最小可用渲染器
function h(type, props = {}, children = null) {
  return { type, props, children, el: null,
    shapeFlag: typeof children === 'string' ? 'TEXT_CHILD' : 'ARRAY_CHILD' };
}

function mount(vnode, container) {
  const el = (vnode.el = document.createElement(vnode.type));
  for (const k in vnode.props) patchProp(el, k, null, vnode.props[k]);
  if (vnode.shapeFlag === 'TEXT_CHILD') el.textContent = vnode.children;
  else vnode.children?.forEach((c) => mount(c, el));
  container.appendChild(el);
}

function patchProp(el, key, oldVal, newVal) {
  if (key.startsWith('on')) {                                  // 事件
    const evt = key.slice(2).toLowerCase();
    oldVal && el.removeEventListener(evt, oldVal);
    newVal && el.addEventListener(evt, newVal);
  } else if (newVal == null) el.removeAttribute(key);
  else el.setAttribute(key, newVal);
}

function patch(n1, n2) {
  if (n1.type !== n2.type) {                                    // 类型不同：替换
    const anchor = n1.el.nextSibling;
    unmount(n1); mount(n2, n1.el.parentNode);
    n1.el.parentNode.insertBefore(n2.el, anchor);
    return;
  }
  const el = (n2.el = n1.el);                                   // 复用 DOM
  // props diff：以新为准，旧的删多的
  const oldProps = n1.props, newProps = n2.props;
  for (const k in newProps) if (oldProps[k] !== newProps[k]) patchProp(el, k, oldProps[k], newProps[k]);
  for (const k in oldProps) if (!(k in newProps)) patchProp(el, k, oldProps[k], null);
  // children diff：九态中最关键的两种
  if (n2.shapeFlag === 'TEXT_CHILD') {
    if (n1.shapeFlag === 'ARRAY_CHILD') el.innerHTML = '';      // 数组 -> 文本：清空再写
    if (n1.children !== n2.children) el.textContent = n2.children;
  } else if (n1.shapeFlag === 'TEXT_CHILD') {
    el.textContent = '';
    n2.children.forEach((c) => mount(c, el));                   // 文本 -> 数组
  } else {
    keyedDiff(n1.children, n2.children, el);                    // 数组 -> 数组
  }
}
function unmount(vnode) { vnode.el.remove(); }
function keyedDiff(oldCh, newCh, container) { /* 见 FRP-119，此处省略为重建 */ 
  oldCh.forEach(unmount); newCh.forEach((c) => mount(c, container));
}

// 验证：点击按钮切换文案（更新走 patch，DOM 复用）
const state = reactive({ msg: 'A' }); // reactive 来自 FRP-113
let oldVnode = h('div', { class: 'box' }, state.msg);
mount(oldVnode, document.querySelector('#app'));
effect(() => { // effect 来自 FRP-113
  const newVnode = h('div', { class: 'box' }, state.msg);
  patch(oldVnode, newVnode);
  oldVnode = newVnode;
});
state.msg = 'B'; // DOM 文本变为 B，div 元素未重建
```
