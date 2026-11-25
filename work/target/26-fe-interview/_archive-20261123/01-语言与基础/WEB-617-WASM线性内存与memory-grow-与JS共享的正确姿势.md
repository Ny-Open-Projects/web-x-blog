---
title: [WEB-617] WASM 线性内存与 memory.grow：与 JS 共享的正确姿势
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-617：WASM 线性内存与 memory.grow：与 JS 共享的正确姿势

**答**：
- 线性内存是一段连续 ArrayBuffer（Memory.buffer），JS 侧用 TypedArray 视图读写，这是 JS↔WASM 大数据共享的通道
- memory.grow 扩容后关键坑：`memory.buffer` 会失效——grow 会 detach 旧 ArrayBuffer，JS 侧缓存过的 TypedArray 视图全部变成「死视图」，必须重新创建
- 正确模式：每次 grow 后重新 `new Uint8Array(memory.buffer)`，或封装 accessor 函数而不是缓存视图；Emscripten 的 HEAPU8 等辅助对象内部已处理
- 容量规划：grow 有上限（memory.max），超出抛 RangeError；大文件处理要预估峰值并预留，避免频繁 grow 抖动
- 共享内存（threads）：SAB 版线性内存可多线程读写，JS 与 wasm worker 并发访问时要自己保证同步（Atomics + mutex），这是复杂度陡增点

```javascript
const exports = instance.exports;
let view = new Uint8Array(exports.memory.buffer);

function ensureCapacity(bytes) {
  const pages = Math.ceil(bytes / 65536);
  if (exports.memory.buffer.byteLength < bytes) {
    exports.memory.grow(pages);
    view = new Uint8Array(exports.memory.buffer); // 关键: grow 后重建视图
  }
}
```
