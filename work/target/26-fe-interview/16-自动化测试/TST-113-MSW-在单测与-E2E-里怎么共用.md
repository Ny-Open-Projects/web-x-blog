---
title: [TST-113] MSW 在单测和 E2E 里怎么共用一套 handlers？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-113：MSW 在单测和 E2E 里怎么共用一套 handlers？
**答**：
- 共用架构：handlers 定义成独立模块（`src/mocks/handlers.ts`）不依赖测试框架；单测用 `setupServer`（Node 拦截），浏览器/E2E 用 `setupWorker`（Service Worker 拦截），两层吃同一份 handlers 数组——这是 MSW「test-before-prod」理念的落点。
- 浏览器侧接入：`public/mockServiceWorker.js`（`npx msw init public/` 生成）；dev 模式 `worker.start()` 让本地开发不依赖后端；E2E 里 Playwright 打开页面时 worker 已注册，默认接管请求。
- E2E 按需开关：生产构建不能带 worker——用环境变量 `ENABLE_MSW` 控制 `main.tsx` 里动态 import；E2E mock 场景单独配一个「msw 特化项目」，或对个别用例 `page.evaluate` 调 window 上的 worker 引用动态插 handler。
- 分层取舍：核心链路 E2E 打真后端，异常分支/三方依赖用 MSW；单测里 MSW 全接管。契约风险靠 schema 校验兜底。
- 追问钩子：worker 拦截对 SSE/WebSocket 支持？——MSW 2.x 有 `ws` handler 可 mock WebSocket；SSE 用原始响应流 mock。

```javascript
// src/mocks/browser.ts
import { setupWorker } from 'msw/browser';
import { handlers } from './handlers';
export const worker = setupWorker(...handlers);

// src/main.tsx —— 按环境启用
if (import.meta.env.VITE_ENABLE_MSW === 'true') {
  const { worker } = await import('./mocks/browser');
  await worker.start({ onUnhandledRequest: 'bypass' });
}

// e2e/msw.spec.ts —— E2E 里动态插场景 handler
test('库存不足分支（MSW 特化）', async ({ page }) => {
  await page.goto('/goods/1'); // 页面已带 worker
  await page.evaluate(async () => {
    const { http, HttpResponse } = await import('msw');
    const w = (window as any).__mswWorker;
    await w.use(http.post('/api/cart', () =>
      HttpResponse.json({ msg: '库存不足' }, { status: 409 })));
  });
  await page.getByRole('button', { name: '加入购物车' }).click();
  await expect(page.getByText('库存不足')).toBeVisible();
});
```
