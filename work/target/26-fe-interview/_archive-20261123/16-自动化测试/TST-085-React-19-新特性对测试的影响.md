---
title: [TST-085] React 19 的新特性对组件测试有什么影响？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-085：React 19 的新特性对组件测试有什么影响？
**答**：
- act 集成：RTL v16+ 直接用 React 19 的 act，导出路径从 react-dom/test-utils 迁移到 react（旧导出被移除），升级后要全局替换 act 来源。
- async/Actions：表单 action（useActionState/useTransition）让提交变成异步——测试要用 findBy/waitFor 等待 action 完成，而不是假设同步 setState。
- use(Promise)：组件里直接 await 数据（配合 Suspense）——测试需把异步数据请求与 Suspense fallback 一起测（findBy 等 resolve）。
- ref/forwardRef 简化、Context 替代 forwardRef——测试查询不受影响，但 mock 三方库时注意其内部也用新 API。
- ErrorBoundary 与 window.onerror：未捕获错误会上抛到 window，测试环境可能触发 vitest 全局报错——需要压噪或显式断言。

```jsx
// React 19 action 表单测试
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('提交走 action 异步完成后显示成功', async () => {
  const user = userEvent.setup();
  render(<SignupForm action={async (fd) => { await save(fd); }} />);
  await user.type(screen.getByLabelText('邮箱'), 'a@b.c');
  await user.click(screen.getByRole('button', { name: '注册' }));

  // action 是异步的：不能同步断言，必须等待
  await waitFor(() => expect(screen.getByText('注册成功')).toBeInTheDocument());
});
// act 从 react 导入（React 19）：
import { act } from 'react';
```
