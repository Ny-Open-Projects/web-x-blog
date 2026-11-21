---
title: [HW-153] 手写 WASM 哈希计算封装——Worker 内 WASM SHA-256、分块喂入与主线程进度
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：大文件 hash（HW-140 秒传依赖）：WebCrypto 的 digest 需要全量输入（大文件内存峰值高）；WASM 增量哈希（分块 update/final）在 Worker 内流式计算——内存峰值 = 块大小，且可配合文件 slice 逐块读取，进度实时上报。

```javascript
// worker.js（伪码：以 sha256-wasm 库为例）
import { Sha256 } from './sha256.wasm.js';
self.onmessage = async ({ data: { file, chunkSize = 4 * 1024 * 1024 } }) => {
  const hasher = new Sha256();
  let offset = 0;
  while (offset < file.size) {
    const buf = await file.slice(offset, Math.min(offset + chunkSize, file.size)).arrayBuffer();
    hasher.update(new Uint8Array(buf));                     // 增量喂入（内存峰值 = 块大小）
    offset += chunkSize;
    self.postMessage({ type: 'progress', pct: +(offset / file.size * 100).toFixed(1) });
  }
  self.postMessage({ type: 'done', hash: hasher.hex() });
};
// 主线程
function hashFile(file, onProgress) {
  return new Promise((resolve) => {
    const w = new Worker('hash.worker.js');
    w.onmessage = ({ data }) => {
      if (data.type === 'progress') onProgress?.(data.pct);
      else { resolve(data.hash); w.terminate(); }           // 用完 terminate（一次性任务不驻留）
    };
    w.postMessage({ file });
  });
}
// 对比 WebCrypto：crypto.subtle.digest('SHA-256', await file.arrayBuffer()) —— 50MB 全量驻内存 + 一次性
// WASM 增量：峰值 4MB + 进度实时；速度 WASM ≈ 原生（比纯 JS 快 5~10 倍）
```

**评分点**：
- 增量 update/final 模式（内存峰值 = 块大小）vs WebCrypto 全量的一次性——本题核心。
- 分块进度实时上报；Worker 用完 terminate。
- WASM vs 纯 JS 的性能量级说明。
- 与秒传/分片上传链路的衔接（HW-140）。
