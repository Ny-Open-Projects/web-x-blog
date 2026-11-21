---
title: [PER-029] Chrome Performance 面板排查页面卡顿的流程是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-029：Chrome Performance 面板排查页面卡顿的流程是什么？

**答**：
- 流程：开启 Performance 录制 -> 复现卡顿操作 -> 停止录制 -> 看 Frames 与主线程火焰图 -> 定位耗时长帧中黄色 Script 区间的函数。
- 典型特征：强制同步布局表现为蓝色 Recalculate Style 与紫色 Layout 密集交替，并带 Layout Thrashing 警告。
- 底部 Bottom-Up 视图按自耗时排序找热点函数，Call Tree 视图看调用链。
- 找到嫌疑函数后先写微基准验证，再针对性优化（缓存读取、切片、移入 Worker）。

```javascript
// 卡顿典型：循环内读写交替造成强制同步布局
// Performance 面板里表现为密集的紫色 Layout 块，提示 Layout Thrashing
const cards = document.querySelectorAll('.card');

// 反例：每次写后立刻读，布局队列反复失效
cards.forEach((card) => {
  card.style.width = `${card.offsetWidth + 10}px`;
});

// 正例：一次集中读，一次集中写
const widths = Array.from(cards, (card) => card.offsetWidth + 10);
cards.forEach((card, i) => {
  card.style.width = `${widths[i]}px`;
});
```
