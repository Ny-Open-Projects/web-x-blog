---
title: [ARC-372] WASM 在前端业务中的架构位如何设计？何时值得引入
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-372：WASM 在前端业务中的架构位如何设计？
**答**：
- 适用场景：CPU 密集且算法成熟（图像处理/音视频编解码/加密/压缩/复杂计算库如 SQLite、FFmpeg 移植）；JS 实现慢 5~20 倍时收益明显。
- 不适用：DOM 操作（WASM 无法直接访问 DOM，边界调用成本高）、短小逻辑（加载 .wasm 的成本超过收益）。
- 架构决策：把 WASM 模块当作"带 ABI 的依赖"管理——版本锁定、体积预算（gzip 后 < 1MB 评估）、加载与实例化策略（懒加载 + Worker 内实例化）。
- JS ↔ WASM 边界设计：调用次数最小化（批处理而非逐次调用）、大数据用线性内存 + 指针传递，避免频繁结构化转换。
- 降级链路：WASM 不支持或加载失败 → 回退 JS 实现（功能等价、性能降级）→ 极端情况功能降级提示。
```javascript
// WASM 加载与降级管理
let engine;
async function getEngine() {
  if (engine) return engine;
  try {
    const { instance } = await WebAssembly.instantiateStreaming(fetch('/wasm/img.wasm'));
    engine = { blur: (buf, w, h) => instance.exports.blur(buf, w, h) };  // WASM 版
  } catch {
    engine = jsFallbackEngine;                    // JS 降级实现
  }
  return engine;
}
// 调用：批量传整帧数据，而非逐像素跨界调用
```
