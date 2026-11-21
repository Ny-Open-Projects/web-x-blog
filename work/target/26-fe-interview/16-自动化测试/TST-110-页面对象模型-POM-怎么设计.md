---
title: [TST-110] 页面对象模型（POM）怎么设计？Playwright 时代还需要吗？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-110：页面对象模型（POM）怎么设计？Playwright 时代还需要吗？
**答**：
- POM 的价值：把「页面结构（选择器）」与「测试逻辑（业务步骤）」分离——页面改版只改 Page Object，几十条用例不动。本质是给 UI 测试做防腐层。
- Playwright 时代的修正：老 POM（每个方法返回 elementHandle、自己写等待）很多实践已被 locator + auto-wait 取代；现代写法是「Locator 化的 POM」——Page Object 只暴露 locator 和语义化方法，不暴露 handle、不写 sleep、不做断言（断言留在用例里，保持 expect 可读）。
- 设计要点：一个页面/组件一个类；方法名说业务不说 DOM（`addToCart(sku)` 而非 `clickButton3()`）；公共组件（导航栏、toast）抽独立 fragment 类；跨页面流程抽成 flow（`loginFlow.buyer(page)`）。
- 过度设计警告：为每页写全套 POM 但只用两个方法；正确做法是「用到才加」，YAGNI。
- 追问钩子：什么时候干脆不用 POM？——小型项目/一次性验证脚本直接 `page.getByRole` 足够；POM 是维护成本超过收益时的投资。

```javascript
// pages/CartPage.ts —— Locator 化的 POM
import { type Page, type Locator, expect } from '@playwright/test';

export class CartPage {
  readonly page: Page;
  readonly items: Locator;
  readonly checkoutBtn: Locator;

  constructor(page: Page) {
    this.page = page;
    this.items = page.getByTestId('cart-item');
    this.checkoutBtn = page.getByRole('button', { name: '结算' });
  }

  async goto() { await this.page.goto('/cart'); }

  // 业务语义方法：内部只做操作，不断言
  async removeItem(name: string) {
    await this.items.filter({ hasText: name }).getByRole('button', { name: '删除' }).click();
  }
}

// 用例：断言留在用例层
test('删除商品后金额更新', async ({ page }) => {
  const cart = new CartPage(page);
  await cart.goto();
  await cart.removeItem('iPhone 保护壳');
  await expect(page.getByText('共 2 件')).toBeVisible();
});
```
