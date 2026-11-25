---
title: [JS-334] ArrayBuffer 与外部内存：TypedArray 的生命周期
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, V8]
type: 面试题
---

## JS-334：ArrayBuffer 与外部内存：TypedArray 的生命周期

**答**：
- 双对象结构：TypedArray（JS 对象，在新生代）+ 其背后的 ArrayBuffer backing store（外部内存，不在 V8 堆快照的 JS 对象里）——大 TypedArray 的 GC 压力小（JS 侧对象小），但 backing store 依赖外部分配器管理
- detach：transfer() 或 postMessage 转移后原 ArrayBuffer detached（byteLength = 0），原视图访问抛 TypeError——转移语义要贯穿代码设计（谁拥有 buffer）
- GC 与释放：ArrayBuffer 无强引用即满足回收条件，但外存释放有延迟（major GC 才清）——高频创建大 buffer（视频帧）会看到「外存涨、堆不涨」，需要显式池化复用
- SharedArrayBuffer：跨线程共享，生命周期由引用计数管理，GC 语义不同——Atomics 操作直接作用 backing store
- 诊断：DevTools 快照看 ArrayBuffer/TypedArray 数量与 byteLength 聚合；Chrome performance.measureMemory 不含外存，用 process.memoryUsage（Node）的 external 维度

```javascript
function framePool(size, n) {
  const pool = Array.from({ length: n }, () => new ArrayBuffer(size));
  return {
    get: () => pool.pop() || new ArrayBuffer(size),
    put: (b) => { if (pool.length < n) pool.push(b); },  // 显式池化, 避免 GC 延迟释放
  };
}
const pool = framePool(1024 * 1024, 8);   // 8 个 1MB 帧缓冲复用
```
