---
title: [NODE-784] 笔试题——实现搜索索引同步管道（MQ → ES 幂等）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-784：手写索引同步

**需求与边界**：
- 需求：DB → ES 同步管道（SCN-NODE-658）——① 本地消息表（SCN-NODE-746 同事务）；② 消费幂等（版本号比对——旧事件不覆盖新文档）；③ 批量 bulk（性能）；④ 索引一致性校验（ES vs DB diff——SCN-NODE-682 对账）。
- 边界：① 版本号防乱序（seq——ES version_type external）；② bulk 部分失败处理（ES bulk 响应逐项检查——失败重试）；③ 全量重建（增量同步失败兜底——全量重索引）。

**答**：
```javascript
consumer.run({ eachBatch: async ({ batch }) => {
  const body = batch.flatMap(({ message }) => {
    const e = JSON.parse(message.value);
    return [{ index: { _index: 'goods', _id: e.id,
      version: e.seq, version_type: 'external' } }, e.doc];   // 版本防乱序（external）
  });
  const resp = await es.bulk({ body, refresh: false });
  const failed = resp.items.filter(i => i.index.error);
  if (failed.length) {                                 // bulk 部分失败
    failed.forEach(f => alert({ type: 'INDEX_FAIL', id: f.index._id, err: f.index.error }));
    await requeueFailed(failed);                       // 失败重投
  }
}});
// 一致性校验（SCN-NODE-682）
cron('0 4 * * *', async () => {
  const diff = await diffDbEs('goods');                // ES vs DB 对账
  if (diff.count > threshold) await fullReindex('goods');   // 全量重建兜底
});
```

**评分点**:
- external version 防乱序（旧事件不覆盖新文档——seq 单调）。
- bulk 部分失败处理（逐项检查 + 重投——SCN-NODE-651）。
- 全量重建兜底（增量失败的对账触发——SCN-NODE-682）。
- 本地消息表先行（SCN-NODE-746 同事务）。
