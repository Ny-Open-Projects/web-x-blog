---
title: [VIZ-106] glTF 模型加载与优化有哪些手段？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-106：glTF 模型加载与优化有哪些手段？
**答**：glTF 是"3D 界的 JPEG"，加载链：GLTFLoader 解析 JSON → 二进制 buffer → GPU 上传。优化四件套：① **几何压缩**——Draco（有损顶点压缩，体积 -70%）、Meshopt（解码快、按需解码）、KTX2（GPU 直接吃压缩纹理，省显存也省带宽）；② **LOD**——多级细节模型按距离/屏幕占比切换（THREE.LOD）；③ **实例化**——重复模型用 InstancedMesh；④ **加载体验**——decoder 预热、loadingManager 进度、大模型渐进显示。数字孪生/机房场景几乎是必考组合。

```javascript
// glTF + Draco + KTX2 + LOD 全链路
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';
import { KTX2Loader } from 'three/addons/loaders/KTX2Loader.js';
const loader = new GLTFLoader();
const draco = new DRACOLoader().setDecoderPath('/libs/draco/'); // WASM 解码器
loader.setDRACOLoader(draco);
const ktx2 = new KTX2Loader().setTranscoderPath('/libs/basis/').detectSupport(renderer);
loader.setKTX2Loader(ktx2);
loader.load('/model.glb',
  gltf => {
    const lod = new THREE.LOD();
    lod.addLevel(gltf.scene, 0);       // 高模：近距离
    lod.addLevel(buildLowPoly(gltf), 50); // 低模：50 米外自动切换
    scene.add(lod);
  },
  ev => setProgress(ev.loaded / ev.total),  // 进度回调
  err => showFallbackModel()                // 加载失败兜底
);
```
