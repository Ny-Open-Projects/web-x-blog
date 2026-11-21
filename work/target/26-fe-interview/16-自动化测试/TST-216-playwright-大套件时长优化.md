---
title: [TST-216] E2E 总时长 90 分钟太慢，系统优化路径是什么？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-216：E2E 总时长 90 分钟太慢，系统优化路径是什么？
**答**：
- 先测量：分片利用率（各分片时长差异）、worker 空闲率——找到瓶颈再动。
- 减量：受影响子集策略 + 用例合并（同一旅程多断言合一条）。
- 提速：并行度（workers×shards）、跳过不必要等待（expect 自动等待替代 sleep）、API 预置数据替代 UI 操作。
- 架构：高频冒烟独立快速套件（< 5 分钟），全量套件夜间跑。

```javascript
// 数据预置走 API 而非 UI 点击（快 10 倍）
const goods = await request.post('/api/test/seed/goods', { data: { sku: 'E2E-1' } });
await page.goto(`/goods/${goods.sku}`);   // UI 只验证展示与交互
r
```
