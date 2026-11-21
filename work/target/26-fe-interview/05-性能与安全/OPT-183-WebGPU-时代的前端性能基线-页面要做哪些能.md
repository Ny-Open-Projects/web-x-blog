---
title: [OPT-183] WebGPU 时代的前端性能基线，页面要做哪些能力探测与分级？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-183：WebGPU 时代的前端性能基线，页面要做哪些能力探测与分级？

**答**：
- WebGPU 允许页面用类原生的方式用 GPU（计算+渲染），对可视化/图像处理/AI 推理场景性能数量级提升；但设备能力差异极大，必须**探测分级**而不是假设可用。
- 探测内容：`navigator.gpu` 存在性、`requestAdapter()` 返回的 adapter 信息（厂商/架构/特性 features/limits）、理想帧时间（跑一次 micro-benchmark 定档）。
- 分级策略：无 WebGPU → WebGL2 → Canvas2D 降级链；按 `adapter.limits`（maxTextureDimension、maxComputeWorkgroupSize）选择渲染分辨率与粒子规模。
- 性能基线概念：高端 GPU 也要防止过度绘制（分辨率 × 帧率的乘积约束），用 `requestAnimationFrame` 的时间预算动态调 LOD（Level of Detail）。

```javascript
// 一一对应：WebGPU 能力探测 + 渲染档位分级 + 降级链
export async function initGraphicsTier(canvas) {
  if (navigator.gpu) {
    const adapter = await navigator.gpu.requestAdapter({ powerPreference: 'high-performance' });
    if (adapter) {
      const device = await adapter.requestDevice();
      const { limits, features } = adapter;
      // 按能力定档：分辨率上限受 maxTextureDimension 约束
      const tier = features.has('timestamp-query') && limits.maxComputeWorkgroupSizeX >= 64
        ? 'ultra' : 'high';
      return {
        engine: 'webgpu', tier,
        maxRes: Math.min(limits.maxTextureDimension2D, 4096),
        device,
      };
    }
  }
  // 降级链：WebGPU 不可用退 WebGL2，再退 Canvas2D
  const gl = canvas.getContext('webgl2');
  if (gl) {
    const dbg = gl.getExtension('WEBGL_debug_renderer_info');
    const renderer = dbg ? gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : '';
    const tier = /Apple M[2-9]|RTX|Radeon Pro/i.test(renderer) ? 'high' : 'mid';
    return { engine: 'webgl2', tier, maxRes: 2048 };
  }
  return { engine: 'canvas2d', tier: 'low', maxRes: 1024 };  // 最弱档：减分辨率减粒子
}

// 自适应 LOD：用帧时间动态降载，任何 GPU 都保持交互流畅
function adaptiveLOD(render) {
  let last = performance.now(), budget = 16.7, particles = 100_000;
  function loop(now) {
    const dt = now - last; last = now;
    if (dt > budget * 1.5 && particles > 10_000) particles = Math.floor(particles * 0.7); // 超预算降规模
    else if (dt < budget * 0.6 && particles < 500_000) particles = Math.floor(particles * 1.2); // 有余量升规模
    render(particles);
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
}
```

## 二十八、体系与推进
