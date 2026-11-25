---
title: [H5-292] WebGL 加载大模型：过程与压缩格式（draco/ktx）
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebGL]
type: 面试题
---

## H5-292：WebGL 加载大模型：过程与压缩格式（draco/ktx）

**答**：
- 模型加载流程：fetch 二进制 → 解析格式（glTF 为主流）→ 几何体/材质构建 → 上传 GPU；瓶颈在下载体积与解析耗时
- 几何压缩：Draco 压缩顶点数据（体积降 5~10 倍），代价是解压耗时（可放 Worker）
- 纹理压缩：KTX2/Basis 压缩纹理，直接上传 GPU 显存格式（不经过 CPU 解码 RGBA），显存占用降 4~8 倍
- 分级加载：先低模+占位色快速可见，再替换高模（LOD）；渐进式加载对大场景必备
- 检测指标：模型首屏时间与显存占用，用 performance.measure 包住 load 与 parse 两段

```javascript
import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';
const loader = new GLTFLoader();
const draco = new DRACOLoader();
draco.setDecoderPath('/draco/');       // wasm 解码器
loader.setDRACOLoader(draco);
loader.load('/model.glb', (gltf) => scene.add(gltf.scene), (e) => setProgress(e.loaded / e.total));
```
