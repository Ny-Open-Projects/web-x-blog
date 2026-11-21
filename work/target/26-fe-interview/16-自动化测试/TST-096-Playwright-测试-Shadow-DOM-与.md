---
title: [TST-096] Playwright 怎么测 Web Components？Shadow DOM 能穿透吗？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-096：Playwright 怎么测 Web Components？Shadow DOM 能穿透吗？
**答**：
- 结论：能。Playwright 的选择器引擎默认「穿透所有 Shadow DOM」，`getByRole` / CSS 都在 shadow root 里递归查找，不需要 Selenium 那种层层 `getShadowRoot().findElement()`，也不需要打开 `shadowRootOpen` 特殊模式。
- 对比：Selenium 需要 JS 注入逐层展开；Cypress 默认不进 shadow，要加 `includeShadowDom: true`。Playwright 把这层复杂度吃掉了，这是它测微前端/自定义组件库（Liferay、Lit、Stencil 组件）的杀手锏。
- 注意点：`getByText` 默认也能匹配 shadow 内文本；但 CSS 选择器里如果显式写了 `>>>`（ piercing combinator）反而可以显式表达跨边界；自定义元素若在 `connectedCallback` 里异步渲染，auto-wait 会兜住。
- 场景：微前端（qiankun 子应用）、公司自研 Web Components 组件库、iframe + shadow 嵌套（`frameLocator` + 穿透组合）。
- 追问钩子：closed shadow root 怎么办？——Playwright 引擎基于协议层遍历，closed 也能进；但如果组件内部用 canvas 绘制，只能截图比对。

```javascript
test('穿透 Shadow DOM 操作自定义组件', async ({ page }) => {
  await page.goto('/design-system-demo');

  // <my-dialog> 内部三层 shadow：mask → panel → close-btn
  // 普通定位直接命中 shadow 内部元素
  await page.getByRole('button', { name: '打开对话框' }).click();
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.getByRole('button', { name: '确定' }).click(); // 在 shadow 里

  // 显式 piercing 写法（等价，但更"结构化"）
  await page.locator('my-dialog >>> my-panel >>> button.confirm').click();

  // shadow + iframe 嵌套组合：frameLocator 再穿透
  const frame = page.frameLocator('#payment-iframe');
  await expect(frame.getByTestId('amount')).toHaveText('¥ 299.00');
});
```
