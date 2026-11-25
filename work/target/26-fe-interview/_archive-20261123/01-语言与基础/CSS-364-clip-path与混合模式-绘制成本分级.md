---
title: [CSS-364] clip-path 与混合模式：绘制成本分级
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-364：clip-path 与混合模式：绘制成本分级

**答**：
- 成本三档：基础形状 clip（polygon/circle，paint 阶段裁剪，便宜）、复杂 path clip（每帧重算路径栅格化）、混合模式（blend 需要「背景层」参与，可能强制提升图层与离屏合成，贵）
- clip-path 动画：形状动画（polygon 点数一致时插值）在 paint 阶段逐帧重绘——小元素可接受，大面积转场改用 View Transitions/transform 遮罩方案
- mask（遮罩）体系：mask-image 渐变淡出（图片底部渐隐标配）——mask 强制离屏合成（先画内容再叠遮罩），长列表滥用会显存暴涨
- mix-blend-mode 依赖上下文：与父级 stacking context 内内容混合——意外的上下文会让混合对象不对（和 isolation 的组合调试）；backdrop-filter（毛玻璃）是重绘大户：背后内容变化每帧重新模糊，移动端谨慎大面积使用
- 降级链：不支持/性能不足时回退纯色/半透明背景——feature 检测 @supports + 低端机档位降级

```css
/* 图片底部渐隐 mask */
.fade-img { mask-image: linear-gradient(black 70%, transparent); }
/* 毛玻璃: 控制面积, 低端机降级 */
.glass {
  backdrop-filter: blur(12px);
  background: rgba(255,255,255,.6);
}
[data-tier='B'] .glass { backdrop-filter: none; background: rgba(255,255,255,.9); }
```
