---
title: [WCN-115] WCN 项目如何设计测试体系？跨框架一致性（同一组件在 React/Vue 宿主下行为一致）怎么验证？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-115：WCN 项目如何设计测试体系？跨框架一致性怎么验证？

**答**：
- 三层测试：① 组件单测（Vitest + jsdom，逻辑与事件语义）；② 交互 E2E（Playwright，真实浏览器含影子树查询：`page.locator('x-dialog')` 可穿透 open shadow，closed 需 hook）；③ 视觉回归（截图 + 主题矩阵：light/dark/RTL）。
- 跨框架一致性：同一套交互测试脚本跑三个宿主页面（React 宿主 / Vue 宿主 / 原生页面），断言相同 DOM 结果与事件 detail——组件契约不变性测试。
- 契约测试：对 custom-elements.json 断言（attributes/events/slots 与实现一致），CI 中 manifest diff 阻断 breaking 变更。
- 边界场景专项：SSR 输出含 DSD（`shadowrootmode` 存在断言）、define 前交互（无 JS 时可聚焦）、多实例共存（v1/v2 同页）。
- mock 数据与网络走 Playwright route 拦截，保持组件测试纯度。

```javascript
// Playwright：open shadow 可直接穿透
test('x-dialog 关闭事件带 action', async ({ page }) => {
  await page.goto('/react-host');            // React 宿主
  await page.locator('x-dialog .cancel').click();
  await expect(page.locator('x-dialog')).not.toHaveAttribute('open');
});
test('同组件 Vue 宿主行为一致', async ({ page }) => {
  await page.goto('/vue-host');              // 同一测试逻辑换宿主
  await page.locator('x-dialog .cancel').click();
  await expect(page.locator('x-dialog')).not.toHaveAttribute('open');
});
```
