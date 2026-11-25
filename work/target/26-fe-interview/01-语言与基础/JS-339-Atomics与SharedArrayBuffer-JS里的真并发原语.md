---
title: [JS-339] Atomics 与 SharedArrayBuffer：JS 里的真并发原语
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-339：Atomics 与 SharedArrayBuffer：JS 里的真并发原语

**答**：
- SAB + Atomics 是 JS 唯一的跨线程共享内存模型：普通 postMessage 是拷贝/转移，SAB 是同一块内存两个线程直接读写
- Atomics 三类操作：原子读写（load/store/add）、同步原语（wait/notify——主线程不能 wait 会阻塞 UI，只能 Worker 用）、CAS（compareExchange 实现锁）
- 自旋锁/信号量模式：compareExchange(0,1) 抢锁 → 忙等（Worker 内 Atomics.wait）→ store(0) + notify 释放——复杂度高，一般用封装库（如 wasm 的 mutex）
- JS 主线程的「伪并发」：单线程内没有数据竞争，但 async 任务交错（await 间隙状态被改）就是逻辑竞态——竞态修复不靠锁，靠「不可变快照 + 校验」
- 前端落地场景：WASM 多线程计算、Worker 池共享大 buffer、高性能视频/音频处理——普通业务用不到，知道边界即可

```javascript
// Worker 间计数器(原子)
const sab = new SharedArrayBuffer(4);
const i32 = new Int32Array(sab);
// worker 内:
Atomics.add(i32, 0, 1);                       // 原子自增
const done = Atomics.load(i32, 0);
if (done === total) postMessage('all-done');  // 通知主线程
// 主线程等待(Worker 内):
Atomics.wait(i32, 0, 0);                      // 阻塞直到被 notify
```
