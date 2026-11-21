---
title: [PER-269] Web Worker 传递大对象时内存怎么暴涨？Transferable 与 SharedArrayBuffer 怎么用？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-269：Web Worker 传递大对象时内存怎么暴涨？Transferable 与 SharedArrayBuffer 总么用？

**答**：
- 默认 structured clone：postMessage 传对象是深拷贝——10MB 二进制来回传一次就是 20MB 瞬时增量，高频传递直接内存飙升 + clone 耗时。
- Transferable（ArrayBuffer 等）：转移所有权而非拷贝，原线程立刻失去访问权（zero-copy）；适合"主线程算完给 worker 独占"的场景。传前用 `structuredClone` 不行——就是用 transfer 参数。
- SharedArrayBuffer：真正共享内存，两端读写同一块，配合 Atomics 做同步；启用前提是跨域隔离（COOP/COEP 头），Safari 支持已恢复。适合高频双向数据（视频帧、物理模拟）。
- 工程建议：大文件/图像用 transfer；只读大数据（如字体表）一次性传 worker 常驻，避免反复传；传纯 JSON 小对象无所谓 clone。

```javascript
// Transferable：所有权转移，零拷贝
const buf = new ArrayBuffer(10 * 1024 * 1024);        // 10MB
new Float32Array(buf).set(data);                      // 填充
worker.postMessage(buf, [buf]);                       // 第二个参数 = 转移列表
// 此刻主线程 buf.byteLength === 0（所有权已转移）——误用会踩"传完就没了"的坑
// SharedArrayBuffer：双向共享（需 COOP/COEP 响应头）
const sab = new SharedArrayBuffer(1024);
const view = new Int32Array(sab);
worker.postMessage({ sab });                          // 无需转移，两端同内存
Atomics.store(view, 0, 42);                           // 写端
Atomics.wait(view, 0, 0);                             // 读端等待（worker 里可用）
```
