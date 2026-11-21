---
title: [TST-079] jest-dom 提供了哪些高频断言？怎么接入 Vitest？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-079：jest-dom 提供了哪些高频断言？怎么接入 Vitest？
**答**：
- 接入：setup 文件 `import '@testing-library/jest-dom/vitest'`（Vitest 专用入口），之后所有 expect 获得 DOM 扩展 matcher；TS 下类型自动注入。
- 高频 matcher：toBeInTheDocument / toBeVisible（可见性含 aria-hidden 与样式隐藏）、toBeDisabled/toBeEnabled、toHaveValue、toBeChecked、toHaveAttribute、toHaveClass、toHaveTextContent、toHaveFocus、toBePartiallyChecked（半选）。
- 价值：失败信息可读——expect(el).toBeDisabled() 失败时直接告诉你元素可交互，比 expect(el.disabled).toBe(false) 的布尔差异友好得多。
- 易混点：toBeInTheDocument 只查「在 DOM 里」，toBelVisible 还考虑 display:none/visibility/size；toHaveTextContent 是子串匹配（整串要 `^...$` 或 toHaveTextContent(str, { trimAndCollapse })）。

```typescript
// vitest.setup.ts
import '@testing-library/jest-dom/vitest';

// 用法示例
import { render, screen } from '@testing-library/react';
render(<input type="checkbox" checked disabled aria-label="同意协议" />);

const box = screen.getByRole('checkbox', { name: '同意协议' });
expect(box).toBeDisabled();
expect(box).toBeChecked();
expect(box).toHaveAttribute('type', 'checkbox');

// 可见性 vs 存在性
render(<div style={{ display: 'none' }} data-testid="hidden">x</div>);
expect(screen.getByTestId('hidden')).toBeInTheDocument();   // 存在
expect(screen.getByTestId('hidden')).not.toBeVisible();     // 但不可见
```
