---
title: [VIZ-456] WebWorker 中的几何处理（ OffscreenCanvas/SharedArrayBuffer）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-456：WebWorker 中的几何处理（ OffscreenCanvas/SharedArrayBuffer）

**答**：
- 场景：网格细分/简化/法线计算移 Worker，主线程只渲染。
- 传输：SharedArrayBuffer（COOP/COEP 头）零拷贝共享，或 Transferable ArrayBuffer（转移所有权）。
- 同步：Worker 完成回调更新 buffer；处理中显示旧帧（延迟一帧可接受）。

```javascript
// Worker 几何处理
// worker.js
self.onmessage = e => {
  const { positions, task } = e.data;
  const result = processGeometry(positions, task);   // 细分/简化
  self.postMessage({ result }, [result.buffer]);     // 转移零拷贝
};
// main:
const worker = new Worker('geo.worker.js');
function processAsync(positions, task) {
  return new Promise(res => {
    worker.onmessage = e => res(e.data.result);
    worker.postMessage({ positions, task }, [positions.buffer]);
  });
}
```
