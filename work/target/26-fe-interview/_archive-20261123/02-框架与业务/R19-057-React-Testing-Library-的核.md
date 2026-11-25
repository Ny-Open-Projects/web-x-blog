---
title: [R19-057] React Testing Library 的核心理念是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-057：React Testing Library 的核心理念是什么？
**答**：
- 以用户视角测试：像真实使用者一样通过角色、文本、label 查询元素，触发交互后断言结果。
- 不测试实现细节：不碰组件内部 state、不依赖 className，重构实现而不改行为时测试不应挂。
- 查询优先级按可访问性排序：getByRole 最优先，这与无障碍语义天然绑定。
- 配合 userEvent 模拟真实键盘鼠标事件序列。

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Counter from './Counter';

test('点击按钮后显示计数', async () => {
  render(<Counter />);

  // 用户视角：找到名为 加一 的按钮并点击
  await userEvent.click(screen.getByRole('button', { name: '加一' }));

  // 断言用户能看到的结果，而不是组件内部 state
  expect(screen.getByText('1')).toBeInTheDocument();
});
```
