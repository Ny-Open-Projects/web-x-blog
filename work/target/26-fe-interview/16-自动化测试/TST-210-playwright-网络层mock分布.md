---
title: [TST-210] 分布式下 mock 后端（route/MSW）与真实环境的取舍？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-210：分布式下 mock 后端（route/MSW）与真实环境的取舍？
**答**：
- E2E 主流程走真实环境（验证集成），长尾/异常场景用 route mock（超时/500/慢速）。
- route mock 是 per-context 的，天然随 worker 隔离，无分布式同步问题。
- 全 mock 会让 E2E 退化为「UI 冒烟」，失去集成验证价值——mock 比例控制（如 < 30% 用例）。
- mock 数据与真实环境 schema 要同步（版本漂移是常见假绿来源）。

```javascript
test('弱网下单提示', async ({ page }) => {
  await page.route('**/api/order', async route =>
    new Promise(r => setTimeout(() => route.fulfill({ status: 504 }), 5000)));
  await page.getByRole('button', { name: '提交订单' }).click();
  await expect(page.getByText('网络超时，请重试')).toBeVisible();
});
r
```
