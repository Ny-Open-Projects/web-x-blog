---
title: [NODE-009] Stream 有哪四种类型？分别对应什么应用场景？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-009：Stream 有哪四种类型？分别对应什么应用场景？
**答**：
- **Readable**（可读流）：`fs.createReadStream`、`http.IncomingMessage`、`process.stdin`——按需产生数据，两种模式：flowing（自动推送）与 paused（手动 `read()`）。
- **Writable**（可写流）：`fs.createWriteStream`、`http.ServerResponse`、`process.stdout`。
- **Duplex**（双工）：读写独立、两个缓冲区，如 TCP `net.Socket`、WebSocket。
- **Transform**（转换流）：Duplex 特例，写进去的数据被转换后可读出来，如 `zlib.createGzip()`、`crypto.createCipheriv()`。
- 核心收益：**恒定内存处理任意大的数据**——不会把 2GB 文件读进内存，而是流过管道分块处理。

```javascript
const { Readable, Writable, Duplex, Transform } = require('node:stream');
const zlib = require('node:zlib');

// Readable：生成 0~99 的流
const numbers = Readable.from((function* () { for (let i = 0; i < 100; i++) yield String(i); })());

// Transform：每行加上前缀
const addPrefix = new Transform({
  transform(chunk, _enc, cb) { cb(null, `[n] ${chunk}`); },
});

// Writable：收集到内存（演示用，生产应落盘）
const collector = new Writable({
  write(chunk, _enc, cb) { process.stdout.write(chunk); cb(); },
});

// Duplex：net.Socket 的典型代表，读写两侧独立缓冲
console.log('socket 是 Duplex:', require('node:net').Socket.prototype instanceof Duplex);

numbers.pipe(addPrefix).pipe(zlib.createGzip()); // Transform 天然可串联
numbers.pipe(collector);
```
