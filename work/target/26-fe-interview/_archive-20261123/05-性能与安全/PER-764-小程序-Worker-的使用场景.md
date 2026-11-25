---
title: [PER-764] 小程序 Worker 的使用场景与性能边界：什么计算值得进 Worker、通信成本怎么算？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-764：小程序 Worker 的使用场景与性能边界：什么计算值得进 Worker、通信成本怎么算？

**答**：
- 适用：纯计算且数据量适中的任务（大 JSON 解析重组、加解密、图片像素处理、排序聚合）——Worker 与主线程通信是序列化拷贝，**大数据传输的 clone 成本可能超过计算本身**。
- 边界判断：任务耗时 > 50ms 且输入输出 < 1MB 才值得；否则主线程分片（chunk + rAF）更便宜。Worker 不能访问 DOM/大部分 API（wx 有限接口），UI 更新必须回主线程。
- 通信优化：传 ArrayBuffer（transferable 语义视平台支持）、传索引引用（Worker 只算结果索引，主线程取数）、批量任务复用同一 Worker 实例（创建有开销）。
- 度量：Worker 任务耗时、通信传输大小与 clone 耗时、主线程让出的帧收益。

```javascript

const workerPolicy = {
  worth: '任务 > 50ms 且输入输出 < 1MB 才进 Worker',
  notWorth: '大数据 clone 成本可能超过计算收益 -> 主线程分片更便宜',
  comm: ['传 ArrayBuffer 减拷贝', '传索引引用 Worker 只算结果', '复用 Worker 实例（创建有开销）'],
  limit: 'Worker 无 DOM/有限 wx API，UI 更新回主线程',
};
// worker 内
worker.onMessage(({ buf }) => {
  const arr = new Float64Array(buf);
  const result = heavyCompute(arr);                             // >50ms 的计算
  worker.postMessage({ out: result.buffer }, [result.buffer]);  // transferable 减拷贝
});
// 主线程分片对照方案：chunk + rAF，适合 < 50ms 或大数据任务
```
