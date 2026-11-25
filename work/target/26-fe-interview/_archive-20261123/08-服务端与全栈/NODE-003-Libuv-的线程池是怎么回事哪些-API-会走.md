---
title: [NODE-003] Libuv 的线程池是怎么回事？哪些 API 会走线程池？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-003：Libuv 的线程池是怎么回事？哪些 API 会走线程池？
**答**：
- Node 主线程是单线程跑 JS，但 Libuv 默认维护一个 **4 线程**的线程池（可通过 `UV_THREADPOOL_SIZE` 调到最多 1024）。
- 走线程池的 API（高频，必须记全）：**fs 模块的全部文件 I/O**（`fs.readFile`/`writeFile`/`readdir` 等）、`dns.lookup`（注意不是 `dns.resolve`，后者走 c-ares 异步）、部分 **crypto**（`pbkdf2`、`scrypt`、`randomBytes`、`randomFill`）、**zlib**（`gzip`/`gzipSync` 等压缩解压）。
- 不走线程池的：网络 I/O（TCP/UDP/HTTP）由 OS 的 epoll/kqueue/IOCP 异步通知，`dns.resolve` 走 c-ares。
- 实战意义：文件 I/O、`pbkdf2`、zlib 是 CPU 密集/阻塞大户，并发高时会排队占满线程池，拖慢所有走线程池的调用——所以密码哈希、压缩要控制成本或调大线程池。

```javascript
// 线程池验证与调优：pbkdf2 是 CPU 密集型，走 Libuv 线程池
const crypto = require('crypto');

const t1 = Date.now();
// 4 个并发 pbkdf2，默认线程池 4，约并行执行，总耗时 ≈ 单次耗时
for (let i = 0; i < 5; i++) {
  crypto.pbkdf2('secret', 'salt', 100000, 64, 'sha512', () => {
    console.log(`done ${i}, cost ${Date.now() - t1}ms`);
    // 前 4 个耗时接近，第 5 个要等有线程空闲，耗时约翻倍 → 证明线程池大小为 4
  });
}

// 启动时调大线程池：UV_THREADPOOL_SIZE=16 node app.js
// 场景：大量文件 I/O + 图片压缩（zlib/sharp）的服务建议调到 8~16
```
