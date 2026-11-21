---
title: [OPT-097] Transferable Objects 零拷贝怎么实操？所有权模型是什么？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-097：Transferable Objects 零拷贝怎么实操？所有权模型是什么？

**答**：
- Transferable 把 ArrayBuffer 的**所有权**移交给 Worker：零字节拷贝、零克隆耗时，但原线程的 buffer 立即 detach（byteLength 变 0，不可再读写）。
- 可转移类型清单：ArrayBuffer（含 TypedArray 的 .buffer）、MessagePort、ImageBitmap、OffscreenCanvas、VideoFrame、ReadableStream。
- 实操要点：转移后原引用必须置空防误用；Worker 回传结果同样要转移，否则回程又一次克隆；需要"双端都可读"时克隆是唯一选择，要提前分清共享还是移交。
- 与 SharedArrayBuffer 的区别：转移是**移交所有权**（单端持有），SAB 是**共享同一块内存**（双端可读写，需 Atomics 同步）。

```javascript
// 一一对应：Transferable 所有权移交的完整闭环（主线程 <-> Worker）
// main.js
const buf = new ArrayBuffer(64 * 1024 * 1024); // 64MB
const view = new Float32Array(buf);
view.fill(1.0);

console.log(buf.byteLength); // 67108864
worker.postMessage(view, [view.buffer]); // 移交所有权：零拷贝
console.log(buf.byteLength); // 0 —— 已 detach，继续读写会抛错

// 所有权守卫：转移后置空，防误用
let ownedBuf = buf;
// worker.postMessage(ownedBuf, [ownedBuf]); ownedBuf = null;

// worker.js —— 处理后必须同样转移回来，否则回程克隆 64MB
self.onmessage = (e) => {
  const data = new Float32Array(e.data); // 直接在移交来的 buffer 上建视图，无复制
  for (let i = 0; i < data.length; i++) data[i] *= 2; // 计算
  const result = data;
  self.postMessage(result, [result.buffer]); // 回程零拷贝转移
};

// main.js 接收
worker.onmessage = (e) => {
  const result = new Float32Array(e.data); // 又是零拷贝
  console.log(result[0]); // 2.0
};

// ImageBitmap 转移：大图解码结果传 Worker 绘制，同样零拷贝
// const bmp = await createImageBitmap(blob);
// worker.postMessage(bmp, [bmp]);
```
