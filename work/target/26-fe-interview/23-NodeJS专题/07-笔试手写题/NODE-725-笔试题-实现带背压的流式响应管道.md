---
title: [NODE-725] 笔试题——实现带背压的流式响应（DB → transform → HTTP）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-725：手写背压管道

**需求与边界**：
- 需求：DB 游标流 → 行转换 → HTTP 响应（CSV 导出，SCN-NODE-681）——① pipeline 组合（背压自动——SCN-NODE-636）；② 行级转换（列映射/格式化）；③ 错误传播（任一失败——响应中断 + 日志，资源清理）；④ 客户端断开中断源（DB 游标关闭——资源回收）。

**答**：
```javascript
import { pipeline } from 'stream/promises';
app.get('/export', async (req, res) => {
  res.setHeader('Content-Type', 'text/csv');
  const dbStream = await db.queryStream('SELECT * FROM t');   // 游标流
  req.on('close', () => dbStream.destroy());           // 客户端断开：关游标（资源回收）
  const transform = new Transform({
    objectMode: true,
    transform(row, enc, cb) {
      cb(null, `${row.id},${row.name},${row.ts}\r\n`); // 行级转换
    },
  });
  try {
    await pipeline(dbStream, transform, res, { end: true });   // 背压自动（SCN-NODE-636）
  } catch (e) {
    if (!res.headersSent) res.status(500);
    else res.end();                                    // 已发数据：中断（部分文件）
    logger.error({ err: e, traceId: als.getStore()?.traceId });
  }
});
// 背压语义：客户端慢 → res 缓冲满 → transform 暂停 → DB 游标暂停——全链 O(1) 内存
```

**评分点**:
- pipeline 组合（自动背压 + 错误传播——SCN-NODE-636 正确姿势）。
- 客户端断开 → 游标销毁（资源回收——DB 连接不泄漏）。
- 错误处理区分（headersSent 前/后——响应语义正确）。
- 全链内存 O(1)（背压链完整性——大文件不 OOM）。
