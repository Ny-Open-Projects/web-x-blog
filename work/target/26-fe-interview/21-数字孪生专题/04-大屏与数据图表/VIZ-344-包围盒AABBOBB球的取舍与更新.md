---
title: [VIZ-344] 包围盒（AABB/OBB/球）的取舍与更新
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-344：包围盒（AABB/OBB/球）的取舍与更新

**答**：
- AABB 计算最快、剔除便宜，但旋转物体需要重算（体积膨胀）；OBB 贴合但相交测试贵 3~5 倍；球对旋转不变，最廉价但稀疏物体包裹差。
- 更新策略：静止物体预计算；动画物体每帧从顶点重算太贵——用层级 AABB（父级包裹子级并集）+ 脏标记。
- 射线相交：AABB 用 slab 法（3 对平面的进出 t 区间求交），球用二次方程判别式。

```javascript
// AABB slab 射线相交
function rayAABB(ro, rd, min, max) {
  let tmin = -Infinity, tmax = Infinity;
  for (let i = 0; i < 3; i++) {
    const inv = 1 / (rd[i] || 1e-9);
    let t1 = (min[i] - ro[i]) * inv, t2 = (max[i] - ro[i]) * inv;
    if (t1 > t2) [t1, t2] = [t2, t1];
    tmin = Math.max(tmin, t1); tmax = Math.min(tmax, t2);
    if (tmin > tmax) return null;            // 无交
  }
  return { t: tmin >= 0 ? tmin : tmax };
}
function aabbUnion(boxes) {
  return boxes.reduce((u, b) => ({
    min: u.min.map((v, i) => Math.min(v, b.min[i])),
    max: u.max.map((v, i) => Math.max(v, b.max[i])) }));
}
```
