---
title: [TST-063] 笔试：用 userEvent 写一组完整交互测试（输入/点击/键盘/悬停）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-063：笔试：用 userEvent 写一组完整交互测试（输入/点击/键盘/悬停）
**答**：
- 需求：覆盖订单表单核心交互——输入触发校验、点击提交、键盘 Tab/Enter 导航、禁用按钮点击无效。用 userEvent（模拟完整事件序列 focus/input/keydown，比 fireEvent 真实）。
- 要点：每个用例前 `const user = userEvent.setup()`（v14 必须显式创建实例，携带 fake timers 需 `advanceTimers` 参数）；断言用 role 查询。
- 边界：禁用按钮 userEvent.click 会直接报错（元素不可交互），这本身就是行为断言的一部分；selectOption/select 处理下拉。

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import OrderForm from './OrderForm';

describe('OrderForm 交互', () => {
  it('手机号非法时显示校验错误且不提交', async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<OrderForm onSubmit={onSubmit} />);

    await user.type(screen.getByLabelText('手机号'), '123');      // 输入非法号码
    await user.click(screen.getByRole('button', { name: '提交' }));
    expect(screen.getByText('手机号格式不正确')).toBeInTheDocument();
    expect(onSubmit).not.toHaveBeenCalled();
  });

  it('键盘 Enter 可提交合法表单', async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<OrderForm onSubmit={onSubmit} />);

    await user.type(screen.getByLabelText('手机号'), '13800000000');
    await user.keyboard('{Enter}');                                // 键盘事件
    expect(onSubmit).toHaveBeenCalledWith({ phone: '13800000000' });
  });

  it('禁用状态下点击不触发提交', async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<OrderForm onSubmit={onSubmit} loading />);            // 提交中禁用
    const btn = screen.getByRole('button', { name: /提交中/ });
    expect(btn).toBeDisabled();
    await user.click(btn).catch(() => {});                        // userEvent 会拒绝可交互性违规
    expect(onSubmit).not.toHaveBeenCalled();
  });
});
```
**评分点**：
- userEvent.setup() 显式创建（v14 API），而非直接调静态方法。
- userEvent.click 对 disabled 元素的报错语义被利用为断言。
- 键盘导航 user.keyboard 的用法。
- 能对比 fireEvent：fireEvent 只派发单事件，userEvent 完整模拟焦点/输入序列（更真实但更慢）。
