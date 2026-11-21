---
title: [NODE-215] 流式 transform 大文件 CSV 逐行处理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-215：流式 transform 大文件 CSV 逐行处理？
**答**：
- 场景：1GB CSV 导入 DB——不可 readline 全量数组（内存爆炸），用 pipeline + Transform 逐行批处理（NODE-213 的应用层）。
- 批量阈值：攒 N 行（如 1000）批量 insert（减少 DB 往返），攒批本身就是缓冲，要控制批大小配合背压（insert 慢 → cb 晚调 → 上游自动暂停）。
- 断点续跑：记录已处理行号/字节偏移，失败从 checkpoint 续传（createReadStream 的 start 参数）。
- 编码陷阱：多字节字符跨 chunk 截断（UTF-8 中文），要用 string_decoder 或 split('\n') 前先完整解码。

```javascript
import { pipeline, Transform } from 'node:stream';
import { StringDecoder } from 'node:string_decoder';

class CsvBatch extends Transform {
  #buf = ''; #batch = []; #rowNo = 0;
  #decoder = new StringDecoder('utf8');
  constructor(private insertBatch) { super({ highWaterMark: 64 * 1024 }); }
  _transform(chunk, enc, cb) {
    this.#buf += this.#decoder.write(chunk);          // 完整解码防截断
    const lines = this.#buf.split('\n');
    this.#buf = lines.pop()!;
    for (const line of lines) this.#collect(line);
    cb();                                             // 数据量大时上游背压自动生效
  }
  #collect(line) {
    if (!line) return;
    this.#batch.push(parseCsvLine(line));
    if (this.#batch.length >= 1000) {
      const b = this.#batch; this.#batch = [];
      this.insertBatch(b);                            // DB 写入（异步化可在 flush 阶段）
    }
  }
  _flush(cb) {
    if (this.#buf) this.#collect(this.#buf + this.#decoder.end());
    if (this.#batch.length) this.insertBatch(this.#batch);
    cb();
  }
}
await pipeline(createReadStream('big.csv'), new CsvBatch(bulkInsert), { signal });
```
