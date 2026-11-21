---
title: [TST-101] Playwright 的并行与分片（sharding）怎么做？怎么保证并发安全？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-101：Playwright 的并行与分片（sharding）怎么做？怎么保证并发安全？
**答**：
- 两层并行：文件级 worker 并行（`workers: 4`，多个 worker 进程各开各的 BrowserContext，同时跑不同文件）；CI 分片 `--shard=1/3 --shard=2/3`，把用例集切到多台机器跑，GitHub Actions matrix 一行配置，报告可合并（`merge-reports`）。
- 并发安全三条底线：① 每个用例独立 BrowserContext（Playwright 默认）——cookies/localStorage 互不污染；② 测试数据隔离——造数用唯一前缀（`test-${Date.now()}-${random}`），或用 API 造数后 API 删数（fixture teardown）；③ 避免用例间依赖顺序——每个用例自己 setup 自己的数据，别靠"上一个用例创建的订单"。
- 共享资源冲突：同一后端数据库、同一测试账号、第三方 mock 服务都是共享资源；要么按 worker 分账号（`process.env.TEST_WORKER_INDEX`），要么后端提供事务回滚/独立 schema。
- 速度盘算：本地 4 worker，CI 按机器数分片 + `fullyParallel: true`；单文件内也可 `test.describe.configure({ mode: 'parallel' })`（前提仍是数据隔离）。
- 追问钩子：worker 崩溃泄漏怎么办？——`process.env.TEST_WORKER_INDEX` 做资源命名空间，`test.afterAll` 兜底清理，配合后端定时清扫任务。

```javascript
// playwright.config.ts
export default defineConfig({
  fullyParallel: true,
  workers: process.env.CI ? 4 : 2,
  // CI 分片命令：
  // npx playwright test --shard=${{ matrix.shard }}/${{ matrix.total }}
});

// 数据隔离：按 worker 唯一命名
import { test as base } from '@playwright/test';
export const test = base.extend({
  testUser: async ({}, use) => {
    const name = `e2e-w${process.env.TEST_WORKER_INDEX}-${Math.random().toString(36).slice(2, 8)}`;
    await use(name);
    // teardown：用例结束清理自己造的数据
  },
});
```
