---
title: [TST-213] 测试集随代码变更而变化（只跑受影响的 E2E），如何与分片结合？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-213：测试集随代码变更而变化（只跑受影响的 E2E），如何与分片结合？
**答**：
- 变更影响分析：diff 涉及的页面/组件 → 映射到覆盖它们的 E2E 用例（用例元数据声明覆盖面）。
- 先过滤受影响用例，再做分片均衡——两级缩减让 E2E 时长可控。
- 主干合并时全量跑兜底（PR 阶段跑受影响子集）。
- 映射表定期校准（用例新增后未登记覆盖面会漏跑）。

```javascript
const affected = mapDiffToTests(gitDiff());   // 用例元数据：covers: ['cart', 'checkout']
const bins = balance(affected.map(t => ({ id: t.id, ms: t.lastMs })), 4);
// 分片跑受影响子集；主干全量兜底
r
```
