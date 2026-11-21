---
title: [TST-097] Playwright 怎么测 iframe、多页签和弹窗？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-097：Playwright 怎么测 iframe、多页签和弹窗？
**答**：
- iframe：用 `page.frameLocator(selector)` 拿到一个作用域受限的定位器，之后所有 getBy 都在这个 frame 里找；支持嵌套链式调用。关键优势是 frameLocator 惰性重查，iframe 重载后不用重新获取（对比老的 `page.frames()` 拿 Frame 对象，重载即失效）。
- 多页签：监听 `context.waitForEvent('page')`，`window.open` / `target=_blank` 触发时拿到新 Page 对象，两个 page 可以互相操作（A 页支付、B 页验证码）。注意要在触发动作**之前**挂好 waitForEvent，否则错过事件。
- 弹窗三类：① `window.alert/confirm/prompt` 用 `page.on('dialog')` 处理，`dialog.accept()/dismiss()`；② 新窗口用 waitForEvent('page')；③ 页内 modal（div 弹层）就是普通元素，getByRole('dialog')。
- 权限与来源：跨域 iframe 在 Context 层配置 `grantPermissions`；文件下载、剪贴板权限同理。
- 追问钩子：iframe 里的网络请求怎么拦？——`context.route` 全局拦截，或 `page.route` 覆盖主文档请求。

```javascript
test('iframe 支付 + 新页签 OAuth', async ({ page, context }) => {
  await page.goto('/checkout');

  // 1) iframe：银行收银台
  const bank = page.frameLocator('iframe.bank-frame');
  await bank.getByLabel('卡号').fill('6222020200112233');
  await bank.getByRole('button', { name: '确认支付' }).click();
  await expect(page.getByText('支付成功')).toBeVisible();

  // 2) 新页签：第三方登录（先挂监听，再点击）
  const popupPromise = context.waitForEvent('page');
  await page.getByRole('button', { name: '微信登录' }).click();
  const popup = await popupPromise;
  await popup.getByTestId('qr-confirm').click();

  // 3) 原生 confirm 弹窗：自动接受
  page.on('dialog', (d) => d.accept());
  await page.getByRole('button', { name: '取消订单' }).click();
});
```
