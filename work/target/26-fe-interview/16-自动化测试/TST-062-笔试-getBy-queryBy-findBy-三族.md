---
title: [TST-062] 笔试：getBy / queryBy / findBy 三族查询的选型实战
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-062：笔试：getBy / queryBy / findBy 三族查询的选型实战
**答**：
- 规则：getBy —— 断言「存在」时用（查不到立即抛错）；queryBy —— 断言「不存在」时用（返回 null 而不抛错，配 toBeNull）；findBy —— 元素异步出现时用（自带 waitFor 语义，默认 1s）。
- 高频错误：用 getBy 查「应该消失的元素」——红在查询而不是断言，错误信息误导；正确姿势 queryByText(...).toBeNull()。
- 异步场景：接口返回后渲染的列表用 findBy；loading 骨架消失用 waitFor + queryBy。

```jsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { vi, describe, it, expect } from 'vitest';
import OrderList from './OrderList';

describe('OrderList', () => {
  it('接口返回后渲染订单（findBy：异步出现）', async () => {
    vi.mocked(api.fetchOrders).mockResolvedValue([{ id: 'o1', title: '键盘' }]);
    render(<OrderList />);
    expect(await screen.findByText('键盘')).toBeInTheDocument();  // 自动等待出现
  });

  it('点击删除后条目消失（queryBy：断言不存在）', async () => {
    vi.mocked(api.fetchOrders).mockResolvedValue([{ id: 'o1', title: '键盘' }]);
    render(<OrderList />);
    await userEvent.click(await screen.findByRole('button', { name: '删除' }));
    await waitFor(() => expect(screen.queryByText('键盘')).toBeNull()); // 等到它消失
  });

  it('加载中显示骨架屏（同步存在断言用 getBy）', () => {
    vi.mocked(api.fetchOrders).mockReturnValue(new Promise(() => {})); // 永不 resolve
    render(<OrderList />);
    expect(screen.getByTestId('skeleton')).toBeInTheDocument();
  });
});
```
**评分点**：
- 三族语义对应关系准确（存在 getBy / 不存在 queryBy / 异步 findBy）。
- 「断言不存在」配 waitFor 处理消失有时序的场景。
- findBy 能说出底层就是 waitFor（DOM 变化 + 轮询）。
