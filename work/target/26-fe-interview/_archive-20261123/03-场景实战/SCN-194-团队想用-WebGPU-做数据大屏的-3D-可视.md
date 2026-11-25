---
title: [SCN-194] 团队想用 WebGPU 做数据大屏的 3D 可视化，如何评估接入并设计降级链路？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-194：团队想用 WebGPU 做数据大屏的 3D 可视化，如何评估接入并设计降级链路？
**答**：
- 先做能力评估：WebGPU 需要 `navigator.gpu`、用户开启（部分浏览器默认关闭）、硬件支持；目标用户群的支持率决定它只能是"增强"而不是"依赖"。
- 渲染栈选型：直接用 WebGPU API 成本极高，评估现成库（three.js 的 WebGPURenderer、Babylon.js）是否满足需求，自研着色器只做差异化部分。
- 降级链路必须设计进架构：WebGPU → WebGL2 → Canvas2D（静态图兜底），三档能力由同一套场景描述驱动，上层业务无感知。
- 上线配套：能力检测打点（统计真实支持率）、性能对比（WebGPU 并非在所有场景快，小场景初始化反而更慢）、特性开关可一键回 WebGL。

```javascript
// WebGPU 接入：能力检测 + 三档降级链路 + 支持率打点
export async function createRenderer(canvas, scene) {
  const support = await detectGPU();
  report({ type: 'gpu-capability', ...support });       // 上线后统计真实支持率

  if (support.webgpu) {
    try {
      // 现成库优先：three.js WebGPURenderer 自动管理管线
      const { WebGPURenderer } = await import('three/webgpu');
      const renderer = new WebGPURenderer({ canvas, antialias: true });
      await renderer.init();                            // WebGPU 需要显式异步初始化
      return renderScene(renderer, scene);
    } catch (e) {
      report({ type: 'gpu-init-fail', msg: String(e) }); // 设备存在但初始化失败：驱动问题
    }
  }
  if (support.webgl2) {
    // 降级 1：WebGL2 渲染同一场景描述
    const renderer = new THREE.WebGLRenderer({ canvas });
    return renderScene(renderer, scene);
  }
  // 降级 2：Canvas2D 静态兜底（渲染一张预生成的场景图 + 关键数字）
  return renderStaticFallback(canvas, scene);
}

async function detectGPU() {
  const result = { webgpu: false, webgl2: false, adapter: null };
  if (navigator.gpu) {
    try {
      const adapter = await navigator.gpu.requestAdapter();
      result.webgpu = !!adapter;
      if (adapter) result.adapter = adapter.info?.architecture ?? 'unknown';
    } catch { /* 权限或设备问题按不支持处理 */ }
  }
  result.webgl2 = !!document.createElement('canvas').getContext('webgl2');
  return result;
}

// Canvas2D 兜底：大屏至少可看（截图或简化图表），业务指标不丢
function renderStaticFallback(canvas, scene) {
  const ctx = canvas.getContext('2d');
  ctx.fillStyle = '#0b1020'; ctx.fillRect(0, 0, canvas.width, canvas.height);
  scene.kpis.forEach((k, i) => {
    ctx.fillStyle = '#fff';
    ctx.fillText(`${k.label}: ${k.value}`, 40, 60 + i * 40);  // 关键指标文本兜底
  });
  return { dispose() {}, mode: 'canvas2d' };
}
```
