---
title: [NODE-231] worker 中处理 I/O 的陷阱？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-231：worker 中处理 I/O 的陷阱？
**答**：
- 陷阱一：worker 里做网络/DB 请求"看起来并行"——连接池每 worker 各一份（连接数 ×N），把 DB 连接打爆；解法：I/O 留主线程，worker 只算。
- 陷阱二：worker 内 fs 也是异步 I/O（libuv 线程池共享同一进程）——worker 加 fs.read 与主线程竞争 libuv 池（UV_THREADPOOL_SIZE）。
- 陷阱三：worker_data 大对象序列化在主线程执行——启动阶段主线程卡顿；大初始数据用 SharedArrayBuffer 或让 worker 自己读。
- 原则：worker 的输入输出都应该是"计算"——数据进出用 transferable/SAB，I/O 边界收口在主线程或独立 I/O worker。

```javascript
// 陷阱一示范与修正
// worker.js 反例：每 worker 各自连 DB → 8 worker × 10 连接 = 80 连接
// const db = new Pool({ max: 10 }); await db.query(...)
// 正解：worker 只算
worker.on('message', async ({ data }) => {
  parentPort.postMessage(transform(data));      // 纯计算返回，DB 由主线程写
});
// 陷阱三修正：大文件让 worker 自己读（fd 在 worker 内打开）
// worker.js: const buf = await fs.readFile(workerData.path);   // I/O 在 worker 内但走 libuv 池
// 或 workerData.sab = new SharedArrayBuffer(size); fs.readSync 到 SAB —— 零拷贝
```
