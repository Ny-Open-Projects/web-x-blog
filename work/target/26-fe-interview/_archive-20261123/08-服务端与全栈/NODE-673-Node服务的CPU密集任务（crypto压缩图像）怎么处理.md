---
title: [NODE-673] CPU 密集任务（crypto/压缩/图像）怎么处理？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-673：CPU 密集任务怎么处理？
**答**：
- 优先用内置异步：crypto（async API——底层 libuv 线程池）、zlib（stream/promise API）、sharp（图像——libvips 线程池）——「库自带异步」优先于自建 worker。
- libuv 线程池：默认 4 线程（UV_THREADPOOL_SIZE）——被 fs/dns/crypto 共享，加密高峰会饿 DNS 解析——调大线程池是显式决策。
- 真正的 JS 计算进 worker：SCN-NODE-634 选型（>10ms 高频）；worker 池化 + 任务合并（小任务合并批量——通信开销摊薄）。
- 削峰：CPU 任务排队（并发上限——防 CPU 饱和拖垮事件循环）+ 超时（卡死任务杀——SCN-NODE-648 崩溃防御）。
- 追问钩子：为什么「crypto 高峰期 DNS 变慢」——libuv 线程池默认 4 线程被 fs/crypto/dns(getaddrinfo) 共享；PBKDF2 密集时线程池满，DNS 解析排队——表现为「登录慢连带域名解析慢」；UV_THREADPOOL_SIZE 调大或加密分离（独立服务）——共享线程池是 Node 隐性资源竞争的头号案例。

```javascript
// 优先内置异步（libuv 线程池）
await promisify(crypto.pbkdf2)(pwd, salt, 100_000, 32, 'sha256');
// JS 密集进池（SCN-NODE-634）
const pool = new Piscina({ maxThreads: 4, idleTimeout: 10_000 });
// 线程池扩容（显式决策）
process.env.UV_THREADPOOL_SIZE = '16';                 // 启动前设置
```
