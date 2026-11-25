---
title: [WEB-585] Mojo IPC：多进程通信的成本对前端有什么影响
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## WEB-585：Mojo IPC：多进程通信的成本对前端有什么影响

**答**：
- 浏览器进程/渲染进程/GPU/网络进程之间用 Mojo IPC 通信，跨进程传输要序列化/拷贝——一切「渲染进程外的数据交换」都有 IPC 成本
- 前端可感知的 IPC 场景：fetch 响应体（网络→渲染）、postMessage 存储访问（localStorage 是同步 IPC 之外的特例但同步阻塞主线程）、Canvas 位图上屏（渲染→GPU，用共享内存优化）、WebRTC/编解码（渲染↔GPU/音频进程）
- 成本量级：小消息微秒级可忽略；大 payload（MB 级位图/文本）毫秒级，主线程合并器在 task 里能测出
- 优化即「少跨界」：大图像处理放 Worker + OffscreenCanvas（Worker 也在渲染进程内，减少与 GPU 的一次次往返）；流式处理用 Streams API 减少整包拷贝
- 理解这条线索能解释很多「性能玄学」：同为主线程任务，触发 IPC 的（fetch 回调上屏）比纯 JS 计算更贵

```javascript
// OffscreenCanvas: 位图处理留在渲染进程内, 最终结果一次性上屏
const worker = new Worker('paint.js');
const off = new OffscreenCanvas(800, 600);
worker.postMessage({ canvas: off }, [off]); // 转移所有权, 零拷贝
// paint.js 内部绘制 → commit 到页面显示, 避免 主线程↔GPU 反复小步 IPC
```
