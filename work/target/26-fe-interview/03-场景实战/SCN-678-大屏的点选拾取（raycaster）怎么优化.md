---
title: [SCN-678] 大屏 3D 拾取（raycaster 点选）在万级对象下怎么优化？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-678：3D 拾取怎么优化？
**答**：
- Raycaster 代价：默认遍历所有对象做射线三角面求交，万级对象每次拾取几十 ms——必须空间索引（BVH/八叉树）把求交限制在附近对象。
- 预计算加速：three-mesh-bvh 给 InstancedMesh 建 BVH，拾取从 O(n) 到 O(log n)；静态场景建一次，动态对象单独处理。
- 拾取降级策略：hover 拾取节流（mouse move 时不每帧 raycast，间隔 50ms）；拖拽相机时暂停拾取；移动端触摸直接点击才拾取。
- GPU 拾取：极端规模用「颜色编码拾取」——离屏渲染一遍用 id 颜色，readPixels 查询，O(1) 但有渲染成本，适合超大规模。
- 追问钩子：InstancedMesh 拾取怎么拿到实例 id——raycast 命中带 instanceId 属性，配合 BVH 才能快速定位。

```javascript
import { computeBoundsTree, disposeBoundsTree, acceleratedRaycast } from 'three-mesh-bvh';
THREE.Mesh.prototype.raycast = acceleratedRaycast;
THREE.Mesh.prototype.computeBoundsTree = computeBoundsTree;
mesh.computeBoundsTree();                        // 静态场景建一次

let lastPick = 0;
function onPointerMove(e) {
  const now = performance.now();
  if (now - lastPick < 50) return;               // hover 节流
  lastPick = now;
  const ray = raycasterFrom(e);
  const hit = ray.intersectObject(mesh, false)[0];
  if (hit) showTooltip(hit.instanceId);          // InstancedMesh 实例 id
}
```
