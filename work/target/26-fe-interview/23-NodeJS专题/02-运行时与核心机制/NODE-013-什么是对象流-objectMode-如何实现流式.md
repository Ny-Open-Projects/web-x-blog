---
title: [NODE-013] 什么是对象流（objectMode）？如何实现流式 JSON 解析（NDJSON）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-013：什么是对象流（objectMode）？如何实现流式 JSON 解析（NDJSON）？
**答**：
- 默认流传输 Buffer/字符串；设置 `objectMode: true`（或 `stream.pipeline` 自动推断）后可以在流中传递**任意 JS 对象**，省去序列化，常见于数据库查询流、消息处理管道。
- NDJSON（每行一个 JSON）是日志与 LLM SSE 的通用格式：按行 split → `JSON.parse` → 对象流，天然支持增量处理超大文件。
- 流式 JSON（单个大 JSON 对象，非 NDJSON）需要增量 parser（如 `stream-json`），或约定为行分隔协议——面试中先说明协议选择比硬写 parser 更重要。

```javascript
const fs = require('node:fs');
const { Transform, pipeline } = require('node:stream');

// NDJSON 解析为对象流
class JsonParseTransform extends Transform {
  constructor(opts = {}) { super({ ...opts, objectMode: true, readableObjectMode: true }); }
  _transform(chunk, _enc, cb) {
    for (const line of chunk.toString().split('\n')) {
      if (!line.trim()) continue;
      try { this.push(JSON.parse(line)); }
      catch (e) { /* 坏行跳过并告警，不中断整个流 */ this.emit('warn', e.message); }
    }
    cb();
  }
}

// 消费对象流：逐条处理订单日志
pipeline(
  fs.createReadStream('orders.ndjson'),
  new JsonParseTransform(),
  async function* (source) {           // async generator 也是合法的 Transform
    let amount = 0;
    for await (const order of source) amount += order.price * order.count;
    console.log('订单总额:', amount);
  },
  (err) => err && console.error('解析失败:', err),
);
// orders.ndjson 内容：{"price":10,"count":2}\n{"price":3.5,"count":4}\n
```
