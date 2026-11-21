---
title: [TST-011] 快照测试 toMatchSnapshot 适合什么场景？怎么避免它退化成摆设？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-011：快照测试 toMatchSnapshot 适合什么场景？怎么避免它退化成摆设？
**答**：
- 适用：序列化产物稳定且大——组件渲染结果、序列化后的 JSON、错误信息格式、CLI 输出。价值在「回归时一眼看出 diff」。
- 失效模式：快照太大（整个组件树几百行）时，review 根本不看，直接 `-u` 一按全过——快照变成「生成器」而不是测试。
- 防退化手段：控制快照粒度（只快照关键 DOM 片段/序列化对象）；CI 上禁止静默更新（`--ci` 模式下更新快照会直接失败）；PR 里 diff 必须人工确认。
- 与显式断言的关系：关键行为（金额、状态码、文案）用 toBe/toHaveText 显式断言，快照只做兜底防意外变化。
- 追问钩子：inline 快照把期望直接嵌进代码，review 时必然被看到，可读性优于外部文件。

```javascript
// 推荐写法：小粒度快照 + 关键行为显式断言
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import OrderCard from './OrderCard';

describe('OrderCard', () => {
  it('金额与状态正确（显式断言，优先）', () => {
    render(<OrderCard total={649} status="paid" />);
    expect(screen.getByText('¥649.00')).toBeInTheDocument();
    expect(screen.getByRole('status')).toHaveTextContent('已支付');
  });

  it('序列化摘要快照（小而关键）', () => {
    const summary = summarize({ id: 'o1', total: 649, status: 'paid' });
    expect(summary).toMatchSnapshot(); // __snapshots__/xx.snap 中仅几行
  });
});
```
