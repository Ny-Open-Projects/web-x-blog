---
title: [H5-151] 什么时候上 WebGL/WebGPU？与 Canvas 2D 的边界如何判断？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-151：什么时候上 WebGL/WebGPU？与 Canvas 2D 的边界如何判断？
**答**：
- Canvas 2D：元素数千以内、无需着色器、迭代速度优先——API 简单、调试直观，是默认选项。
- WebGL：元素数万级（批渲染一次画完）、需要滤镜/混合/粒子/3D；用 PixiJS/Three.js 封装后成本可控。
- WebGPU：compute shader、更大吞吐、更现代的 API 设计；生态尚在成长，新项目可评估。
- 决策依据是 profile 结果：瓶颈在"JS 逻辑/布局"先优化数据结构与脏区域；瓶颈在"绘制指令重放/状态切换"WebGL 批渲染收益巨大；瓶颈在"纹理上传/像素读回"先减少 getImageData/toDataURL。

```javascript
// 选型判断树（答题口径）
function pickRenderer(scene) {
  const n = scene.count;
  const needsShader = scene.effects.some((e) =>
    ['blur', 'glow', 'particles', '3d'].includes(e));
  if (n < 2000 && !needsShader) return 'Canvas 2D';            // 默认选项
  if (n < 200000) return 'WebGL（用 PixiJS 或 Three.js 封装）';  // 批渲染/着色器
  return 'WebGPU（compute 大吞吐）或服务端渲染';
}

// 先 profile 判断瓶颈在哪，再决定是否升级图形栈
async function profile(canvas) {
  const t0 = performance.now();
  for (let i = 0; i < 60; i++) renderFrame(canvas);            // 跑 60 帧
  const perFrame = (performance.now() - t0) / 60;
  console.log('ms/frame =', perFrame.toFixed(2));
  // perFrame > 16.7 才需要优化：
  //   瓶颈是 JS 逻辑/布局       → 先优化数据结构与脏区域，别急着上 WebGL
  //   瓶颈是绘制指令重放状态多  → WebGL 批渲染收益巨大
  //   瓶颈是纹理上传/像素读回   → 减少 getImageData / toDataURL 频率
}

// 中间路线：整体保留 Canvas 2D，把热点区域（万级粒子/滤镜）拆成
// WebGL 层叠加（分层 canvas），避免整站迁移；
// WebGPU 生态（Three.js WebGPURenderer 等）在成熟中，新项目可评估
```

## 追问（补充）

**追问**：

1. 什么情况下 Canvas 2D 反而比 WebGL 快？ → 元素少、以文本和矢量为主、频繁 `getImageData` 读回像素，或设备 GPU 弱/被驱动黑名单时；WebGL 的上下文创建和纹理上传开销反而更大。
2. 分层 canvas（2D 底 + WebGL 叠）要注意什么？ → 两层宽高必须按同一 devicePixelRatio 设置，靠 DOM 顺序决定合成层级；WebGL 层要开 alpha 并用透明清屏，否则会把底层盖住。
3. 怎么确认瓶颈在绘制而不是 GC？ → Rendering 面板看栅格化/合成耗时是否占满帧；Memory 面板若出现周期性锯齿说明是 GC，此时应先减少对象分配而不是换图形栈。
