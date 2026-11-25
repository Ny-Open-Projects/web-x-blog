---
title: [NODE-755] 笔试题——实现对账分片执行器（分片 + 断点 + 差异工单）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-755：手写对账执行器

**需求与边界**：
- 需求：对账执行（SCN-NODE-682）——① 按小时分片（失败只重跑该小时——SCN-NODE-682）；② 断点记录（幂等——已完成小时跳过）；③ 多重匹配（SCN-FIN-552 复用）；④ 差异自动/人工分流（SCN-OPS-259 边界声明）。
- 边界：① 渠道文件延迟（重试日历——T+2 补对）；② 分片并发（多 worker 并行小时——互不依赖）；③ 差异率突增告警（趋势——SCN-NODE-682 监控）。

**答**：
```javascript
async function reconcileDay(date) {
  const shards = hoursOf(date);                        // 24 小时分片
  const results = await Promise.all(shards.map(async (h) => {
    if (await isDone(date, h)) return { hour: h, skipped: true };   // 断点幂等（SCN-NODE-655）
    const mine = await db.ordersByHour(date, h);
    const theirs = await withRetry(() => parseChannelFile(date, h), 3,   // 渠道文件延迟重试
      { retriable: (e) => e.code === 'FILE_NOT_YET' });
    if (!theirs) return deferHour(date, h);            // 延迟：排入 T+2 补对日历
    const diff = reconcilePair(mine, theirs);          // 多重匹配（SCN-FIN-552）
    await dispatchDiffs(diff, { autoRule: (d) => d.kind === 'LONG' && d.amount < 100 });   // 自动/人工分流
    markDone(date, h);                                 // 断点标记
    return { hour: h, diffs: diff.length };
  }));
  const diffRate = totalDiff(results) / totalOrders(results);
  if (diffRate > baseline * 2) alert({ type: 'RECON_ANOMALY', diffRate });   // 趋势告警
  return results;
}
```

**评分点**:
- 分片 + 断点幂等（失败只重跑该小时——SCN-NODE-682）。
- 渠道文件延迟日历（T+2 补对——重试日历语义）。
- 自动/人工分流边界显式（autoRule 声明——SCN-OPS-259）。
- 差异率趋势告警（对账监控——SCN-NODE-682）。
