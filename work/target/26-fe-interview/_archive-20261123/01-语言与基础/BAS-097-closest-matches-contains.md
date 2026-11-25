---
title: [BAS-097] closest、matches、contains 分别做什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-097：closest、matches、contains 分别做什么？
**答**：
- closest(selector)：从自身沿祖先向上找最近匹配（含自身），事件委托里定位真实触发源的首选。
- matches(selector)：判断当前元素是否命中选择器，返回布尔值。
- contains(node)：判断某节点是否是当前节点的后代（或自身），"点击外部关闭弹窗"就用它取反。

```javascript
list.addEventListener('click', (e) => {
  const item = e.target.closest('li.item');  // 向上定位目标项
  if (!item) return;                          // 点在容器空白处
  if (item.matches('.item.active')) item.classList.remove('active');
});
document.addEventListener('click', (e) => {
  if (!popover.contains(e.target)) popover.hide(); // 点在弹窗外部才关闭
});
```
