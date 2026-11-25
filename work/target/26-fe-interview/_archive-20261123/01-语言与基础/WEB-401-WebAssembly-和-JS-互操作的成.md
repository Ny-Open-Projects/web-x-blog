---
title: [WEB-401] WebAssembly 和 JS 互操作的成本在哪？什么时候值得上？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-401：WebAssembly 和 JS 互操作的成本在哪？什么时候值得上？
**答**：
- 成本点：JS↔WASM 边界传值要转换（数字便宜，字符串/大数组昂贵，最好共享内存）；GC 对象跨边界不互通。
- 值得上：计算密集（编解码、图像处理、加密、游戏物理）且调用粒度大（一次进去算很多）；不值得：频繁小调用、大量 DOM 操作。
- 工程：wasm 模块异步加载+预热编译（StreamingCompilation），体积关注 code size。

```javascript
// 差: 每次调用一个数字（边界开销>计算收益）
for (let i = 0; i < 1e6; i++) out[i] = wasm.add(i, i);
// 好: 一次传 TypedArray 进去批量算
const buf = new Float64Array(1e6);
wasm.process(buf.buffer, buf.length);   // 共享内存，零拷贝
console.log('调用粒度大才值得跨边界');
```
