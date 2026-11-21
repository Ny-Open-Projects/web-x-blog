---
title: [H5-233] Transferable 对象是什么，大数据零拷贝传给 Worker
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-233：Transferable 对象是什么，大数据零拷贝传给 Worker

**答**：
- Transferable：ArrayBuffer、MessagePort、ImageBitmap、OffscreenCanvas、ReadableStream、VideoFrame 等支持「所有权转移」的对象
- 语义：postMessage(msg, [transferList]) 后原线程立即失去访问权（neutered，byteLength 变 0），数据没有拷贝只有引用移交
- 典型用法：图片解码结果 ImageBitmap 转移给 Worker 处理、大二进制（文件、音频 PCM）双向传递
- 设计意义：让 Worker 体系真正适合大数据管线，否则 clone 开销吃掉并行收益
- 钩子：普通对象数组不能 transfer，只能 clone——要传大数据请用 TypedArray 的 buffer

```javascript
// 图片解码转移到 Worker 处理再转回来
const bitmap = await createImageBitmap(imgBlob);
worker.postMessage({ bitmap }, [bitmap]);        // 转走
// worker 里处理完
const out = await createImageBitmap(offscreen);
postMessage({ bitmap: out }, [out]);             // 零拷贝转回主线程
```
