---
title: [TST-104] waitForNetworkIdle 为什么不可靠？E2E 里正确的网络等待姿势是什么？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-104：waitForNetworkIdle 为什么不可靠？E2E 里正确的网络等待姿势是什么？
**答**：
- networkIdle 的脆弱性：它假设「500ms 没新请求 = 加载完成」，但埋点上报、长轮询、WebSocket 心跳、图片懒加载随时可能打破空闲判定——永远等不到 idle 或偶尔超时，是 flaky 的经典来源。
- 正确姿势一：等具体响应。`page.waitForResponse('**/api/list')` 在点击**之前**注册 promise，点击后 await，精确对齐业务请求。
- 正确姿势二：等 UI 表现。`expect(page.getByRole('cell', { name: '订单 1001' })).toBeVisible()`——auto-wait 轮询，只要数据渲染出来就过，不关心请求细节；一般场景优先这个，简单且贴近用户视角。
- 正确姿势三：等 URL / 等自定义状态。路由跳转用 `waitForURL('**/detail/*')`；复杂条件用 `page.waitForFunction(() => window.__appReady === true)`（应用自己打 readiness 标记）。
- 反模式清单：`waitForTimeout(3000)`（死等）、`waitForLoadState('networkidle')`、sleep 后立即断言。唯一可接受的死等：无法观测的第三方动画兜底，且必须写注释说明。
- 追问钩子：流式响应（SSE/打字机）怎么断言？——等最后一条内容出现或 `expect.poll(() => page.getByTestId('stream').textContent())` 收敛。

```javascript
test('网络等待三种正确姿势', async ({ page }) => {
  await page.goto('/orders');

  // 姿势1：先注册，后触发，等具体响应
  const respPromise = page.waitForResponse((r) =>
    r.url().includes('/api/orders') && r.request().method() === 'GET');
  await page.getByRole('button', { name: '刷新' }).click();
  const resp = await respPromise;
  expect(resp.status()).toBe(200);

  // 姿势2：等 UI（首选，最像用户）
  await expect(page.getByRole('cell', { name: /订单 100\d/ }).first()).toBeVisible();

  // 姿势3：等路由与自定义就绪标记
  await page.getByRole('link', { name: '详情' }).first().click();
  await page.waitForURL('**/orders/*');
  await page.waitForFunction(() => (window as any).__appReady === true);
});
```
