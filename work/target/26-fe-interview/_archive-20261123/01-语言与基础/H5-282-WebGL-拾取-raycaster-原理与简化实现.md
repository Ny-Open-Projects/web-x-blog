---
title: [H5-282] WebGL 拾取：raycaster 原理与简化实现
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-282：WebGL 拾取：raycaster 原理与简化实现

**答**：
- 原理：把屏幕点击点反投影成一条「相机发出的射线」，与场景中的几何体求交，取最近者——three.js 的 Raycaster 做的就是这件事
- 屏幕点→射线：NDC 坐标 (x,y) 构造矩阵 → unproject 得到世界坐标方向向量 → 归一化即射线方向
- 求交成本：逐三角形相交检测，模型面数多时拾取变慢——可用包围盒/包围球粗筛，或用 GPU 拾取（颜色编码离屏渲染）
- GPU 拾取思路：每个对象分配唯一颜色，离屏渲染一帧，读点击像素颜色反查对象——O(1)，适合海量对象
- 坑：canvas 尺寸与 NDC 换算要用 clientWidth（不是 buffer 尺寸）

```javascript
const ndc = new THREE.Vector2(
  (e.clientX / innerWidth) * 2 - 1,
  -(e.clientY / innerHeight) * 2 + 1
);
raycaster.setFromCamera(ndc, camera);
const hits = raycaster.intersectObjects(scene.children, true);
if (hits.length) select(hits[0].object);
```
