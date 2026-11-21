---
title: [PER-678] 移动端 JS 主线程卡顿与 Native UI 线程卡顿怎么分别观测？两线程的卡顿归因如何区分？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-678：移动端 JS 主线程卡顿与 Native UI 线程卡顿怎么分别观测？两线程的卡顿归因如何区分？

**答**：
- 两线程卡顿源不同：**JS 线程卡顿**（长任务、同步 XHR、大 JSON parse）表现为点击响应慢；**Native UI 线程卡顿**（重布局/图片解码/阴影绘制）表现为滚动掉帧——观测方法必须分开才能归因。
- JS 线程观测：PerformanceObserver longtask + rAF 帧间隔（同 673）；Native 线程观测：客户端 SDK 提供 FPS 采样（CADisplayLink/Choreographer），前端拿不到，要约定 bridge 上报。
- 归因方法：卡顿时刻双线程数据对齐（JS longtask 与 Native 掉帧同时出现 -> JS 拖累 UI（如同步解码）；只 Native 掉帧 -> UI 层问题（过深层级/过度绘制）；只 JS 卡 -> 逻辑层问题）。
- 协作产物：一张双线程时间线图进排障工具（JS longtask 轨道 + Native FPS 轨道 + 用户操作轨道），值班能直接读出是哪条轨道的锅。

```javascript

const dualThreadDiagnosis = {
  jsThread: 'longtask observer + rAF 帧间隔（前端自采）',
  uiThread: '容器 SDK FPS 上报（bridge 约定）',
  attribution: {
    both: 'JS longtask 与掉帧同时出现 -> JS 拖累 UI（同步解码/大 JSON parse）',
    uiOnly: '仅掉帧 -> UI 层问题（层级过深/过度绘制/大图同步解码）',
    jsOnly: '仅 longtask -> 逻辑层问题（算法/同步请求）',
  },
  timeline: 'JS longtask 轨道 + Native FPS 轨道 + 操作轨道三线对齐成排障时间线',
};
console.log(dualThreadDiagnosis.attribution.both);
```
