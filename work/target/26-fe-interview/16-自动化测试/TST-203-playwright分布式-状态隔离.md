---
title: [TST-203] 分布式执行下测试数据如何隔离，避免分片间互相污染？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-203：分布式执行下测试数据如何隔离，避免分片间互相污染？
**答**：
- 每 shard/worker 独立命名空间：数据库 schema/测试用户/文件目录都带 shard id 后缀。
- 禁止共享可变数据（同一批测试订单被两个分片同时操作）——数据工厂按 worker 发号。
- globalSetup 每分片独立执行时注意幂等（建表用 IF NOT EXISTS）。
- 清理策略：teardown 只清自己命名空间，防误删他分片数据。

```javascript
test.beforeAll(async ({ browser }, workerInfo) => {
  const ns = `shard${process.env.SHARD_INDEX ?? 0}-w${workerInfo.workerIndex}`;
  await seedData({ namespace: ns });       // 数据工厂按命名空间发号
  process.env.TEST_NS = ns;
});
r
```
