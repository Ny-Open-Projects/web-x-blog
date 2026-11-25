---
title: [VIZ-202] WebGPU 渲染管线进阶：多 Pass 与 RenderBundle
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-202：WebGPU 渲染管线进阶：多 Pass 与 RenderBundle

**答**：
- 多 Pass：先渲染到离屏纹理（G-Buffer/后处理输入），再合成——WebGPU 的 pass 显式声明颜色附件。
- RenderBundle：把不变的绘制命令录制复用（静态场景批量绘制），减少每帧 JS 编码开销。
- 收益场景：静态图表底图（网格/坐标轴）录一次，动态数据层每帧重编。

```javascript
// RenderBundle 复用静态绘制命令
const bundle = device.createRenderBundleEncoder({
  colorFormats: ['bgra8unorm'],
});
// ... bundle.setPipeline / setBindGroup / draw(gridVertices)
const staticBundle = bundle.finish();                    // 录制一次
function frame() {
  const pass = encoder.beginRenderPass({ colorAttachments: [{ view, loadOp: 'clear' }] });
  pass.executeBundles([staticBundle]);                   // 静态层：零重编码
  // 动态数据层：每帧正常编码
  pass.end();
}
// 收益：10 万网格线静态部分编码从 ~8ms → ~0.2ms
```
