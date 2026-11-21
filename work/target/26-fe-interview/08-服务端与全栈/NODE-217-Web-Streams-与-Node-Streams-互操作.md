---
title: [NODE-217] Web Streams 与 Node Streams 互操作？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-217：Web Streams 与 Node Streams 互操作？
**答**：
- 两套标准并存：Node Streams（fs/net/http 传统 API）与 Web Streams（ WHATWG，fetch 的 body、Response 都是）。Node ≥17.0 提供互操作桥：Readable.toWeb/fromWeb、Writable.toWeb/fromWeb。
- 互操作价值：fetch 拿到的 Web ReadableStream 接入 Node 管道（落盘/转码），或把 Node 文件流作为 Web Response 返回（Service Worker/边缘运行时同构）。
- 差异点：Web 流背压模型（desiredSize/queuing strategies count/bytes）与 Node 水位线不同；TransformStream vs node Transform API 不同名。
- 实践建议：边界处转换一次，域内统一用一套 API；同构代码（SSR/BFF）优先 Web Streams。

```javascript
import { Readable, Writable } from 'node:stream';
import { createWriteStream } from 'node:fs';

// fetch（Web 流）→ Node 落盘
const res = await fetch(url);
const nodeReadable = Readable.fromWeb(res.body);        // Web → Node
await pipeline(nodeReadable, createWriteStream('out.bin'));

// Node 文件流 → Web Response（边缘同构）
const file = createReadStream('report.pdf');
const webStream = Readable.toWeb(file);                 // Node → Web
return new Response(webStream, { headers: { 'Content-Type': 'application/pdf' } });
// TransformStream（Web 版）
const { readable, writable } = new TransformStream({
  transform(chunk, controller) { controller.enqueue(chunk.toString().toUpperCase()); },
});
Readable.fromWeb(webSrc).pipeThrough(Readable.prototype)  // 概念示意：Web 管道用 pipeThrough
```
