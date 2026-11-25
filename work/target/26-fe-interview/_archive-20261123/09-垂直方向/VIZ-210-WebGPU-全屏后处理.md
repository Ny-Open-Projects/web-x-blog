---
title: [VIZ-210] WebGPU 全屏后处理：Bloom 与抗锯齿管线
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-210：WebGPU 全屏后处理：Bloom 与抗锯齿管线

**答**：
- 后处理链：场景渲染到离屏 → 提亮阈值 pass → 高斯模糊 pass（双 pass 横纵）→ 合成 pass。
- 抗锯齿：MSAA（WebGPU 原生 sampleCount=4，零代码改动）vs FXAA（后处理 pass）——MSAA 优先（硬件级无成本）。
- pass 组合成本：每 pass 全屏 fillrate；后处理 pass 数控制在 4 以内。

```javascript
function bloomPipeline(device, sceneTexture) {
  // 1. 提亮：threshold pass（亮度 > 阈值保留）
  // 2. 高斯模糊：水平 pass → 垂直 pass（ ping-pong 纹理对）
  // 3. 合成：scene + bloom 加权叠加
  const pass = encoder.beginRenderPass({ colorAttachments: [{
    view: sceneTexture.createView(),
    loadOp: 'load', storeOp: 'store',                   // load 保场景内容
  }] });
  pass.setPipeline(compositePipeline);
  pass.draw(3);                                          // 全屏三角形
  pass.end();
}
// MSAA：createTexture({ sampleCount: 4 }) + pass 的 multisampledTextureCount——一行级改动
```
