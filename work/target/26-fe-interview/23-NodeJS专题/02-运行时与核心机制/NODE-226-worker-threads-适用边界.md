---
title: [NODE-226] worker_threads 适用边界：什么时候不用？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-226：worker_threads 适用边界：什么时候不用？
**答**：
- 适用：CPU 密集计算（图像处理/加解密/大 JSON 解析/压缩）、阻塞型同步库（bcrypt/pdf 生成）——解除主线程事件循环阻塞。
- 不适用一：I/O 密集（网络/DB 查询）——事件循环本就擅长，worker 反而增加通信开销。
- 不适用二：任务 < 数毫秒——worker 创建/通信开销（毫秒级）比任务本身还贵；用微任务切片（NODE-25x）。
- 不适用三：需要共享大量可变状态——worker 间只有 MessagePort 与 SharedArrayBuffer，共享复杂状态成本高。
- 面试表达：worker 是"把 CPU 任务移出事件循环"的手段，不是"多线程万能药"。

```javascript
// 决策伪代码
function shouldUseWorker(task) {
  if (task.type === 'io') return false;                 // I/O 密集：事件循环即可
  if (task.estimatedMs < 10) return false;              // 太小：开销不划算
  if (task.sharesMutableState) return false;            // 状态共享困难
  return true;                                          // CPU 密集：用 worker
}
// 适用示例：图片缩略图
// worker: sharp(buffer).resize(200).toBuffer() —— CPU/GPU 混合，主线程做它会阻塞所有请求
```
