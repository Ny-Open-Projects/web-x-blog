---
title: [NODE-636] Stream 背压（backpressure）怎么正确处理？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-636：Stream 背压怎么处理？
**答**：
- 背压问题：读快写慢时，不处理背压会无限积压数据在内存（缓冲区膨胀 → OOM）。
- 正确姿势：pipe/pipeline 自动管理背压（写端 write 返回 false 时暂停读端）；手工 write 时必须检查返回值——false 则 stream.once('drain') 后再继续。
- pipeline vs pipe：pipeline 自动传播错误与清理（pipe 错误处理是著名坑——任一流 error 未处理即进程崩溃 + 不清理下游）；Node 14+ 推荐 stream.pipeline / Readable.from。
- Web Streams 时代：ReadableStream.pipeTo 与 async iterator（for await of 也遵循背压——pull 模式天然背压）。
- 追问钩子：为什么「pipe 了但内存仍涨」——常见三种：① 用了 pipe 但中途 `data` 事件插手消费（把暂停逻辑绕过了）；② transform 的 _transform 忘了 callback（下游背压信号传不上来）；③ pipe 的两端之一是「永远不慢」的（如写内存数组而非真流）——背压是链路特性，任一环节破坏整链失效。

```javascript
// 错误示例（内存涨）
readable.on('data', chunk => { writable.write(chunk); });   // 无背压检查
// 正确示例
await pipeline(readable, transformStream, writable);   // 自动背压 + 错误传播
// 手工版
if (!ws.write(chunk)) await once(ws, 'drain');         // 背压等待
```
