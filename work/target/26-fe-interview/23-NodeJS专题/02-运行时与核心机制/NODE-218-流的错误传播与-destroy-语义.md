---
title: [NODE-218] 流的错误传播与 destroy 语义？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-218：流的错误传播与 destroy 语义？
**答**：
- destroy(err)：统一终止入口——触发 'error'（若有 err）→ 'close'；destroy 后 push/write 均无效，'finish' 不再触发。
- propagateDestroy：pipeline 负责把一环 destroy 传到全链；手工管理时用 stream.finished()（promisified）观察终结状态（error/close/end 三态合一）。
- autoDestroy 选项：现代流默认 true——'end'/'error' 后自动 destroy；手写流类要显式设置（否则半开流）。
- 典型坑：双回调（cb(err) 后继续 push）、destroy 后仍 write（ERR_STREAM_DESTROYED）、忘记 error 监听（uncaughtException）。

```javascript
import { finished } from 'node:stream/promises';
import { Transform } from 'node:stream';

const t = new Transform({
  autoDestroy: true,                          // 现代默认
  transform(chunk, enc, cb) {
    if (bad(chunk)) return cb(new Error('bad chunk'));   // cb(err) → 自动 destroy → 'error'
    cb(null, chunk);
  },
});
t.on('error', e => log.error(e));             // 必须监听，否则 uncaughtException
// 终结观察（等价 finished 回调版）：
const done = finished(source, { cleanup: true }, (err) => {
  log.info('stream finished', err?.message ?? 'ok');     // error/close/end 三态合一
});
source.destroy(new Error('abort'));           // 触发 error + close；finished resolve/reject
```
