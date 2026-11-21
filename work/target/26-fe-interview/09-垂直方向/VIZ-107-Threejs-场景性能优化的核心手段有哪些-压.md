---
title: [VIZ-107] Three.js 场景性能优化的核心手段有哪些？（压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-107：Three.js 场景性能优化的核心手段有哪些？（压轴）
**答**：先量化再优化：stats 看帧率、Spector 看每帧 draw call。手段按收益排序：① **降 draw call**——静态物体 `mergeGeometries` 合并、重复物体 InstancedMesh、保持 frustum culling；② **材质共享**——相同外观复用同一 Material 实例，避免着色器首次编译掉帧（可预热编译）；③ **纹理治理**——KTX2 压缩、尺寸取 2 的幂、及时 dispose；④ **渲染侧**——pixelRatio clamp 到 2、按需渲染（无交互不跑 render）、阴影贴图按需更新；⑤ **更新侧**——静态物体 `matrixAutoUpdate = false`。

```javascript
// draw call 优化三板斧：合并 + 实例化 + 材质共享
import * as BufferGeometryUtils from 'three/addons/utils/BufferGeometryUtils.js';
// 1. 静态物体合并：1000 个箱子 1000 次 draw call -> 1 次
const merged = BufferGeometryUtils.mergeGeometries(boxGeometries);
scene.add(new THREE.Mesh(merged, sharedMaterial));
// 2. 重复物体实例化：一片森林只有 1 次 draw call
const forest = new THREE.InstancedMesh(treeGeo, treeMat, 10000);
const m = new THREE.Matrix4();
trees.forEach((t, i) => {
  m.compose(t.position, t.quaternion, t.scale);
  forest.setMatrixAt(i, m);           // 实例矩阵一次上传
});
forest.instanceMatrix.needsUpdate = true;
scene.add(forest);
// 3. 材质共享 + 按需渲染
const sharedMaterial = new THREE.MeshStandardMaterial({ map: atlasTex });
controls.addEventListener('change', () => { needsRender = true; }); // 交互时才渲染
```

---

## 十二、WebGPU 与新图形 API（VIZ-108 ~ VIZ-111）
