---
title: [ARC-125] 组件测试架构（RTL / Vue Test Utils 最佳实践分层）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-125：组件测试架构（RTL / Vue Test Utils 最佳实践分层）？
**答**：
- 第一原则：测"用户视角的行为"（渲染了什么、点了会发生什么）而不是实现细节（state、内部方法）——RTL 的 query 优先级（getByRole > getByText > getByTestId）就是在强制这一点。
- 分层实践：展示组件测"props → 渲染输出 + 交互回调"；hooks 用 renderHook 测状态机；页面级集成测试组合 msw 数据验证整链路（加载/错误/空态三态必测）。
- 反模式清单：不测快照式 DOM 结构（改样式就崩）、不 mock 子组件（除非边界：路由/Portal）、不在测试里 sleep（用 waitFor/userEvent）。
- 可访问性语义顺带保障：用 getByRole 写查询天然推动 a11y 语义补齐。

```typescript
// 组件测试示例（React Testing Library + msw）
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { http, HttpResponse } from 'msw';

test('提交表单成功后跳转详情页', async () => {
  // Arrange：msw 拦截网络，返回契约数据
  server.use(http.post('/api/orders', () => HttpResponse.json({ id: 'ord_1' })));
  const onCreated = vi.fn();
  render(<OrderForm onCreated={onCreated} />);

  // Act：像用户一样操作（不用 fireEvent 模拟，用 userEvent 走真实事件链）
  await userEvent.type(screen.getByRole('textbox', { name: '收货地址' }), '北京市朝阳区');
  await userEvent.click(screen.getByRole('button', { name: '提交订单' }));

  // Assert：只断言用户可见的结果
  expect(await screen.findByText('下单成功')).toBeVisible();
  expect(onCreated).toHaveBeenCalledWith(expect.objectContaining({ id: 'ord_1' }));
});
// 三态覆盖约定：每个数据组件至少有 加载中 / 错误 / 空数据 三条用例
test('接口报错展示错误态与重试', async () => {
  server.use(http.get('/api/orders', () => HttpResponse.error()));
  render(<OrderList />);
  expect(await screen.findByRole('alert')).toHaveTextContent('加载失败');
  await userEvent.click(screen.getByRole('button', { name: '重试' }));
});
```
