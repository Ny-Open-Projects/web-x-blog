---
title: [PER-961] 从输入 URL 到像素上屏：现代浏览器的渲染管线分哪几个阶段
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-961：从输入 URL 到像素上屏：现代浏览器的渲染管线分哪几个阶段

**答**：
- 主流程：导航 → HTML 解析（DOM/CSSOM）→ Style（计算样式）→ Layout（布局树）→ Paint（绘制记录/图层化）→ Composite（合成提交）→ Raster（光栅化）→ Draw（GPU 上屏）。
- 关键认知：Style/Layout 是主线程 CPU 工作，Paint 生成的是 Display Item 列表，真正像素由合成器线程/光栅线程完成。
- 流水线是增量的：滚动只走 Raster/Draw，transform 动画只走 Composite，理解"改了什么决定走多深"是优化根基。
- 追问点：Blink 的 Paint 阶段产出 Paint Op Buffer 供栅格化复用；Chromium 中每个合成器层独立光栅化。

```javascript
// 用 PerformanceObserver 观测管线痕迹
new PerformanceObserver(list => {
  for (const e of list.getEntries())
    console.log(e.name, e.startTime.toFixed(0), e.duration.toFixed(1));
}).observe({ type: 'layout-shift', buffered: true });
// 结合 devtools Performance 面板：紫色 Script / 绿色 Layout / 绿色 Paint
// 优化口诀：动画走 Composite（transform/opacity），
// 布局稳定用 contain，滚动区域用 content-visibility
```
