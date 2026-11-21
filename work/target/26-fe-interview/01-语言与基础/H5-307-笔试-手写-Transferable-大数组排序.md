---
title: [H5-307] 笔试：手写 Transferable 大数组排序
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Worker]
type: 笔试题
---

## H5-307：笔试：手写 Transferable 大数组排序

**题目**：实现 `sortBig(floatArray)`：把 1 亿元素的 Float32Array 传给 Worker 排序，排序结果零拷贝返回主线程。注意转移后原数组的可用性与时序。

**答**：
```javascript
// worker.js
self.onmessage = ({ data }) => {
  const arr = new Float32Array(data); // 收到的是转移来的 buffer
  arr.sort();                         // TypedArray.sort 数值排序
  self.postMessage(arr.buffer, [arr.buffer]); // 转移回去
};
// main.js
async function sortBig(floatArray) {
  const worker = new Worker('worker.js');
  const buf = floatArray.buffer;
  const p = new Promise(resolve => worker.onmessage = ({ data }) => resolve(data));
  worker.postMessage(buf, [buf]);      // 转移所有权，主线程此时不能用
  const sortedBuf = await p;
  worker.terminate();
  return new Float32Array(sortedBuf);  // 用返回的 buffer 重建视图
}
const big = new Float32Array(1e8).map(() => Math.random());
const sorted = await sortBig(big);
console.log(big.byteLength); // 0 —— 原 buffer 已被转移（neutered）
```

**评分点**：
- 理解转移语义：postMessage 后原 buffer neutered（byteLength=0），这是核心考点
- TypedArray.sort() 是数值排序（默认 sort 字符串化的问题不存在于 TypedArray）
- 返回后用新 Float32Array 视图包装 buffer
- 一次性任务用完 terminate 回收
