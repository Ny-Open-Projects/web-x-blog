---
title: [TST-914] 把 200 个 Jest 快照迁移到 Vitest，如何保证「零静默回归」地平滑迁移？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-914：把 200 个 Jest 快照迁移到 Vitest，如何保证「零静默回归」地平滑迁移？
**答**：
- 结论：迁移分三步——先让两者快照格式对齐（序列化器一致），再在 CI 双跑对比，最后按目录灰度切换并保留回滚开关。
- 格式差异：Jest 的 __snapshots__/*.snap 头注释、转义规则与 Vitest 不同，需用官方 snapshotFormat 配置对齐后再迁移。
- 零静默：迁移期同一用例两框架各跑一次，diff 非空则拦截，禁止 update 一把梭。
- 追问钩子：迁移后发现 3 个快照 diff 但业务代码没动，你如何判断是序列化差异还是真回归？

```javascript
// vitest.config.ts —— 迁移期对齐 Jest 序列化格式
import { defineConfig } from 'vitest/config';
export default defineConfig({
  test: {
    snapshotFormat: { escapeString: true, printBasicPrototype: true },
    // 与 Jest 的 toMatchSnapshot 行为对齐，减少假 diff
  },
});
// 迁移期双跑校验脚本（伪代码）
const diffs = await compare(
  runWith('jest', '--ci'),
  runWith('vitest', '--run')
);
if (diffs.length) {
  console.error('迁移期出现 diff，禁止合并:', diffs.map(d => d.file));
  process.exit(1);
}
```
