---
title: [1271] 笔试手写：实现 长任务进度 ETA 预估器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## 1271：笔试手写：实现 长任务进度 ETA 预估器

**需求**：实现 etaEstimator(steps)：steps 为 { id, startedAt, finishedAt|null }[]（毫秒时间戳，按序）。已完成步骤算平均耗时（滑动窗口取最近 5 个已完成）；ETA = 已完成均耗 × 剩余步数 + 当前进行中步骤的已耗时间；全部完成返回 eta: 0。返回 { done, etaMs, avgStepMs }。

```js
function etaEstimator(steps, now = Date.now()) {
  const finished = steps.filter(s => s.finishedAt);
  const running = steps.find(s => !s.finishedAt && s.startedAt);
  const recent = finished.slice(-5); // 滑动窗口
  const avgStepMs = recent.length
    ? recent.reduce((s, x) => s + (x.finishedAt - x.startedAt), 0) / recent.length : 0;
  const done = finished.length;
  const remain = steps.length - done;
  const runningElapsed = running ? now - running.startedAt : 0;
  const etaMs = remain === 0 ? 0 : avgStepMs * (remain - (running ? 1 : 0)) + runningElapsed;
  return { done, etaMs: Math.max(0, Math.round(etaMs)), avgStepMs: Math.round(avgStepMs) };
}
```

**评分点**：
- 滑动窗口均值而非全程均值（适应速度变化）
- 进行中步骤按已耗计、剩余按均值计（ETA 构成拆解）
- remain=0 归零、负值钳制
- 能讨论：ETA 的展示语义（区间而非点值）与抖动抑制
