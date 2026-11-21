---
title: [CSS-092] mask 如何实现列表渐隐与刮刮卡效果？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-092：mask 如何实现列表渐隐与刮刮卡效果？

**答**：
- mask 用图像（含渐变）的 alpha 通道控制元素可见度，黑透白显（默认 luminance/alpha 视类型）。
- 渐隐列表：上下边缘用 `linear-gradient` 的 mask 淡出，比裁切+遮挡元素干净得多。
- 刮刮卡：上层 canvas 被涂抹后其透明区域"擦除"，下层内容透出——mask 每帧跟随 canvas 合成。
- mask 支持多层叠加与 `-webkit-mask` 前缀，长列表渐隐注意 mask 不参与重排、成本可控。

```css
/* 1. 列表两端渐隐 */
.fade-list {
  overflow-y: auto;
  mask-image: linear-gradient(transparent, #000 8%, #000 92%, transparent);
}

/* 2. 单行超长文本渐隐省略（替代省略号） */
.fade-text {
  white-space: nowrap; overflow: hidden;
  mask-image: linear-gradient(90deg, #000 85%, transparent);
}

/* 3. 刮刮卡：canvas 涂抹擦除覆盖层 */
.scratch-wrap { position: relative; }
.scratch-prize { position: absolute; inset: 0; }
.scratch-canvas { position: absolute; inset: 0; touch-action: none; }
/* JS 在 canvas 上以 destination-out 画圆即"刮开"，canvas 自身即 mask */
```
