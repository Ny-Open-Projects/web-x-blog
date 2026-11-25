---
title: [WCN-764] 笔试：手写基于编译产物的增量 DOM patch 函数
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-764：笔试：手写基于编译产物的增量 DOM patch 函数

**答**：
- 需求：实现 `patch(el, vnode)`，vnode 形如 `{ tag, props?, children?: (vnode|string)[] }`。按增量策略更新真实 DOM：tag 不同则替换；props 做增删（新 props 中不存在则移除旧属性）；children 按索引递归 patch，文本节点直接改 textContent。返回更新后的 el。
- 要点：props 比较用 ===；children 长度不一致时截断/追加；边界：vnode 为空、children 类型混合。

```javascript
function patch(el, vnode) {
  if (!vnode) return el;
  if (!el || el.nodeType === 3 || el.tagName?.toLowerCase() !== vnode.tag) {
    const next = document.createElement(vnode.tag);
    el?.replaceWith?.(next);
    el = next;
  }
  // props 更新：先删旧，再设新
  for (const attr of [...el.attributes]) {
    if (!(attr.name in (vnode.props || {}))) el.removeAttribute(attr.name);
  }
  for (const [k, v] of Object.entries(vnode.props || {})) {
    if (el.getAttribute(k) !== String(v)) el.setAttribute(k, v);
  }
  // children 按索引 patch
  const kids = vnode.children || [];
  [...el.childNodes].forEach((child, i) => patch(child, kids[i]));
  for (let i = el.childNodes.length; i < kids.length; i++) {
    const k = kids[i];
    el.appendChild(typeof k === 'string' ? document.createTextNode(k)
      : (() => { const n = document.createElement(k.tag); patch(n, k); return n; })());
  }
  return el;
}
console.log(typeof patch);
```

**评分点**：
- tag 不同时正确替换节点，相同则复用（增量思想）。
- props 增删处理完整，移除不再存在的旧属性。
- children 按索引递归 patch，长度变化能增能减。
- 文本节点与元素节点混合处理，边界防御到位。
