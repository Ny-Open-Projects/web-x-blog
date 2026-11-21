---
title: [TST-077] 用 role 与 accessible name 写测试，怎么顺带保住可访问性？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-077：用 role 与 accessible name 写测试，怎么顺带保住可访问性？
**答**：
- 原理：getByRole 按 ARIA 角色表匹配，元素必须有正确语义（button/nav/dialog）且可感知（非 aria-hidden）；accessible name 来自 label、aria-label、内嵌文本。查询失败往往就是 a11y 缺陷本身。
- 常见暴露的 a11y 问题：div 当按钮（无 button role，需 onClick + role/tabIndex 才查得到）、icon-only 按钮无 aria-label、label 未关联 input。
- 收益：测试即 a11y 检查——用 role 写测试的团队，组件语义化水平天然更高；再配 jest-dom 的 toHaveAccessibleName 精确断言。
- 追问钩子：axe（accessibility checker）可以加到测试里做全页扫描，role 查询是「点」，axe 是「面」，组合覆盖。

```jsx
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';

describe('a11y 驱动的测试', () => {
  it('图标按钮必须有 accessible name', () => {
    render(<button aria-label="关闭通知"><svg /></button>);
    expect(screen.getByRole('button', { name: '关闭通知' })).toBeInTheDocument();
    // 如果实现漏了 aria-label，这行直接红 —— a11y 缺陷被测试拦住
    expect(screen.getByRole('button', { name: '关闭通知' })).toHaveAccessibleName('关闭通知');
  });

  it('导航与主区域语义完整', () => {
    render(<AppShell />);
    expect(screen.getByRole('navigation', { name: '主导航' })).toBeInTheDocument();
    expect(screen.getByRole('main')).toBeInTheDocument();
  });

  it('表单控件与 label 关联', () => {
    render(<><label htmlFor="phone">手机号</label><input id="phone" /></>);
    expect(screen.getByRole('textbox', { name: '手机号' })).toBeInTheDocument();
  });
});
```
