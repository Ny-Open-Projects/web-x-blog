---
title: [VIZ-094] 实现图表自适应容器尺寸（ResizeObserver）。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-094：实现图表自适应容器尺寸（ResizeObserver）。
**答**：window.resize 监听不到容器自身变化（侧边栏折叠、tab 切换、父级 flex 变化），正确做法是 `ResizeObserver` 观察图表容器，回调里 chart.resize()。注意三点：① 回调高频触发要 rAF 合帧；② contentRect 宽高为 0（隐藏容器）时跳过，等显示后再 resize；③ Observer 断开要放进组件卸载逻辑防泄漏。ECharts 内部也是这个机制（自动 resize 需开启时同样基于容器尺寸）。

```javascript
// ResizeObserver 优于 window.resize：监听容器真实尺寸变化（侧边栏折叠/布局变化都能感知）
function autoResize(chart, el) {
  let raf = 0;
  const ro = new ResizeObserver(entries => {
    cancelAnimationFrame(raf);                   // 高频触发合并到一帧
    raf = requestAnimationFrame(() => {
      const { width, height } = entries[0].contentRect;
      if (width > 0 && height > 0) chart.resize({ width, height }); // 隐藏容器跳过
    });
  });
  ro.observe(el);
  return () => { ro.disconnect(); cancelAnimationFrame(raf); };   // 卸载时断开防泄漏
}
// tab 切换场景：容器从 display:none 恢复时会触发一次回调，自然完成补 resize
```
