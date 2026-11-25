---
title: [CSS-344] 栅格化与图层：GPU 纹理的生命周期
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-344：栅格化与图层：GPU 纹理的生命周期

**答**：
- 图层生命周期：提层（will-change/3d）→ 绘制记录 → 栅格化（raster 线程把绘制记录变位图，按 tile 分块）→ GPU 纹理上传 → 合成——每层纹理占显存 = 尺寸 × dpr² × 4 字节
- 内存代价量化：一个 375×2000 的长图层在 dpr 3 下 ≈ 375×3×2000×3×4 ≈ 27MB——「随手 will-change」的显存账要会算；大层会被 tile 化按需栅格化缓解
- 栅格化优先级：视口附近 tile 先栅格（checkerboard 空白就是没赶上）；快速滚动时非可视 tile 延迟栅格——大背景层快速滚动发白就是这机制
- 释放时机：will-change 移除/元素不可见/内存压力下纹理回收——长驻 will-change 是显存泄漏源；动画结束移除是规范动作
- 诊断：DevTools Layers 面板看每层尺寸与内存、Rendering 面板 Paint flashing（重绘区）/ Layer borders（tile 边界与 checkerboard）

```css
/* 反例: 长页面 200 个元素全提层 → 数百MB显存 */
li { will-change: transform; }
/* 正解: 动画进入前提层, 结束释放 */
li.animating { will-change: transform; }
/* 长列表用 content-visibility 替代盲目提层 */
li { content-visibility: auto; }
```
