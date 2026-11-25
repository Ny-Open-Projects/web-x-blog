---
title: [OPT-098] SharedArrayBuffer 和 Atomics 是什么概念？前端哪里用得上？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-098：SharedArrayBuffer 和 Atomics 是什么概念？前端哪里用得上？

**答**：
- SharedArrayBuffer 让**两个线程读写同一块物理内存**，不再有克隆与转移开销；但它带来数据竞争，必须配 `Atomics`（原子操作：add/load/store/wait/notify）保证同步。
- 前置条件苛刻：跨域隔离头 `Cross-Origin-Opener-Policy: same-origin` + `Cross-Origin-Embedder-Policy: require-corp`，否则 SAB 不可用（Spectre 缓解）。
- 典型前端场景：Worker 池共享同一份超大矩阵做并行计算（图像处理/物理引擎）；`Atomics.wait` 在主线程不可用（会冻结 UI），要用 `Atomics.waitAsync`。
- 没有强需求不上：大多数业务用 Transferable 转移 + 分块就够，SAB 增加的是心智负担（内存序、自旋锁）。

```javascript
// 一一对应：SAB + Atomics 的最小可用示例（主线程与 Worker 共享计数/任务槽）
// 前置：响应头必须配置
//   Cross-Origin-Opener-Policy: same-origin
//   Cross-Origin-Embedder-Policy: require-corp

// main.js
if (!crossOriginIsolated) {
  console.warn('未跨域隔离，SAB 不可用'); // 页面级检查
}
const sab = new SharedArrayBuffer(1024);
const int32 = new Int32Array(sab);
int32[0] = 0; // [0] 作任务计数器，[1] 作就绪标志
worker.postMessage(sab); // SAB 不需要转移，本来就是共享

// 主线程投递任务号
Atomics.store(int32, 0, taskId);
Atomics.notify(int32, 0); // 唤醒 wait 中的 Worker

// worker.js
self.onmessage = (e) => {
  const int32 = new Int32Array(e.data);
  while (true) {
    // 原子等待：睡眠等主线程 notify，不烧 CPU（wait 在 Worker 内合法）
    Atomics.wait(int32, 0, Atomics.load(int32, 0)); // 值变化才被唤醒
    const task = Atomics.load(int32, 0);
    const result = heavyCompute(task);
    // 原子写结果 + 置就绪标志，主线程可轮询 load
    Atomics.store(int32, 1, result);
    Atomics.store(int32, 2, 1); // ready flag
  }
};

// 主线程读取结果：wait 不可用于主线程，用 waitAsync（返回 Promise）
Atomics.waitAsync(int32, 2, 0).value.then(() => {
  console.log('worker 结果:', Atomics.load(int32, 1));
});
```
