---
title: [NODE-183] 设计一个多云存储同步服务？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-183：设计一个多云存储同步服务？
**答**：
- 场景：主云（OSS）为权威，同步到备份云（COS/S3）做容灾或迁移；两种触发：**事件驱动实时同步**（上传回调）+ 定时全量对账兜底。
- 增量判定：HEAD 两端对比 etag/size，一致跳过；不一致按策略（主为准）覆盖。
- 传输优化：大文件走**服务端拷贝**（云间直拷不过本机）；小文件流式中转并限速，避免打满出口带宽。
- 可靠性：失败重试 3 次进死信，下轮对账兜底；sync_lag（主备时间差）与失败率是核心指标。

```javascript
async function syncObject(objKey) {
  const [primary, backup] = await Promise.all([
    oss.head(objKey),
    cos.head(objKey).catch(() => null),
  ]);
  if (backup && backup.etag === primary.etag && backup.size === primary.size) return 'skip';
  if (primary.size > 1024 * 1024 * 1024) {
    await cos.copyFrom(oss.publicUrl(objKey));   // 大文件云间直拷，不过本机
  } else {
    await limiter.schedule(() =>                 // 限速，保护出口带宽
      cos.putStream(objKey, (await oss.getStream(objKey)).stream));
  }
  await db.syncLog.create({ data: { objKey, etag: primary.etag, ts: Date.now() } });
  return 'synced';
}
// 对账任务：每日 list 主云分页比对备份云 → 漏掉的重新入队；失败 3 次进死信表
```
