---
title: [WEB-616] WASM 与 JS 的类型边界：什么数据跨得快
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-616：WASM 与 JS 的类型边界：什么数据跨得快

**答**：
- 边界现状：WASM MVP 只支持数值类型（i32/i64/f32/f64）直接交换，字符串/对象都要走线性内存序列化——跨边界传字符串是 WASM 优化的头号大坑
- 高频小调用会被边界成本吃掉收益：单次跨界约几十到上百 ns，循环里每元素调一次 wasm 函数比纯 JS 还慢；正确姿势是批量传（一次传数组整体）
- wasm-gc 与 JS Interop 提案（部分已落地）：让 GC 对象直接跨边界引用，减少序列化，但浏览器支持度差异大，生产仍以线性内存方案为主
- 大数据零拷贝路径：JS TypedArray 与 WASM 线性内存共享（new Uint8Array(memory.buffer)），传指针+offset 即可，这是图像/音频处理的标配
- 决策口诀：计算密集 + 数据扁平 → WASM 收益大；频繁字符串/对象交互 → 边界成本反噬

```javascript
// 批量传递: 共享线性内存, 传指针而非逐个调用
const { memory, process_pixels } = instance.exports;
const buf = new Uint8Array(memory.buffer, 0, pixels.length);
buf.set(pixels);                          // 数据进线性内存(零拷贝共享)
const outPtr = process_pixels(pixels.length); // 只跨界一次: 传长度
const out = new Uint8Array(memory.buffer, outPtr, pixels.length); // 结果仍共享
```
