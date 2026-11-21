---
title: [PER-276] SharedArrayBuffer + Atomics.wait 会在主线程阻塞，跨线程同步的正确姿势是什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-276：SharedArrayBuffer + Atomics.wait 会在主线程阻塞，跨线程同步的正确姿势是什么？

**答**：
- Atomics.wait 是"忙等待"式阻塞：调用线程挂起直到条件满足。**主线程禁止 wait**（会抛错——浏览器不允许 UI 线程阻塞）；只在 Worker 里可用。
- 主线程等待的正确姿势：反向等待——主线程用 `Atomics.notify`（Worker 写完通知）+ 事件/postMessage 感知；或主线程不等待，数据就绪后 Worker postMessage 通知，主线程读共享内存。
- Worker 侧等待：`Atomics.wait(int32, index, expectedValue, timeout)` 挂起等主线程 `Atomics.store + Atomics.notify` 唤醒——适合"worker 拉取主线程输入"的拉模式。
- 内存序注意：共享内存并发写需要 Atomics.store/load（而不是普通数组访问），否则写入可见性不保证；临界区尽量小，能消息传递就不要共享内存（复杂度成本高）。

```javascript
// 主线程（不能 wait，只 store + notify）
const sab = new SharedArrayBuffer(1024);
const i32 = new Int32Array(sab);
document.querySelector('input').addEventListener('change', (e) => {
  i32[1] = e.target.value.length;            // 普通写不保证可见性，用 Atomics：
  Atomics.store(i32, 1, e.target.value.length);
  Atomics.notify(i32, 1);                    // 唤醒 worker 里 wait 的线程
});
// worker.js（可以 wait）
const i32 = new Int32Array(msg.sab);
while (Atomics.load(i32, 1) === 0) {
  Atomics.wait(i32, 1, 0, 1000);             // 阻塞等待（worker 独有），带超时
}
// 拿到数据后处理；结论：数据流尽量 postMessage，wait 只做 worker 侧的细粒度同步
```
