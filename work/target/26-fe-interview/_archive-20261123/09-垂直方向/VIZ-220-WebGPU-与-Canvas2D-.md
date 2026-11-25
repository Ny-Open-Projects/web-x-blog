---
title: [VIZ-220] WebGPU 与 Canvas2D 混合渲染：静态底图 + GPU 动态层
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-220：WebGPU 与 Canvas2D 混合渲染：静态底图 + GPU 动态层

**答**：
- 务实混合：坐标轴/网格等静态内容用 Canvas2D（文本渲染省心），动态数据层用 WebGPU（性能），两层叠加。
- 合成：CSS 叠加两个 canvas（GPU 层 pointer-events 穿透）或 GPU 层采样 Canvas2D 纹理。
- 适用：图表库渐进升级路径——不动静态层，先把数据层 GPU 化。

```javascript
// CSS 叠层方案（最简）
const container = document.createElement('div');
const c2d = document.createElement('canvas');             // 静态层：轴/网格/图例
const gpu = document.createElement('canvas');             // 动态层：WebGPU 数据
gpu.style.pointerEvents = 'none';                         // GPU 层穿透交互
container.append(c2d, gpu);
// 纹理采样方案：Canvas2D 内容作为纹理供 WebGPU 合成（单 canvas 输出）
// device.queue.copyExternalImageToTexture({ source: c2d }, { texture }, size)
// 选型：需要统一导出（截图/录屏）→ 纹理采样方案；分层独立 → CSS 叠层
```
