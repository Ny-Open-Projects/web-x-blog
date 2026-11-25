---
title: [PER-020] Web Worker 的使用场景是什么？如何与主线程通信？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-020：Web Worker 的使用场景是什么？如何与主线程通信？

**答**：
- Worker 在独立线程执行 JS，不阻塞主线程渲染与交互，适合大数据排序/解析、图片处理、加密解密、复杂计算。
- 通信基于 `postMessage` 的结构化克隆，传大对象有拷贝开销；二进制数据可用 Transferable（ArrayBuffer）转移所有权实现零拷贝。
- 限制：不能操作 DOM、不能访问 `window`，可用 `self` 访问部分全局 API；worker 内也能 importScripts 或 ESM import。
- Vite/webpack 下用 `new Worker(new URL('./xx.worker.js', import.meta.url))` 标准写法，打包器自动处理。

```javascript
// main.js —— 主线程把重计算交给 Worker，避免卡死 UI
const worker = new Worker(new URL('./fib.worker.js', import.meta.url));

worker.postMessage({ n: 40 });
worker.onmessage = (e) => {
  console.log('计算结果', e.data);
  worker.terminate(); // 用完及时终止，释放线程
};

// fib.worker.js —— Worker 线程内独立执行
self.onmessage = (e) => {
  const { n } = e.data;
  let a = 0, b = 1;
  for (let i = 0; i < n; i++) [a, b] = [b, a + b];
  self.postMessage(b);
};
```
