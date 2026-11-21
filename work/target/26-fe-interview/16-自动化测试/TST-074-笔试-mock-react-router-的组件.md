---
title: [TST-074] 笔试：为依赖 react-router 的组件配置测试环境并测试跳转
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-074：笔试：为依赖 react-router 的组件配置测试环境并测试跳转
**答**：
- 需求：组件内有 `<Link>`、`useNavigate`、`useParams`，单测直接渲染会报 router context 缺失；要测「点击跳转到 /pay/:id」与「读取路由参数」。
- 两种方案：① 包一层真实 Router（createMemoryRouter + RouterProvider）——集成度最高，能断言 URL 变化；② vi.mock react-router-dom 的 useNavigate/useParams——只测回调行为，更轻。
- 推荐优先方案 ①：memory router 无需真实浏览器，断言 `router.state.location` 或渲染 TestLocation 组件读 URL。

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { createMemoryRouter, RouterProvider } from 'react-router';
import { describe, it, expect } from 'vitest';
import OrderDetail from './OrderDetail';
import PayPage from './PayPage';

function renderWithRouter(initialPath) {
  const router = createMemoryRouter(
    [
      { path: '/order/:id', element: <OrderDetail /> },
      { path: '/pay/:id', element: <PayPage /> },
    ],
    { initialEntries: [initialPath] },
  );
  return { router, ...render(<RouterProvider router={router} />) };
}

describe('OrderDetail 路由行为', () => {
  it('读取路由参数并渲染', () => {
    renderWithRouter('/order/o-100');
    expect(screen.getByText('订单号：o-100')).toBeInTheDocument();
  });

  it('点击去支付跳转到 /pay/:id', async () => {
    const user = userEvent.setup();
    const { router } = renderWithRouter('/order/o-100');
    await user.click(screen.getByRole('link', { name: '去支付' }));
    expect(router.state.location.pathname).toBe('/pay/o-100');  // 断言 URL 变化
    expect(await screen.findByText('收银台')).toBeInTheDocument();
  });
});
```
**评分点**：
- createMemoryRouter/RouterProvider 搭真实路由环境，能断言 location。
- useParams 行为用真实 router 传参验证而不是 mock。
- 备选方案 vi.mock useNavigate 也说得清（只需断言回调时的轻量场景）。
