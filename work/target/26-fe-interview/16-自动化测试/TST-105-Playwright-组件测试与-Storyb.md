---
title: [TST-105] Playwright 的组件测试（component testing）是什么？和单测怎么分工？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-105：Playwright 的组件测试（component testing）是什么？和单测怎么分工？
**答**：
- 是什么：Playwright CT 让组件跑在**真实浏览器**里渲染（Vite 打包单组件），用 `mount` 挂载后用和 E2E 一模一样的 locator / auto-wait / 截图 API 来测。区别于 RTL + jsdom 的「假 DOM 模拟」。
- 核心差异：jsdom 里没有真实布局——`getBoundingClientRect` 恒 0、没有 IntersectionObserver、动画不跑；Playwright CT 里这些都真实，能测「滚动加载」「悬浮展开」「动画结束后的样式」这类 RTL 测不了的行为。
- 分工建议：交互逻辑、表单校验、状态分支 → RTL（快、调试好）；视觉与布局行为、真浏览器 API 依赖、组件视觉回归 → Playwright CT（真、能截图）。团队二选一也别硬切：通常 RTL 为主，CT 补充视觉层。
- 与 Storybook 的关系：CT 可以直接 mount 组件写交互断言；Storybook + `@storybook/experimental-addon-test`（跑 Playwright 跑 story）让「每个 story 即一条测试」，两套体系正在融合。
- 追问钩子：CT 的局限——不支持 SSR 场景、要维护 Vite 配置、多框架 monorepo 成本；以及为什么说「CT 填补金字塔中层」。

```jsx
// Counter.spec.tsx —— Playwright 组件测试
import { test, expect } from '@playwright/experimental-ct-react';
import { CartButton } from './CartButton';

test('点击后徽标 +1，超 99 显示 99+', async ({ mount }) => {
  const component = await mount(<CartButton count={0} onAdd={() => {}} />);

  await component.getByRole('button', { name: '加入购物车' }).click();
  await expect(component.getByTestId('badge')).toHaveText('1');

  // 真浏览器才有的断言：徽标没有溢出容器（jsdom 里恒 0 无法判断）
  const box = await component.getByTestId('badge').boundingBox();
  expect(box.width).toBeLessThan(40);
});
```
