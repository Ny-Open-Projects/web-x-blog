---
title: [NODE-219] objectMode 流的使用场景？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-219：objectMode 流的使用场景？
**答**：
- objectMode：流中传输 JS 对象而非 Buffer——highWaterMark 语义变成"对象个数"（默认 16）；适合 ETL/行解析/对象级 ETL 管道。
- 混合流：transform 可设 readableObjectMode 与 writableObjectMode 分别控制两侧（Buffer 进 → 对象出：行解析器）。
- 注意点：对象流不做字节拷贝，性能好但对象引用共享要小心（下游修改影响上游数据）；序列化成本在边界处理。
- 典型链：fs 行读（文本流）→ CSV parse（对象流）→ 聚合（对象流）→ JSON.stringify（文本流出）。

```javascript
import { Transform } from 'node:stream';
// Buffer 进 → 对象出（只 readableObjectMode）
class CsvParse extends Transform {
  #buf = '';
  constructor() { super({ readableObjectMode: true }); }
  _transform(chunk, enc, cb) {
    this.#buf += chunk;
    const lines = this.#buf.split('\n');
    this.#buf = lines.pop()!;
    lines.forEach(l => this.push(parseCsv(l)));          // 对象逐行 push
    cb();
  }
  _flush(cb) { if (this.#buf) this.push(parseCsv(this.#buf)); cb(); }
}
// 对象进 → Buffer 出
class ToJson extends Transform {
  constructor() { super({ writableObjectMode: true }); }
  _transform(obj, enc, cb) { cb(null, JSON.stringify(obj) + '\n'); }   // 文本输出
}
// pipeline(fs read, new CsvParse(), new ToJson(), writeStream)
```
