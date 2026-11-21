---
title: [TST-384] 测试结果如何反哺 AI 评审（减少重复意见）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-384：测试结果如何反哺 AI 评审（减少重复意见）？
**答**：
- 测试已覆盖的行为，AI 评审跳过重复建议（注入覆盖信息）。
- 测试失败未过的区域，AI 评审重点看（风险加权）。
- 历史：同类问题已被评审意见修过的，不再重复（意见库检索）。
- 效果度量：AI 意见与测试结果的重合率下降 = 联动生效。

```javascript
const ctx = { covered: await coverageOf(diffFiles), failed: failingTests(diffFiles) };
const prompt = `已覆盖区域（${ctx.covered}）不必重复评审风格问题；
失败区域（${ctx.failed}）重点评审正确性。`;
r
```
