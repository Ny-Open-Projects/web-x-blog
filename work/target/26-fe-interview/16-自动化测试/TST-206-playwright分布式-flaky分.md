---
title: [TST-206] 分布式下 flaky 用例为什么更常见？如何定位？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-206：分布式下 flaky 用例为什么更常见？如何定位？
**答**：
- 放大效应：单机偶发 × 分片数 × worker 数，同一用例在不同环境表现不同。
- 常见根因：共享后端数据冲突、单机资源超卖、时区/ locale 差异。
- 定位手段：trace + 分片标记重跑失败分片；对嫌疑用例单独在单机复跑对照。
- 治理：隔离区（quarantine）+ 环境一致性检查（时钟/数据命名空间）。

```javascript
// 失败自动重试仅限分布式环境，且记录 shard 便于归因
export default defineConfig({
  retries: process.env.CI ? 2 : 0,
  reporter: [['blob', { outputDir: `blob-report/shard-${process.env.SHARD_INDEX}` }]],
});
r
```
