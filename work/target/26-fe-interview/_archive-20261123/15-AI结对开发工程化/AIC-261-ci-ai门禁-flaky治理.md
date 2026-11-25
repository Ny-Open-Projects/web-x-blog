---
title: [AIC-261] AI 门禁如何辅助 flaky 测试治理？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-261：AI 门禁如何辅助 flaky 测试治理？
**答**：
- 自动归因：flaky 用例失败时 AI 聚合历史失败模式（超时/并发/环境），输出归因假设与置信度。
- 隔离执行：疑似 flaky 用例自动移入隔离区（quarantine），不阻塞主干但计入治理看板。
- 修复辅助：AI 按归因类型给修复方案（加等待改轮询/隔离共享状态/固定时钟）。
- 退出机制：隔离区用例连续 20 次通过自动回归主干，防止「隔离即遗忘」。

```javascript
async function flakyGuard(test: Test, runs: Run[]) {
  const cause = await diagnose(runs);           // timeout/concurrency/env
  if (cause.confidence > 0.7) quarantine(test, { exit: '20 连绿自动回归' });
  return suggestFix(cause);                     // 轮询替代 sleep / 固定时钟
}
r
```
