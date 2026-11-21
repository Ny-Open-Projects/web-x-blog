---
title: [NODE-464] Node 服务参与的端到端（E2E）测试策略如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-464：端到端测试策略
**答**:
- 范围界定：E2E = 前端 UI → BFF → 核心下游的真实链路（关键业务路径）；不追求全覆盖（贵、脆、慢）——覆盖"用户能不能完成核心任务"（下单/支付/登录）+ 冒烟。
- 环境策略：专用 E2E 环境（数据可控、外部依赖用 stub 挡板——支付沙箱/短信挡板返回固定值）、测试账号池（预置不同状态的账号：VIP/欠费/黑名单）。
- 稳定性工程：显式等待（不 sleep）、幂等准备（用例自带数据构造与清理，不依赖其他用例）、失败重跑与截图/trace 归档（失败可回放）、选择器规范（data-testid，禁 CSS 路径）。
- 服务端配合：挡板服务（stub 下游可切换行为：正常/超时/错误——测前端降级 ARC-545）、时间可控（测试时钟：验证倒计时/SLA 逻辑 NODE-437）、钩子清理。
- 运维：E2E 时长预算（< 15 分钟，超了分片并行）、flaky 率治理（ARC-130 > 2% 的用例修复或下线）、主道每 MR 跑冒烟 + 定时全量。
```javascript
// E2E 关键路径（Playwright）
test('用户完成下单支付（挡板支付）', async ({ page }) => {
  await loginAs(page, 'vip-user');                               // 账号池
  await page.goto('/goods/g1'); await page.click('#buy');
  await page.click('#submit-order');
  await expect(page.locator('.pay-panel')).toBeVisible();
  await payStub.succeed(orderIdOf(page));                        // 支付挡板成功
  await expect(page.locator('.pay-success')).toBeVisible();
});
```
