---
title: [CSS-186] 合成层（Compositing Layers）怎么调试“层爆炸”？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-186：合成层（Compositing Layers）怎么调试“层爆炸”？

**答**：
- 层爆炸：transform/filter/will-change 等把大量元素提升为合成层，每层占独立显存（尺寸 × 4 字节），滚动卡顿、内存暴涨。
- 调试入口：Layers 面板看层数量、尺寸、内存占比与提升原因；Rendering 面板开 paint flashing 看重绘区域。
- 原则：只有确实要跑合成器动画（transform/opacity）的元素才值得单独成层；静态元素上 `will-change` 是纯浪费。
- 修复：列表项动画结束移除 will-change（或只在 `.animating` 态声明）、限制提升范围到动画元素本身、超大图降尺寸。

```css
/* 反面教材：1000 个列表项全部常驻合成层 */
.list-item {
  will-change: transform;   /* 滥用：层爆炸元凶 */
}

/* 正确：动画进行中才提升，结束回落 */
.list-item.animating {
  will-change: transform;   /* JS 加类前提升，动画结束移除类 */
}
/* 或者：不给提示，直接让合成器动画自动触发提升 */
.list-item {
  transition: transform .3s;
}
.list-item:hover { transform: translateY(-2px); }

/* 排查对照表（Layers 面板观察）：
   transform: translateZ(0)      → 强制提升
   position: fixed               → 可能提升
   filter / backdrop-filter      → 提升
   3D transform / will-change    → 提升
   单层内存 = 宽 × 高 × 4 字节，超大背景图单独成层最危险 */
```
