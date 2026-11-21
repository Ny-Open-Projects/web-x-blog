---
title: [OPT-108] WebGL 资源优化有哪些手段？纹理压缩和 instancing 是什么？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-108：WebGL 资源优化有哪些手段？纹理压缩和 instancing 是什么？

**答**：
- WebGL 的三大资源：几何（顶点）、纹理、draw call；对应优化：**instancing** 合并同类绘制、**纹理压缩格式**降显存与带宽、几何合批/LOD 减顶点数。
- Instancing：一次 draw call 画 N 个实例（ GPU 侧复制），万棵树的绘制从 1 万次 draw call 变 1 次——CPU 提交开销是渲染瓶颈首因。
- 纹理压缩：JPEG/PNG 在 GPU 里仍要解码成 RGBA 占满显存；KTX2/Basis Universal（ASTC/ETC2 硬件格式）显存占用降为 1/4-1/8 且免运行时解码。
- 配套：mipmap 必开（远处采样省带宽且抗闪烁）、纹理尺寸上限按需（2048 封顶）、`powerPreference: 'high-performance'` 与上下文丢失恢复处理。

```javascript
// 一一对应：Three.js 下的纹理压缩与 InstancedMesh 示意
import * as THREE from 'three';
import { KTX2Loader } from 'three/addons/loaders/KTX2Loader.js';

// 1. 纹理压缩：KTX2（Basis Universal，按设备自动转 ASTC/ETC/BC）
const ktx2 = new KTX2Loader()
  .setTranscoderPath('https://cdn.example.com/basis/')
  .detectSupport(renderer);
const tex = await ktx2.loadAsync('terrain.ktx2');
tex.generateMipmaps = true;
tex.minFilter = THREE.LinearMipmapLinearFilter; // mipmap 开启：省带宽 + 抗闪烁
// 对比：4096x4096 RGBA 纹理 64MB 显存；KTX2 ASTC 后约 8MB，且免解码卡顿

// 2. Instancing：一万棵树一次 draw call
const treeGeo = new THREE.ConeGeometry(1, 4, 6);
const treeMat = new THREE.MeshLambertMaterial({ color: 0x2d6a2d });
const instanced = new THREE.InstancedMesh(treeGeo, treeMat, 10_000);
const m = new THREE.Matrix4();
for (let i = 0; i < 10_000; i++) {
  m.setPosition(Math.random() * 500 - 250, 0, Math.random() * 500 - 250);
  instanced.setMatrixAt(i, m); // 每棵树只存一个矩阵，几何共享
}
instanced.instanceMatrix.needsUpdate = true;
scene.add(instanced);
// 收益：draw call 从 10000 -> 1，CPU 提交时间下降 3 个数量级

// 3. 上下文丢失兜底（低端移动端常见）：
renderer.domElement.addEventListener('webglcontextlost', (e) => {
  e.preventDefault(); // 允许恢复
});
renderer.domElement.addEventListener('webglcontextrestored', () => {
  rebuildScene(); // 重建 GPU 资源
});
```
