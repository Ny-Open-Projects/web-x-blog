---
title: [TST-371] AI 探索性测试（Agent 自由探索发现 bug）的价值与控制？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-371：AI 探索性测试（Agent 自由探索发现 bug）的价值与控制？
**答**：
- 价值：覆盖「人想不到」的路径组合，发现崩溃/死循环/白屏类问题。
- 控制：探索范围限定（URL 白名单/操作预算/时长上限），产物是「发现清单」不是测试套件。
- 发现转化：有价值的发现转正为固定用例（先红后绿验证）。
- 成本核算：探索预算（token/时长）与产出比，低产出场景停用。

```javascript
const explore = await agentExplore({
  urls: allowlist, ops: 200, maxMinutes: 15,
  report: 'crash | blank | infinite-loop | console-error',
});
await promoteToTests(explore.findings);   // 转正：先红后绿
r
```
