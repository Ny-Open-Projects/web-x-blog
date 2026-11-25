---
title: [FRP-011] 请手写 patch 的核心流程（同层比较 + children 三种情况）。
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-011：请手写 patch 的核心流程（同层比较 + children 三种情况）。

**答**：
- diff 的前提是**同层比较**：只对比同一层级的 vnode，不跨层移动（复杂度从 O(n^3) 降到 O(n)），跨层移动节点会被"销毁重建"。
- 判断是否同一节点：`type` 和 `key` 都相同（isSameVNodeType）；相同走 patchProps 更新，不同直接卸载旧的、挂载新的。
- children 三种情况：新旧都是文本 → 替换文本；新是数组旧是文本/反之 → 全量替换；**新旧都是数组 → 进入 diff 子节点**（下一题）。
- 组件的 patch 则递归到组件的 render 结果继续对比。

```javascript
// 简化实现，帮助理解 patch 核心流程
function isSameVNodeType(n1, n2) {
  return n1.type === n2.type && n1.key === n2.key;
}

function patch(n1, n2, container) {
  // n1 旧 vnode，n2 新 vnode；n1 为空表示首次挂载
  if (n1 && !isSameVNodeType(n1, n2)) {
    unmount(n1);          // type/key 不同：卸载旧的，重建新的（不跨层复用）
    n1 = null;
  }
  if (!n1) {
    mount(n2, container); // 首次挂载
    return;
  }

  const el = (n2.el = n1.el); // 复用真实 DOM

  // 情况一：双方都是文本子节点
  if (typeof n2.children === 'string') {
    if (n1.children !== n2.children) el.textContent = n2.children;
  }
  // 情况二：新数组旧文本 / 新文本旧数组 —— 全量替换
  else if (Array.isArray(n2.children) && typeof n1.children === 'string') {
    el.textContent = '';
    n2.children.forEach((c) => mount(c, el));
  }
  // 情况三：双方都是数组 —— diff 子节点列表（见 FRP-012 的 keyed diff）
  else if (Array.isArray(n2.children) && Array.isArray(n1.children)) {
    diffChildren(n1.children, n2.children, el);
  }

  // 更新 props：旧的没有新的有 = 添加；反之 = 移除；都有且不同 = 更新
  const oldProps = n1.props || {}, newProps = n2.props || {};
  for (const key in newProps) {
    if (oldProps[key] !== newProps[key]) el.setAttribute(key, newProps[key]);
  }
  for (const key in oldProps) {
    if (!(key in newProps)) el.removeAttribute(key);
  }
}
// mount / unmount / diffChildren 在后续题目中给出
```
