---
title: [TST-107] E2E 该不该 mock 后端接口？真环境和假数据的边界怎么定？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-107：E2E 该不该 mock 后端接口？真环境和假数据的边界怎么定？
**答**：
- 结论：分层混合。前端职责内的链路（渲染、交互、路由、状态）mock 后端；端到端业务验证（前后端契约、支付回调、真实数据库写入）打真后端。全 mock 会漏掉契约变更，全真则数据难造、速度慢、不稳定。
- mock 的适用场景：异常分支（后端很难稳定造出 500/超时）、边界数据（1 万条列表、超长昵称）、依赖三方（短信、支付网关）——这些用 page.route / MSW 造，又快又稳。
- 真后端的适用场景：写操作落库后的状态查询、鉴权链路、定时任务触发的状态机。用测试环境独立数据库 + API 造数，用例结束清理。
- 契约风险与对策：mock 后端真实接口最大的坑是「mock 说成功，真后端改了字段」——对策是核心接口留一组「契约冒烟」打真环境，或用契约测试（schema 校验）兜底。
- 追问钩子：灰度环境怎么测？——E2E 用独立灰度域名 + `X-Gray-Tag` header（route 里统一加），保证命中被测版本。

```javascript
// 混合策略示例：核心链路真后端，异常分支 mock
test('下单主链路（真环境）+ 异常兜底（mock）', async ({ page }) => {
  // 真后端：登录、列表、下单走测试环境
  await page.goto('https://staging.shop.com');
  await page.getByLabel('手机号').fill('13800000000');
  // ... 下单成功，断言落库后的订单状态
  await expect(page.getByText('待发货')).toBeVisible();

  // mock：库存不足异常（真后端难造）
  await page.route('**/api/stock/check', (route) =>
    route.fulfill({ json: { available: 0 } }));
  await page.getByRole('button', { name: '再买一件' }).click();
  await expect(page.getByText('库存不足')).toBeVisible();
});
```
