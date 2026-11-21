---
title: [TST-193] Storybook 驱动的测试体系怎么搭？story 即用例的实践
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-193：Storybook 驱动的测试体系怎么搭？story 即用例的实践
**答**：
- 理念：每个组件先写 story（所有视觉状态：默认/loading/错误/空态/边界数据），story 就是「组件的活文档 + 测试夹具」——测试、视觉回归、设计走查都基于同一套 story，一次编写多处复用。
- 三层测试挂在 story 上：① 视觉回归——每个 story 截一张基线图（Storybook + Playwright `test.stories` 或 Chromatic），状态全覆盖、数据固定，是视觉回归最稳的载体；② 交互测试——play function（`play: async ({ canvas }) => {...}`）在 story 里写交互断言，`@storybook/test` 提供 RTL 同款 API；③ a11y——addon-a11y 扫描每个 story。
- 体系价值：组件库团队尤其受益——对外发布的每个组件状态都有基线，升级时视觉 diff + 交互测试双重护航；业务团队的复杂组件（表格、级联选择器）同理。
- CI 编排：Storybook build → 静态资源发布预览 → Playwright 按 story 跑交互/视觉；PR 里附 preview 链接让产品/设计也能「看用例」。
- 追问钩子：story 和组件测试会不会重复？——story 覆盖「状态全集」，组件测试覆盖「行为断言」，前者保视觉完整、后者保逻辑正确，职责不同但底座相同。

```javascript
// Button.stories.tsx：状态全集 + play 交互测试
import { expect, within, userEvent } from '@storybook/test';
import Button from './Button';

export default { title: 'Button', component: Button };
export const Default = { args: { children: '提交' } };
export const Loading = { args: { children: '提交', loading: true } };
export const Disabled = { args: { children: '提交', disabled: true } };

export const ClickEmits = {
  args: { children: '提交', onClick: fn() },
  play: async ({ canvasElement, args }) => {       // 交互测试挂在 story 上
    const canvas = within(canvasElement);
    await userEvent.click(canvas.getByRole('button', { name: '提交' }));
    await expect(args.onClick).toHaveBeenCalledTimes(1);
  },
};
// CI：npx playwright test --config storybook  → 每个 story 视觉基线 + play 断言
```
