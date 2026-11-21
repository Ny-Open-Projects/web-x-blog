---
title: [NODE-616] Node 服务的大批量写（批量插入/更新）优化如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-616：大批量写优化
**答**:
- 批量插入：multi-row INSERT（一条 SQL 多 values——比循环单条快 10x+）、COPY（PG 大量数据最快路径——CSV 流式 COPY）、batchSize 调优（500~1000 行/批——参数化语句上限与事务大小平衡）、upsert 批量（ON CONFLICT 批量——幂等批量插入）。
- 事务与锁：分批事务（万行拆 50 批——锁范围小、可断点续跑 NODE-335）、锁影响评估（大批写锁表行——错峰执行/只读副本）、失败恢复（批次断点——从失败批重跑）。
- 读写保护：限速执行（大批写对在线查询的影响——限速+错峰 NODE-437）、监控（写入期间在线 P95——影响可观测）。
- 优化谱系：先索引后数据（大批导入前删非必需索引后重建——离线场景）、批量更新（UPDATE FROM VALUES 批量——比循环 update 快）、分区表（大表批量写——分区裁剪）。
- 验证：吞吐对比（优化前后 rows/s——量化收益）、在线影响（写期间在线查询 P95 变化）。
```javascript
// 批量插入模板
for (const batch of chunk(rows, 1000)) {
  const values = batch.flatMap((r, i) => `($${i*3+1},$${i*3+2},$${i*3+3})`);
  await tx.query(`insert into t(a,b,c) values ${values.join(',')}
    on conflict (a) do nothing`, batch.flatMap(Object.values));  // 批量 upsert
  await sleep(50);                                               // 限速保护
}
```
