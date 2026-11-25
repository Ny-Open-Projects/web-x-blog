---
title: [TST-862] 笔试：手写一个「AI 生成测试用例的确定性校验器」，校验 schema 与断言合法性
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-862：笔试：手写一个「AI 生成测试用例的确定性校验器」，校验 schema 与断言合法性
**答**：
- 需求：实现 validateAIGeneratedTests(tests) —— 校验 AI 生成的用例结构是否合法、断言是否非恒真、是否引用了不存在的 API。
- 规则：必填字段 name/cases/assertions；断言类型仅限 allowedTypes；检测恒真断言（expect(true)）；未通过则逐条给出错误。
- 边界：tests 非数组抛错；单个用例错误不阻断其他用例校验；返回每条的 valid 与全局 allValid。

```javascript
const ALLOWED = ['toBe', 'toEqual', 'toThrow', 'toHaveBeenCalled'];
function validateAIGeneratedTests(tests, knownApis = []) {
  if (!Array.isArray(tests)) throw new TypeError('tests 必须是数组');
  const results = tests.map((t, i) => {
    const errs = [];
    if (!t.name || !Array.isArray(t.cases) || !Array.isArray(t.assertions))
      errs.push('缺少必填字段 name/cases/assertions');
    for (const a of t.assertions || []) {
      if (!ALLOWED.includes(a.type)) errs.push(`非法断言类型 ${a.type}`);
      if (a.type === 'toBe' && a.value === true && a.actual === true)
        errs.push('检测到恒真断言 expect(true)');
      if (a.api && !knownApis.includes(a.api)) errs.push(`引用未知 API ${a.api}`);
    }
    return { index: i, valid: errs.length === 0, errors: errs };
  });
  return { allValid: results.every(r => r.valid), results };
}
console.log(validateAIGeneratedTests([
  { name: 'sum', cases: [[1,2]], assertions: [{ type: 'toBe', value: 3 }] },
  { name: 'bad', cases: [], assertions: [{ type: 'toBe', actual: true, value: true }] },
], ['sum'])); // 第二条 invalid（恒真）
```
**评分点**：
- 校验必填字段、断言类型白名单、恒真断言、未知 API 四类，覆盖 AI 生成常见问题。
- 单用例错误不阻断整体，返回逐条结果 + allValid。
- 非数组输入抛错，边界健壮。
- 能点出「AI 生成必须过确定性校验才能入库」这一工程化闸门思维。
