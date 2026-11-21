---
title: [HW-143] 手写容器响应式图表——ResizeObserver 防抖重绘、初始尺寸与 DPR 适配
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：图表跟随容器（不是窗口）尺寸：ResizeObserver 观察容器（比 window resize 精确——侧栏折叠也触发）；重绘防抖（rAF 合帧 + 高频 resize 合并）；canvas 按 devicePixelRatio 缩放（否则高清屏模糊）；首次回调即初始尺寸（RO 触发时机）。

```javascript
function responsiveChart(canvas, draw) {
  const ctx = canvas.getContext('2d');
  const ro = new ResizeObserver((entries) => {
    for (const e of entries) {
      requestAnimationFrame(() => {                   // rAF 合帧：高频 resize 每帧一次重绘
        const { width, height } = e.contentRect;
        const dpr = window.devicePixelRatio || 1;
        canvas.width = width * dpr;                   // 物理像素 = 逻辑 × DPR（高清屏清晰）
        canvas.height = height * dpr;
        canvas.style.width = width + 'px';            // CSS 尺寸 = 逻辑像素
        canvas.style.height = height + 'px';
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);       // 绘制坐标系回逻辑像素
        draw(ctx, width, height);
      });
    }
  });
  ro.observe(canvas.parentElement);                   // 观察容器（侧栏折叠也触发）
  return () => ro.disconnect();                       // 卸载清理
}
// 对比 window resize：容器 RO 精确（布局变化都触发），且与容器布局耦合
// DPR 适配三步：物理尺寸 ×dpr / CSS 尺寸逻辑 / ctx.setTransform(dpr,...) —— 漏一步就模糊
```

**评分点**：
- ResizeObserver 观察容器（非 window）——精确性的来源。
- DPR 三步适配完整（物理尺寸/CSS 尺寸/setTransform）——漏一步高清屏模糊。
- rAF 合帧防高频重绘；disconnect 清理。
- 首次回调即初始尺寸（无需手动初始化）。
