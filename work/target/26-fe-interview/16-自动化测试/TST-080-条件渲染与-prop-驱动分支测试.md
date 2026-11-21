---
title: [TST-080] 条件渲染组件怎么测？prop 驱动的分支怎么组织用例？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-080：条件渲染组件怎么测？prop 驱动的分支怎么组织用例？
**答**：
- 分支组织：每个「用户可观察的状态」一条用例（loading/empty/error/loaded），用 it.each 表驱动 prop 组合，断言对应分支元素存在 + 其他分支不存在（双向断言防「永远显示 loading」这类 bug）。
- 双向断言的价值：只断言「error 图标在」漏掉「loading 还在」的 bug；配对 queryBy(...).toBeNull() 成本低收益高。
- 数值边界：badge 溢出（>99 显示 99+）这类逻辑单独边界用例；布尔 prop 的 false 缺省也要测（漏传与显式 false 等价性）。
- 追问钩子：条件渲染的测试成本远低于逻辑组件——多数用 it.each 一次列完，不要一条分支一个 describe 撑篇幅。

```jsx
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import StatusBadge from './StatusBadge';

describe('StatusBadge 分支表', () => {
  it.each([
    ['loading', true, false, '加载中…'],
    ['error', false, true, '加载失败'],
    ['paid', false, false, '已支付'],
  ])('%s 态：spinner=%j error=%j 文案=%s', (status, spinner, error, text) => {
    render(<StatusBadge status={status} />);
    expect(screen.queryByTestId('spinner')).toBe(spinner ? document.querySelector('x') ?? screen.queryByTestId('spinner') : null);
    spinner ? expect(screen.getByTestId('spinner')).toBeInTheDocument()
            : expect(screen.queryByTestId('spinner')).toBeNull();
    error ? expect(screen.getByTestId('error-icon')).toBeInTheDocument()
          : expect(screen.queryByTestId('error-icon')).toBeNull();
    expect(screen.getByText(text)).toBeInTheDocument();
  });

  it('计数超过 99 显示 99+', () => {
    render(<StatusBadge status="paid" count={150} />);
    expect(screen.getByText('99+')).toBeInTheDocument();
  });
});
```
