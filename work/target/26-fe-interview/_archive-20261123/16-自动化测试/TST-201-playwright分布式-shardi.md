---
title: [TST-201] Playwright 的 sharding 分布式执行是怎么工作的？如何保证分片均匀？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-201：Playwright 的 sharding 分布式执行是怎么工作的？如何保证分片均匀？
**答**：
- 按测试文件（默认）或 --shard=i/n 把用例切成 n 份，各自在独立机器/容器跑，报告用 merge-reports 合并。
- 按文件切分的坑：大文件集中导致某分片巨慢——用 --fully-parallel 让按用例粒度分配。
- 均匀性优化：先跑一次收集每用例耗时，按「贪心装箱」把长用例均摊到各分片。
- 分片数不是越多越好：环境准备/数据初始化开销占比会上升，通常 4-8 片收益最高。

```javascript
# CI 中分片执行 + 报告合并
npx playwright test --shard=1/4 --reporter=blob
npx playwright test --shard=2/4 --reporter=blob
npx playwright merge-reports --reporter=html blob-report/
r
```
