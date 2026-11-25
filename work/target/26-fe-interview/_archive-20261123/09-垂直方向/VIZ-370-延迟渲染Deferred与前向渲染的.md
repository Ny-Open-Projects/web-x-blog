---
title: [VIZ-370] 延迟渲染（Deferred）与前向渲染的取舍
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-370：延迟渲染（Deferred）与前向渲染的取舍

**答**：
- 前向：每片元直接算光照，透明物体友好，多光源贵（每光源全场景成本）。
- 延迟：G-Buffer 存 albedo/法线/深度，光照在屏幕空间统一算——光源数量几乎免费，但透明/MSAA 难。
- Web 端：WebGL2 MRT 支持延迟；移动端 tile-based 架构上 G-Buffer 带宽伤性能——常用前向+（Forward+）混合。

```javascript
// G-Buffer 布局设计
const GBUFFER = [
  { attach: 0, format: 'RGBA8',  content: 'albedo + materialFlag' },
  { attach: 1, format: 'RGBA16F', content: 'normal.xy + roughness/metallic' },
  { attach: 2, format: 'D32',    content: 'depth' },
];
// 带宽估算：1920×1080×(8+8+4)B×2(读写) ≈ 50MB/帧
// 移动端 tile 内存超标 -> 降分辨率或改 Forward+
```
