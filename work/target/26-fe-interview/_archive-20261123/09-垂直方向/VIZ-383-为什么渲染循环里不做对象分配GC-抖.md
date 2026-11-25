---
title: [VIZ-383] 为什么渲染循环里不做对象分配（GC 抖动）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-383：为什么渲染循环里不做对象分配（GC 抖动）

**答**：
- 每帧 new 数组/对象会触发 GC 停顿（js 堆 50~200ms 级）——表现为周期性掉帧。
- 对策：预分配 Float32Array/对象池、复用临时变量（scratch 对象）、避免 map/filter 产生中间数组。
- 检测：Performance 面板 GC 事件 + 内存曲线锯齿；rAF 内分配计数工具。

```javascript
// 无分配渲染循环
const scratch = { pos: new Float32Array(3), mat: new Float32Array(16) };
function frame(t) {
  // 反模式：const tmp = particles.map(p => p.pos.clone())
  for (let i = 0; i < N; i++) {
    // 直接写入预分配 buffer
    scratch.pos[0] = px[i] + vx[i] * dt;
    // ...
  }
  gl.bufferSubData(gl.ARRAY_BUFFER, 0, buffer);   // 复用同一 buffer
  requestAnimationFrame(frame);
}
```
