---
title: [TST-965] 笔试：手写「AI 用例断言有效性度量器」——识别 expect(true).toBe(true) 式空断言
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-965：笔试：手写「AI 用例断言有效性度量器」——识别 expect(true).toBe(true) 式空断言
**答**：
- 需求：实现 measureAssertions(assertions)，assertions 为 [{ actual, expected, mode }] 字符串描述数组。
- 规则：空断言（actual 为常量 true/false/数字字面量）判为无效；mode 为 'snapshot' 且内容为空判为无效；其余有效。返回 { valid, invalid, validityRate }。
- 边界：空数组 validityRate 记 0；expected 为 undefined 视为无效（等于没断言）。

```javascript
function measureAssertions(assertions) {
  const valid = [], invalid = [];
  const isLiteral = s => /^(true|false|\d+|'[^']*'|\d+\.\d+)$/.test(String(s).trim());
  for (const a of assertions) {
    let reason = null;
    if (isLiteral(a.actual)) reason = '对常量断言，恒真/恒假';
    else if (a.expected === undefined) reason = '缺少期望值';
    else if (a.mode === 'snapshot' && !a.expected) reason = '空快照断言';
    (reason ? invalid : valid).push(reason ? { ...a, reason } : a);
  }
  const total = assertions.length;
  return { valid: valid.length, invalid, validityRate: total ? +(valid.length / total).toFixed(2) : 0 };
}
console.log(measureAssertions([
  { actual: 'true', expected: 'true' },              // 无效
  { actual: 'order.price', expected: '9900' },        // 有效
  { actual: 'res.code', expected: undefined },        // 无效
])); // { valid:1, invalid:[...2条], validityRate:0.33 }
```
**评分点**：
- 能识别对常量 true/false/数字字面量的空断言。
- expected 为 undefined 与空快照判为无效。
- validityRate 计算正确，空数组记 0。
- invalid 带 reason，便于给 AI 生成结果反馈。
