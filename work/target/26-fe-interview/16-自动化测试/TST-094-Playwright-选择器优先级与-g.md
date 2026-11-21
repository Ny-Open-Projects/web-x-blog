---
title: [TST-094] Playwright 里选择器怎么选？getByRole 为什么是首选？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-094：Playwright 里选择器怎么选？getByRole 为什么是首选？
**答**：
- 优先级：`getByRole` > `getByLabel` / `getByPlaceholder` / `getByText` > `getByTestId` > CSS/XPath。原则是「像用户一样找元素」：用户靠角色、名字、标签文本来感知页面，不靠 class。
- getByRole 的三重价值：① 稳定——角色由 ARIA 语义决定，重构 DOM/class 不影响；② 精确——`{ name }` + `exact` 区分"提交"和"提交并返回"；③ 附赠 a11y 检查——role 都查不到说明可访问性有问题，测试在替你做 a11y 审计。
- testid 是兜底：内容是动态生成的（随机文案、图标按钮、国际化文案）、或者页面里多个元素角色和名字相同时，用 `data-testid`，并在测试里集中定义常量。Playwright 的 `getByTestId` 默认属性可配置 `testIdAttribute: 'data-test'`。
- CSS/XPath 只在结构断言（如"这个 tr 是表格第 3 行"）或第三方组件无语义时用，且尽量包在 helper 里不外泄。
- 追问钩子：图标按钮怎么定位？——给 `aria-label`（同时修 a11y），测试用 `getByRole('button', { name: '关闭弹窗' })`，别用 `.icon-close` 这种 class。

```javascript
// playwright.config.ts 里统一 testid 约定
import { defineConfig } from '@playwright/test';
export default defineConfig({
  use: { testIdAttribute: 'data-test' },
});

test('定位优先级实战', async ({ page }) => {
  await page.goto('/settings');
  // 1) 首选：角色 + 可访问名
  await page.getByRole('checkbox', { name: '邮件通知' }).check();
  // 2) 表单：label 关联
  await page.getByLabel('昵称').fill('阿白');
  // 3) 动态文案/图标按钮：testid 兜底
  await page.getByTestId('save-settings-btn').click();
  await expect(page.getByRole('status')).toContainText('已保存'); // role=status 即 toast
});
```
