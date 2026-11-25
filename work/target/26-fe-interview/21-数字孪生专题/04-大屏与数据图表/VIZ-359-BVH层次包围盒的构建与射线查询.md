---
title: [VIZ-359] BVH（层次包围盒）的构建与射线查询
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-359：BVH（层次包围盒）的构建与射线查询

**答**：
- BVH：递归二分场景（按最长轴排序取中点/SAH 切分），节点存 AABB 与子节点/图元。
- 查询：射线先与根 AABB 相交（slab 法），相交则递归子节点，命中最近 t 返回——O(log n) 级拾取。
- SAH（表面面积启发式）：切分代价 = 遍历概率 × 图元成本，比中点切分快 20%~50%。

```javascript
// 简化 BVH 构建
function buildBVH(items, depth = 0) {
  if (items.length <= 2) return { leaf: items, box: aabbUnion(items.map(i => i.box)) };
  const box = aabbUnion(items.map(i => i.box));
  const axis = box.max
    .map((v, i) => v - box.min[i])
    .reduce((mi, v, i, arr) => v > arr[mi] ? i : mi, 0);
  const sorted = [...items].sort((a, b) =>
    (a.box.min[axis] + a.box.max[axis]) - (b.box.min[axis] + b.box.max[axis]));
  const mid = sorted.length >> 1;
  return { box, left: buildBVH(sorted.slice(0, mid), depth + 1),
    right: buildBVH(sorted.slice(mid), depth + 1) };
}
function bvhRay(node, ro, rd, hitFn) {
  const hit = rayAABB(ro, rd, node.box.min, node.box.max);   // 344
  if (!hit) return null;
  if (node.leaf) return hitFn(node.leaf);
  return [bvhRay(node.left, ro, rd, hitFn),
          bvhRay(node.right, ro, rd, hitFn)]
    .filter(Boolean).sort((a, b) => a.t - b.t)[0] ?? null;
}
```
