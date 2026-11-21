---
title: [TST-020] test.each 参数化测试怎么写？什么场景值得参数化？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-020：test.each 参数化测试怎么写？什么场景值得参数化？
**答**：
- 价值：同一逻辑多组输入输出（格式化、校验、边界值）用一张表驱动，减少复制粘贴的 it；失败时报告能精确指出哪一行数据。
- 形式：数组表 `%s` 占位命名 / 模板字符串表格两种写法；异步用 `it.each(...).concurrent`。
- 适用判断：输入→输出的映射「同构」（逻辑一致）才参数化；如果不同分支行为差异大（要 mock 不同东西），拆成独立 it 更清晰。
- 边界数据优先：空串、0、负数、超长、Unicode、非法输入——参数化表正是边界值分析的落地形式。

```javascript
import { describe, it, expect } from 'vitest';
import { formatMoney } from './money';

describe('formatMoney 边界表', () => {
  // 表格写法：首行是参数名，%s 用于用例命名
  it.each([
    ['零', 0, '¥0.00'],
    ['普通', 1234.5, '¥1,234.50'],
    ['负数', -20, '-¥20.00'],
    ['千分位', 1234567.891, '¥1,234,567.89'],
    ['非法', NaN, '¥0.00'],
  ])('%s: %f -> %s', (name, input, expected) => {
    expect(formatMoney(input)).toBe(expected);
  });
});
```
