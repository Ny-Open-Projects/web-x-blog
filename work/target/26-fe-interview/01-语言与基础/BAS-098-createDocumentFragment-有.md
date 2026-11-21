---
title: [BAS-098] createDocumentFragment 有什么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-098：createDocumentFragment 有什么用？
**答**：
- 轻量内存节点容器：先把子节点批量挂到 fragment，再一次 appendChild 进文档，只触发一次回流。
- 循环直接 append 到真实 DOM 会反复触发布局计算，大数据量插入时性能差距明显。
- fragment 插入后自身不会进入 DOM，子节点被"搬运"进去。

```javascript
const frag = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  const li = document.createElement('li');
  li.textContent = `item ${i}`;
  frag.appendChild(li);      // 先攒在内存 fragment 里
}
document.querySelector('ul').appendChild(frag);  // 一次性插入
```
