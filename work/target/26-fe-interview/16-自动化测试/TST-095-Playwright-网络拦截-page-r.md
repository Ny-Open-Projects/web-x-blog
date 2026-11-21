---
title: [TST-095] Playwright 怎么做网络拦截？page.route 的原理与实战
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-095：Playwright 怎么做网络拦截？page.route 的原理与实战
**答**：
- 原理：`page.route(pattern, handler)` 在协议层注册拦截器，匹配的请求根本不发出去，由 handler 决定 `fulfill`（伪造响应）、`continue`（放行，可改 header/url）、`abort`（模拟断网/失败）。因为拦截在浏览器网络栈之下，连 fetch/XHR/图片/字体全部覆盖，不依赖应用代码。
- 三类典型用法：① mock 接口造数据（比等后端造数快且稳定）；② 模拟异常（500、超时、慢接口）测 loading/降级；③ 拦掉无关资源（埋点、广告、字体）提速。
- 注意事项：route 在页面跳转后仍有效（page 级）；要针对新开页签用 `context.route`；glob 匹配 `**/api/**`，函数匹配可写复杂逻辑；mock 未被触发可以用 `expect(response).toBeTruthy()` 或 route handler 内断言。
- 与 MSW 分工：page.route 是「测试工具层」的拦截，E2E 快速造场景；MSW 是「应用运行层」的拦截，同一套 handler 单测和 E2E 共用。面试给出取舍即可。
- 追问钩子：怎么模拟弱网？——`route.fulfill` 前加 `await sleep`，或 `continue` + CDP `Network.emulateNetworkConditions`。

```javascript
test('网络拦截：mock 列表 + 模拟 500 + 拦埋点', async ({ page }) => {
  // 1) mock 成功响应
  await page.route('**/api/goods*', async (route) => {
    const url = new URL(route.request().url());
    const page_ = Number(url.searchParams.get('page') ?? 1);
    await route.fulfill({
      json: { list: [{ id: page_, name: `商品${page_}` }], total: 3 },
    });
  });
  // 2) 模拟接口 500，测错误态
  await page.route('**/api/recommend*', (route) =>
    route.fulfill({ status: 500, json: { msg: 'server error' } })
  );
  // 3) 放行其余请求，但拦掉埋点提速
  await page.route('**/track**', (route) => route.abort());

  await page.goto('/list');
  await expect(page.getByText('商品1')).toBeVisible();
  await expect(page.getByText('推荐服务异常')).toBeVisible(); // 降级文案
});
```
