---
title: [TST-251] Storybook 的测试能力（interaction tests/play fn）如何用好？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-251：Storybook 的测试能力（interaction tests/play fn）如何用好？
**答**：
- story 是「可复用测试夹具」：story + play 函数 = 交互测试（复用 story 的状态准备）。
- play 函数用 testing-library 断言，与单测同一套心智。
- CI 跑 test-storybook 全量 story（含 play），失败截图进报告。
- story 组织即测试组织：每个交互状态一个 story（default/loading/error），天然形成状态覆盖矩阵。

```javascript
export const WithError: Story = {
  args: { error: '加载失败' },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    await expect(canvas.getByRole('alert')).toHaveTextContent('加载失败');
    await userEvent.click(canvas.getByRole('button', { name: '重试' }));
  },
};
r
```
