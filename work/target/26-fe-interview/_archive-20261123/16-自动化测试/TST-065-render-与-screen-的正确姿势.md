---
title: [TST-065] RTL 的 render / screen / cleanup 正确姿势是什么？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-065：RTL 的 render / screen / cleanup 正确姿势是什么？
**答**：
- render 返回解构（container、rerender、unmount）应尽量少用；查询一律走 `screen`——它绑定当前活跃的 container，测试代码与「用户视角」对齐，且多个 render 时自动指向最新。
- cleanup：RTL 在 Vitest/Jest globals 环境下自动 afterEach cleanup（检测到 globalThis.afterEach 时开启）；若 globals: false，需手动 `afterEach(cleanup)`，否则 DOM 叠加导致 getBy 多元素报错。
- rerender：测 props 变化驱动的行为（loading → loaded），unmount：验证卸载清理（事件监听、定时器）。
- debug()：`screen.debug()` 打印当前 DOM 帮助排查；`render(...).baseElement` 用于断言整体。
- 追问钩子：`screen.getByText` 报「multiple elements」时，先用 getByRole 缩窄而不是换 class——通常意味着该文案出现在多个语义位置。

```jsx
import { render, screen, cleanup } from '@testing-library/react';
import { afterEach } from 'vitest';
// globals: false 时需要手动：
afterEach(() => cleanup());

test('props 变化驱动 rerender', () => {
  const { rerender, unmount } = render(<OrderItem status="loading" />);
  expect(screen.getByTestId('skeleton')).toBeInTheDocument();

  rerender(<OrderItem status="paid" />);            // 同组件树更新 props
  expect(screen.getByText('已支付')).toBeInTheDocument();

  unmount();                                        // 验证卸载清理
  expect(document.querySelectorAll('[data-testid]')).toHaveLength(0);
});
```
