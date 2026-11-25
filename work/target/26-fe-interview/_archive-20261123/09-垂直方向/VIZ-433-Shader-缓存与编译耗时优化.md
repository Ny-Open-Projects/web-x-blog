---
title: [VIZ-433] Shader 缓存与编译耗时优化
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-433：Shader 缓存与编译耗时优化

**答**：
- 编译耗时：复杂 shader 首次编译 50~500ms——预编译常用变体（启动期 idle 阶段）。
- 缓存：WebGL program 无磁盘缓存（浏览器内部有）；WebGPU 有 pipeline caching API（有限）。
- 策略：启动只编译首屏所需，其余 idle 编译；加载屏隐藏编译卡顿。

```javascript
// 预编译调度
function precompileScheduler(programs, deadline = 12) {
  const queue = [...programs];
  function step(deadlineNow) {
    while (queue.length && performance.now() - deadlineNow < deadline) {
      const p = queue.shift();
      p.compile();                       // 触发编译（含一次无绘制 link）
    }
    if (queue.length) requestIdleCallback(step);
  }
  requestIdleCallback(ts => step(ts));
}
// 首屏程序同步编译，其余 idle 预热
```
