---
title: [NODE-010] 什么是背压（backpressure）？pipe、pipeline、stream.compose 有何区别？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-010：什么是背压（backpressure）？pipe、pipeline、stream.compose 有何区别？
**答**：
- 背压：写端消费速度跟不上读端生产速度时，`write()` 返回 `false`，表示内部缓冲超过 `highWaterMark`（默认 64KB），数据积压在内存里。手工处理要 `drain` 事件配合暂停读取，**pipe 自动处理背压**。
- **pipe**：自动背压但**不会转发错误、出错不会销毁流**，流可能悬挂且 fd 泄漏——生产环境禁用。
- **pipeline**（推荐）：自动背压 + 任一流错误会 destroy 整条链 + Promise 化（await），错误集中处理。
- **stream.compose**（Node 17+）：pipeline 的链式封装，返回可继续 pipe 的 Transform，支持 `signal` 中断与预置销毁，适合动态组装管道。

```javascript
const fs = require('node:fs');
const zlib = require('node:zlib');
const { pipeline, compose } = require('node:stream/promises');
const { compose: composeStream } = require('node:stream');

// 错误示范：read.pipe(write) 出错时 write 未销毁，fd 泄漏
// 正确：pipeline + 集中错误处理
async function gzipFile(src, dest) {
  await pipeline(
    fs.createReadStream(src),
    zlib.createGzip(),
    fs.createWriteStream(dest),
  );
  console.log('压缩完成');
}
gzipFile('access.log', 'access.log.gz').catch((err) => {
  console.error('pipeline 任一环节失败都会到这里并销毁全链:', err.message);
});

// stream.compose：把多个流组合成一个 Transform，可继续参与其他管道
const compressor = composeStream(zlib.createGzip(), zlib.createGzip()); // 双重压缩（示意）
fs.createReadStream('access.log')
  .pipe(compressor)
  .pipe(fs.createWriteStream('access.log.gz2'))
  .on('finish', () => console.log('compose 组合完成'));

// 手工背压（理解原理用）：write 返回 false 时暂停，drain 后恢复
// rs.on('data', (chunk) => { if (!ws.write(chunk)) rs.pause(); });
// ws.on('drain', () => rs.resume());
```
