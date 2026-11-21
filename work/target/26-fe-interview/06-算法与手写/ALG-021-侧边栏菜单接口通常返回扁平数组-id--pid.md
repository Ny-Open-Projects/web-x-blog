---
title: [ALG-021] 侧边栏菜单接口通常返回扁平数组 `[{id, pid, name}]`，需要转成嵌套树结构渲染。如何一次遍历 O(n) 实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-021：侧边栏菜单接口通常返回扁平数组 `[{id, pid, name}]`，需要转成嵌套树结构渲染。如何一次遍历 O(n) 实现？
**答**：先用一遍循环把每个节点按 id 建立到"新节点（带 children 数组）"的 Map；第二遍按 pid 挂到父节点的 children 上，找不到父节点的作为根。避免递归查找父节点导致的 O(n²)。时间 O(n)，空间 O(n)。

```javascript
function buildTree(items) {
  const map = new Map();
  for (const it of items) map.set(it.id, { ...it, children: [] });
  const roots = [];
  for (const it of items) {
    const node = map.get(it.id);
    if (it.pid == null || !map.has(it.pid)) roots.push(node);
    else map.get(it.pid).children.push(node);
  }
  return roots;
}
```
