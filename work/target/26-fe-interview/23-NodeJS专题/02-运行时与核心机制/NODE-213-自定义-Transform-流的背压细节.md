---
title: [NODE-213] 自定义 Transform 流的背压细节？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-213：自定义 Transform 流的背压细节？
**答**：
- Transform 的 _transform(chunk, enc, cb)：cb(err, out) 完成"读一块→写一块"；背压自动由可读/可写两侧 highWaterMark 协调——但**同步消费 cb 会导致缓冲**（readable 的 readableFlowing 语义）。
- 关键规则：在 cb 里再 write 输出比 chunk 大的数据（膨胀转换）时要检查返回值/依赖框架的回调机制；正确做法是回调式：`cb(null, out)` 一次一块。
- _flush(cb)：收尾（如压缩尾部块），必须调用 cb，否则流永不结束。
- objectMode：对象流（JSON 行处理）背压按"对象个数"计——highWaterMark 语义是数量。

```javascript
import { Transform } from 'node:stream';
class LineCounter extends Transform {
  #buf = '';
  constructor() { super(); }
  _transform(chunk, enc, cb) {
    this.#buf += chunk.toString();
    const lines = this.#buf.split('\n');
    this.#buf = lines.pop()!;                       // 残行留到下一块
    this.count += lines.length;
    cb();                                           // 输出在 flush（或逐行 push）
  }
  _flush(cb) {
    if (this.#buf) this.count++;                    // 最后一行
    this.push(String(this.count));
    cb();                                           // 不调用 → 流卡死
  }
}
// 膨胀转换的反例与正解：
// 反例：_transform 里 while 大循环 push 全部结果 —— 忽略背压
// 正解：一次 cb(null, oneChunk)，让 readable/writable 两侧的水位线协调节奏
```
