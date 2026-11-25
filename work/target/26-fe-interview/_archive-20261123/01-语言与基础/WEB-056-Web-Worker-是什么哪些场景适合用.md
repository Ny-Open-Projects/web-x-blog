---
title: [WEB-056] Web Worker 是什么？哪些场景适合用？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-056：Web Worker 是什么？哪些场景适合用？
**答**：
- Worker 在独立线程执行 JS，与主线程通过 postMessage 传递消息（结构化克隆），不阻塞 UI。
- 适用：大 JSON 解析、图片/视频处理、复杂计算、WebAssembly 配合的重负载。
- 限制：无 DOM/window 访问，不能直接操作页面；与主线程通信有序列化开销，超大对象可用 Transferable（ArrayBuffer 转移所有权）零拷贝传递。
- 类型：Dedicated Worker（专属）、Shared Worker（多标签共享）、Service Worker（代理网络与离线）。

```javascript
// main.js：主线程把重计算交给 Worker，UI 不卡顿
const worker = new Worker(new URL('./fib.worker.js', import.meta.url)); // Vite/webpack 都支持

worker.postMessage({ n: 40 });
worker.addEventListener('message', (e) => {
  console.log('worker result:', e.data); // 计算期间页面可以正常响应点击
});
worker.addEventListener('error', (e) => console.error(e.message));

// Transferable 示例：转移 ArrayBuffer 所有权，零拷贝
const buffer = new ArrayBuffer(1024 * 1024); // 1MB
worker.postMessage({ buffer }, [buffer]); // 转移后主线程不能再读 buffer
console.log(buffer.byteLength); // 0，所有权已移交
```

```javascript
// fib.worker.js：worker 文件里没有 DOM，只有消息通道
self.addEventListener('message', (e) => {
  const { n } = e.data;

  function fib(k) {
    let [a, b] = [0, 1];
    for (let i = 0; i < k; i++) [a, b] = [b, a + b];
    return a;
  }

  const result = fib(n);
  self.postMessage(result); // 回传主线程
});
```
