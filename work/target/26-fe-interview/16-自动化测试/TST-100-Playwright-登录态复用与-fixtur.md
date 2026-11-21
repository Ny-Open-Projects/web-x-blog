---
title: [TST-100] Playwright 怎么复用登录态？fixtures 和 storageState 怎么用？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-100：Playwright 怎么复用登录态？fixtures 和 storageState 怎么用？
**答**：
- storageState：把登录后的 cookies + localStorage 序列化成 JSON，后续用例直接带态启动，跳过每个用例重复走 UI 登录（登录一次即可，E2E 大头提速手段）。做法：`setup` 项目里跑一遍登录 → `page.context().storageState({ path: 'auth.json' })` → 其他项目 `use: { storageState: 'auth.json' }`。
- 全局 setup：`globalSetup` 或依赖项目（Playwright 1.31+ 的 projects dependencies）里完成「登录 + 造基础数据」，所有用例继承，保证只跑一次。
- 自定义 fixtures：把「登录后的 page」「预置商品的 context」「造数 API client」封装成 fixture，用例声明参数即得，自动清理。比 beforeEach + 模块级变量更类型安全、可组合、可 override。
- 注意：登录态过期（token TTL）怎么办——setup 里登录放最后一步或用接口登录拿 token；长跑 CI 用 session 刷新；不要共享同一个 auth.json 给并发写操作用例（数据互踩）。
- 追问钩子：多角色（买家/卖家/管理员）怎么管理？——每个角色一个 storageState 文件，fixture 里按角色注入。

```javascript
// auth.setup.ts：登录一次，存登录态
import { test as setup, expect } from '@playwright/test';
const authFile = 'playwright/.auth/buyer.json';
setup('login as buyer', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('手机号').fill('13800000000');
  await page.getByLabel('密码').fill('test1234');
  await page.getByRole('button', { name: '登录' }).click();
  await expect(page.getByText('欢迎回来')).toBeVisible();
  await page.context().storageState({ path: authFile });
});

// fixtures.ts：自定义 fixture 注入登录页
import { test as base } from '@playwright/test';
export const test = base.extend<{ buyerPage: Page }>({
  buyerPage: async ({ browser }, use) => {
    const ctx = await browser.newContext({ storageState: 'playwright/.auth/buyer.json' });
    await use(await ctx.newPage());
    await ctx.close();
  },
});
```
