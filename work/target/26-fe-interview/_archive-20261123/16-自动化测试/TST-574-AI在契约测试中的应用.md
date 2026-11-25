---
title: [TST-574] AI 在契约测试中的应用场景
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-574：AI 在契约测试中的应用场景

**答**：
- 结论：AI 可辅助「从 OpenAPI/Schema 生成契约测试骨架、生成边界与异常请求样例、解释契约变更影响」，但契约的真值仍是 schema 本身。
- 做法：用 schema 驱动生成正/异常请求与响应断言；契约变更时用 AI 汇总 breaking 影响并推荐需更新的用例；生成物仍需跑契约校验确认。
- 追问钩子：AI 生成的契约测试会不会和真实 schema 脱节？——不会，只要以 schema 为唯一真值源并在 CI 跑契约校验；AI 只生成「如何测」，不定义「测什么」。

```javascript
// 从 schema 字段生成边界请求样例（AI 辅助思路的确定性实现）
function boundarySamples(schema) {
  const out = [];
  for (const [field, def] of Object.entries(schema)) {
    if (def.type === 'number') out.push({ field, value: def.min - 1, kind: 'below-min' },
      { field, value: def.max + 1, kind: 'above-max' });
    if (def.type === 'string') out.push({ field, value: '', kind: 'empty' },
      { field, value: 'a'.repeat(def.maxLen + 1), kind: 'too-long' });
  }
  return out;
}
```
