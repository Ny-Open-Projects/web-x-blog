---
title: [TST-071] Portal（弹窗/抽屉）组件怎么测？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-071：Portal（弹窗/抽屉）组件怎么测？
**答**：
- 核心：Portal 渲染到 container 外（document.body），不能用 render 返回的 container 查询——必须用 screen（绑定 document.body）查询；弹窗内容查不到时先确认挂载点。
- 断言面：开关（open 后 toBeInTheDocument / 关闭后 queryBy toBeNull）、Escape 关闭、遮罩点击关闭、焦点管理（打开后焦点进入弹窗、关闭后归还触发器）。
- 多弹窗与 z-index 无需关心（实现细节）；aria-modal/role="dialog" + aria-label 让 getByRole('dialog') 生效，顺带验证 a11y。
- 卸载清理：unmount 后 body 里不应残留弹窗节点（Portal 组件常见 bug）。

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import ConfirmDialog from './ConfirmDialog';

describe('ConfirmDialog (Portal)', () => {
  it('open 时渲染到 body 且可关闭（Escape）', async () => {
    const user = userEvent.setup();
    const onClose = vi.fn();
    render(<ConfirmDialog open onClose={onClose} title="确认删除" />);

    // Portal 在 container 外，screen 从 document.body 查询
    const dialog = screen.getByRole('dialog', { name: '确认删除' });
    expect(dialog).toBeInTheDocument();

    await user.keyboard('{Escape}');
    expect(onClose).toHaveBeenCalled();
  });

  it('关闭后 body 无残留节点', () => {
    const { rerender, unmount } = render(<ConfirmDialog open onClose={vi.fn()} title="x" />);
    rerender(<ConfirmDialog open={false} onClose={vi.fn()} title="x" />);
    expect(screen.queryByRole('dialog')).toBeNull();
    unmount();
    expect(document.body.querySelectorAll('[role="dialog"]')).toHaveLength(0); // 卸载清理
  });
});
```
