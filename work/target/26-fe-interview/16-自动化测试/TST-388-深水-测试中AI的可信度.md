---
title: [TST-388] AI 测试工具产出「看起来对但错」的幻觉测试如何防？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-388：AI 测试工具产出「看起来对但错」的幻觉测试如何防？
**答**：
- 所有 AI 测试必须真实执行验证（不允许「生成即入库」）。
- 断言来源校验：断言的期望值来自需求文档/接口契约（可追溯），而非 AI 臆造。
- 变异验证兜底：注入已知 bug 验证测试会红（抽样）。
- 标记追溯：AI 生成测试打标，问题统计按来源归因。

```javascript
// 断言期望值可追溯
const expected = contract.orders.status.enum;   // 来自契约
expect(order.status).toBeOneOf(expected);       // 非 AI 自造
// AI 测试带 meta: { source: 'ai-gen', prompt: v12 }
r
```
