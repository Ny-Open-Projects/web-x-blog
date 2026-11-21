---
title: [H5-234] SharedArrayBuffer 为什么被 COOP/COEP 锁起来
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-234：SharedArrayBuffer 为什么被 COOP/COEP 锁起来

**答**：
- SharedArrayBuffer（SAB）：主线程与 Worker 共享同一块内存，配合 Atomics 做真·多线程
- 被封杀的原因：Spectre/Meltdown 侧信道攻击可以利用高精度计时读越权内存，SAB 提供了攻击所需的共享内存与时间测量
- 解锁条件：页面带 `Cross-Origin-Opener-Policy: same-origin` + `Cross-Origin-Embedder-Policy: require-corp`——把自己的页面与不受信资源隔离成独立进程
- 实际影响：开了 COEP 后所有跨域子资源必须带 CORS/CORP 头，接入成本高，很多团队因此放弃 SAB
- 替代方案：不涉及共享写只需传递时，用 Transferable；计时需求用 performance.now（已被降精度）

```http
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```
```javascript
const sab = new SharedArrayBuffer(1024);        // 需要上面两个响应头才可用
Atomics.store(new Int32Array(sab), 0, 42);      // Worker 侧 Atomics.load 同步读
```
