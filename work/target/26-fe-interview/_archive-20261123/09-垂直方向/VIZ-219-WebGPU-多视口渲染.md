---
title: [VIZ-219] WebGPU 多视口渲染：大屏多图表单 canvas
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-219：WebGPU 多视口渲染：大屏多图表单 canvas

**答**：
- 大屏多图表（20 个）共用一个 WebGPU canvas：每图表一个 viewport（pass.setViewport/scissor）+ 各自变换 uniform——一次 pass 渲染全部，省掉多 canvas 合成。
- 交互命中：点击先映射到所属图表区域（viewport 矩形判断）再转局部坐标。
- 收益：合成层减少、内存（多 canvas 纹理）下降。

```javascript
function renderDashboards(device, charts) {
  const pass = encoder.beginRenderPass({ colorAttachments: [{ view, loadOp: 'clear' }] });
  for (const chart of charts) {
    pass.setViewport(chart.x, chart.y, chart.w, chart.h);   // 视口
    pass.setScissorRect(chart.x, chart.y, chart.w, chart.h);   // 裁剪
    pass.setBindGroup(0, bindGroupWith(chart.uniforms));    // 各自变换
    pass.draw(chart.vertexCount);
  }
  pass.end();
}
// 命中：click(e) → 找 viewport 包含点的 chart → 局部坐标 = (e - chart.x) / chart.scale
// 注意：WebGPU 无独立 setViewport per draw——需按 chart 分 draw 段或多次 pass
```
