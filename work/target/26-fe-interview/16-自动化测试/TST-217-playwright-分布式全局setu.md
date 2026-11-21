---
title: [TST-217] 多分片下 globalSetup 重复执行的坑与正确姿势？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-217：多分片下 globalSetup 重复执行的坑与正确姿势？
**答**：
- globalSetup 每个 shard 都会跑——建数据要幂等，或改为「一个分片负责 seed，其余等待就绪」。
- 更干净：seed 独立成 CI job（在测试 job 之前），各分片只消费。
- 就绪协调用对象存储/Redis 标记（seed-done 键），避免轮询竞态。
- 清理同理：统一在收尾 job 做，或按命名空间各自清理。

```javascript
// globalSetup 幂等 seed
async globalSetup() {
  await pg.query(`CREATE TABLE IF NOT EXISTS e2e_goods (...)`);
  await pg.query(`INSERT INTO e2e_goods ... ON CONFLICT (sku) DO NOTHING`);
}
r
```
