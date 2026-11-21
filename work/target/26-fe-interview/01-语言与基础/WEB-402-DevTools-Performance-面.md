---
title: [WEB-402] DevTools Performance 面板的火焰图怎么看？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 笔试题
---

## WEB-402：DevTools Performance 面板的火焰图怎么看？
**答**：
- 先看概览轨道：FPS/网络/主线程，找到掉帧区间；再看 Main 轨道火焰图：横向是时间，纵向是调用栈，宽块=耗时函数。
- 识别模式：连续紫色（Layout/Recalculate Style）→ 强制同步布局；绿色脚本大块 → JS 耗时；Scheduling 区灰色 → 长任务被拆/排队。
- 分析套路：Bottom-Up 视图找 self time 最大的函数、勾掉 Noise（idle/gc）、用 Timings 面板看 User Timing 标记（performance.mark）。

```javascript
// 配合 User Timing 打标
performance.mark('render-start');
renderList();
performance.mark('render-end');
performance.measure('render', 'render-start', 'render-end');
console.table(performance.getEntriesByType('measure'));
// Bottom-Up 找 self time → 定位真正的热点函数
```

**评分点**：
- 结论先行，排查/实现路径清晰
- 覆盖典型异常与边界
- 代码可运行、体现方法论
- 主动给出工程取舍
