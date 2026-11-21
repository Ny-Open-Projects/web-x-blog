---
title: [VIZ-130] Web Worker 与可视化的结合有哪些模式？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-130：Web Worker 与可视化的结合有哪些模式？
**答**：主线程只留渲染与交互，重计算全部下沉 Worker：① **数据加工**——聚合/排序/过滤/降采样在 Worker 做，postMessage 传 **Transferable**（ArrayBuffer 所有权转移，零拷贝）；② **布局计算**——力导向图迭代、大规模 hexbin 聚合；③ **共享内存**——SharedArrayBuffer + Atomics 同步进度（需 COOP/COEP 头）；④ **预取管线**——Worker 预加载预解码下一窗口数据。注意：DOM/ECharts 实例不能进 Worker；结构化克隆大对象很慢要传 TypedArray；Worker 池按 CPU 核数开，Comlink 可省手写协议。

```javascript
// 主线程 <-> Worker：Transferable 零拷贝传大数组
const worker = new Worker('agg-worker.js');
worker.postMessage({ type: 'histogram', buf: bigBuffer }, [bigBuffer]); // 转移所有权
// agg-worker.js
self.onmessage = ({ data: { type, buf } }) => {
  const values = new Float64Array(buf);
  const bins = new Uint32Array(64);                  // 分桶聚合
  for (let i = 0; i < values.length; i++)
    bins[Math.min(63, Math.max(0, values[i] * 64 | 0))]++;
  self.postMessage({ type, bins: bins.buffer }, [bins.buffer]); // 结果也零拷贝传回
};
// 主线程收到后 new Uint32Array(e.data.bins) 直接画图
// 注意：buf 转移后主线程不可再用；Comlink.wrap(new Worker(...)) 可省手写协议
```
