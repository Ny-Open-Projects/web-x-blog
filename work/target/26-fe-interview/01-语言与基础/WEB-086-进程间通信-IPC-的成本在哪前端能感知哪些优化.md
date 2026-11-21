---
title: [WEB-086] 进程间通信 IPC 的成本在哪？前端能感知哪些优化手段？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-086：进程间通信 IPC 的成本在哪？前端能感知哪些优化手段？
**答**：
- 渲染进程与浏览器主进程、网络服务之间的每次通信都要序列化/反序列化（Chromium 用 Mojo），数据大、频率高时 CPU 与延迟成本显著。
- 页面层对应的同类问题：postMessage/Worker 通信走结构化克隆，大对象克隆就是"页面里的 IPC 成本"。
- 优化思路一：传不可变快照或增量而非全量；优化思路二：用 Transferable（ArrayBuffer）转移所有权实现零拷贝；优化思路三：高频流数据放 SharedArrayBuffer 共享内存。
- Service Worker 的每次 fetch 拦截、DevTools 协议通信本质都是 IPC 往返，过度拦截会放大延迟。

```javascript
// 结构化克隆的成本随对象大小线性增长
const big = { list: Array.from({ length: 1e6 }, (_, i) => i) };
console.time('clone-1M');
structuredClone(big);
console.timeEnd('clone-1M');

// 优化一：Transferable 转移所有权，零拷贝
const buf = new ArrayBuffer(16 * 1024 * 1024); // 16MB
console.time('transfer');
const w = new Worker(URL.createObjectURL(new Blob(['onmessage=()=>{}'])));
w.postMessage(buf, [buf]); // 不复制内存，buf 在本线程立刻不可用
console.timeEnd('transfer');

// 优化二：同源高频共享走 SharedArrayBuffer（需 COOP/COEP 头）
// Cross-Origin-Opener-Policy: same-origin
// Cross-Origin-Embedder-Policy: require-corp
// const sab = new SharedArrayBuffer(1024); w.postMessage(sab);
```
