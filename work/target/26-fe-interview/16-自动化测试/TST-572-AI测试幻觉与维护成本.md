---
title: [TST-572] AI 生成测试的幻觉与维护成本怎么破
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-572：AI 生成测试的幻觉与维护成本怎么破

**答**：
- 结论：幻觉根源是「缺乏上下文 + 概率生成」；对策是「给足上下文（代码/schema/规范）+ 结构化输出 + 强制校验 + 人工评审 + 持续反馈」。
- 维护成本来自「生成物不稳定、风格不一」；用统一模板/Prompt 版本化 + 入库前规范化，把 AI 产出拉齐到团队标准。
- 追问钩子：AI 生成的断言引用了不存在的字段怎么办？——入库闸门做「断言字段是否存在于类型/schema」的静态校验，不存在直接拒绝并记录 Prompt 改进点。

```javascript
// 幻觉校验：断言中的字段是否真实存在于 schema
function checkAssertionFields(code, schemaFields) {
  // 提取 expect(res.xxx) / obj.yyy 中被引用的属性名
  const used = [...code.matchAll(/\.(\w+)/g)].map(m => m[1]);
  const unknown = [...new Set(used)].filter(f => !schemaFields.includes(f));
  return { hasHallucination: unknown.length > 0, unknown };
}
// 入库闸门：把幻觉校验接入生成用例审查
function aiCaseGate(cases, schema) {
  return cases.map(c => {
    const check = checkAssertionFields(c.code, schema.fields);
    return { id: c.id, ...check, blocked: check.hasHallucination };
  });
}
const schema = { fields: ['userId', 'name', 'email'] };
console.log(aiCaseGate([
  { id: 1, code: 'expect(res.userId).toBe(1)' },
  { id: 2, code: 'expect(res.userName).toBe(1)' }, // 幻觉字段
], schema));
```
