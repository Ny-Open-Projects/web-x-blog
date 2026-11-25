---
title: [VIZ-103] Bloom 辉光与高斯模糊等后处理效果的实现原理是什么？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-103：Bloom 辉光与高斯模糊等后处理效果的实现原理是什么？
**答**：后处理 = 把场景先渲染到**帧缓冲纹理（FBO）**，再对纹理做全屏 quad 的多 pass 处理。Bloom 标准流程：① 亮度提取 pass（超阈值的像素留下）；② 对亮区降采样后做多级高斯模糊（横一遍 + 竖一遍的分离卷积，复杂度从 O(n²) 降 O(n)）；③ 上采样加法混合回原场景。工程上直接用 Three.js 的 EffectComposer + UnrealBloomPass，但要知道 threshold/strength/radius 三个参数对应哪一步才能调出效果。

```javascript
// Three.js 后处理链：场景渲染 -> 亮度提取 -> 高斯模糊 -> 叠加
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
const composer = new EffectComposer(renderer);   // 内部维护多张 render target
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(
  new THREE.Vector2(innerWidth, innerHeight),
  0.9,   // strength：辉光强度
  0.4,   // radius：模糊扩散半径
  0.85   // threshold：亮度阈值，低于此值不发光
);
composer.addPass(bloom);
function animate() {
  composer.render();          // 依次执行各 pass，最终输出到屏幕
  requestAnimationFrame(animate);
}
```
