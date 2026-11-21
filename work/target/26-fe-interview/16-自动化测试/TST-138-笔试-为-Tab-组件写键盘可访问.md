---
title: [TST-138] 笔试：为 Tab 组件写键盘可访问性测试（roving tabindex + ARIA）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-138：笔试：为 Tab 组件写键盘可访问性测试（roving tabindex + ARIA）
**答**：
- 场景：Tab 组件按 WAI-ARIA 规范：tablist/tab/tabpanel 角色、`aria-selected`、roving tabindex（列表内只有激活项 tabIndex=0）、左右箭头切换、Home/End 首尾跳转。测试就是验证这套 a11y 契约。
- 技巧：全部用 getByRole 定位（tab 组件的语义刚好是 role 体系）；userEvent.keyboard 模拟按键序列；顺带断言「面板内容与激活 tab 对应」。
- 这题的隐藏考点：a11y 测试的通用方法——role/aria 属性断言 + axe 自动扫描（见 TST-150），键盘测试是 a11y 里无法自动化的部分。

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Tabs from './Tabs';

function setup() {
  render(<Tabs items={['基本信息', '订单记录', '收货地址']} />);
  return userEvent.setup();
}

test('点击切换：aria-selected 与面板联动', async () => {
  const user = setup();
  expect(screen.getByRole('tab', { name: '基本信息' })).toHaveAttribute('aria-selected', 'true');

  await user.click(screen.getByRole('tab', { name: '订单记录' }));
  expect(screen.getByRole('tab', { name: '订单记录' })).toHaveAttribute('aria-selected', 'true');
  expect(screen.getByRole('tab', { name: '基本信息' })).toHaveAttribute('aria-selected', 'false');
  expect(screen.getByRole('tabpanel', { name: '订单记录' })).toBeInTheDocument();
});

test('roving tabindex：箭头移动焦点，Home/End 跳边界', async () => {
  const user = setup();
  const tabs = ['基本信息', '订单记录', '收货地址'].map(
    (n) => screen.getByRole('tab', { name: n }));

  tabs[0].focus();
  await user.keyboard('{ArrowRight}');
  expect(tabs[1]).toHaveFocus();
  expect(tabs[0]).toHaveAttribute('tabindex', '-1');   // 非激活项移出 Tab 序
  expect(tabs[1]).toHaveAttribute('tabindex', '0');    // roving tabindex

  await user.keyboard('{End}');
  expect(tabs[2]).toHaveFocus();
  await user.keyboard('{ArrowRight}');                  // 末尾循环回首个（规范允许 wrap）
  expect(tabs[0]).toHaveFocus();
  expect(screen.getByRole('tabpanel', { name: '基本信息' })).toBeInTheDocument();
});
```

**评分点**：
1. 用 role + aria 属性断言而非 DOM 结构（a11y 驱动的正确姿势）。
2. roving tabindex 语义验证：仅激活项 tabindex=0。
3. 箭头/Home/End 完整键盘行为，含边界循环。
4. 焦点断言用 toHaveFocus（jest-dom 提供）。
