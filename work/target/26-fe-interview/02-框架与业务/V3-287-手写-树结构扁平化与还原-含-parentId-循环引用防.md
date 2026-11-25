---
title: [V3-287] 手写：树结构扁平化与还原（parentId 互转，含异常数据防御）
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-287：手写：树结构扁平化与还原（parentId 互转，含异常数据防御）
**答**：实现两个互逆函数：`flatten(tree)` 树转扁平列表（保留 parentId，深度优先保序）；`unflatten(list)` 扁平列表转树。要求防御：parentId 指向不存在节点、孤儿节点（父在列表尾部/缺失）、循环引用（A 的父是 B，B 的父是 A）、重复 id。
**评分点**：
- O(n) 实现（Map 索引，不嵌套循环）
- 孤儿/缺失父节点的兜底策略（提升为根并收集警告）
- 循环引用检测（未达根的节点判环）
- 深度优先保序与根排序稳定性

```javascript
function flatten(tree, parentId = null, out = [], warn = []) {
  for (const node of tree ?? []) {
    if (out.some((n) => n.id === node.id)) { warn.push(`重复 id: ${node.id}`); continue; }
    const { children, ...rest } = node;
    out.push({ ...rest, parentId });
    flatten(children, node.id, out, warn);
  }
  return { list: out, warn };
}
function unflatten(list) {
  const nodes = new Map(), roots = [], orphan = [];
  for (const item of list) {
    if (nodes.has(item.id)) { console.warn(`重复 id: ${item.id}`); continue; }
    nodes.set(item.id, { ...item, children: [] });
  }
  for (const item of list) {
    if (item.parentId == null || !nodes.has(item.parentId)) {
      if (item.parentId != null) orphan.push(item.id); // 缺失父 → 兜底为根
      roots.push(nodes.get(item.id));
    } else {
      const parent = nodes.get(item.parentId);
      parent.children.push(nodes.get(item.id));        // 尾部父也能先建索引再挂子
    }
  }
  // 循环引用检测：从每个"孤儿"沿 parent 链走，回到自身即环
  const visited = new Set();
  for (const id of orphan) {
    let cur = nodes.get(id), path = new Set();
    while (cur && cur.parentId != null && nodes.has(cur.parentId)) {
      if (path.has(cur.id)) { console.warn(`循环引用: ${id}`); break; }
      path.add(cur.id); cur = nodes.get(cur.parentId);
    }
    visited.add(id);
  }
  return { tree: roots, warn: orphan.length ? `孤儿节点 ${orphan.length} 个` : [] };
}
```
