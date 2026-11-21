---
title: [TST-202] Playwright 里 worker 与 shard 的区别是什么？分别解决什么问题？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-202：Playwright 里 worker 与 shard 的区别是什么？分别解决什么问题？
**答**：
- worker：单机内并行进程数（workers: 4），共享 OS 资源，解决单机利用率。
- shard：多机切分（--shard），解决总时长超机器内并行上限。
- 两者相乘得总并发：总耗时 ≈ 总时长 / (workers × shards)。
- worker 间通过独立的浏览器上下文隔离（storageState 各自独立），shard 间连报告都要后合并——故障域完全不同。

```javascript
// playwright.config.ts
export default defineConfig({
  workers: process.env.CI ? 4 : 2,        // 单机并行
  fullyParallel: true,                     // 用例级分配（worker 内也自由调度）
  // shard 由 CLI --shard=1/4 控制，多机并行
});
r
```
