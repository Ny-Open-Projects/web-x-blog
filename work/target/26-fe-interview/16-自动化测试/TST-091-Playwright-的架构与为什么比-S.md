---
title: [TST-091] Playwright 的架构是什么？为什么比 Selenium / Cypress 快？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-091：Playwright 的架构是什么？为什么比 Selenium / Cypress 快？
**答**：
- 架构：Playwright 通过 WebSocket 直连浏览器（Chromium 走 CDP，WebKit/Firefox 走自家 patch 协议），驱动层在 Node 进程内，指令不走 HTTP 轮询，天然低延迟。
- 对比 Selenium：Selenium 基于 WebDriver 协议走 HTTP 请求-响应，每条指令一次往返，且依赖浏览器厂商 driver；Playwright 一条长连接双向通信，还能推送事件（DOM 变化、网络、控制台）。
- 对比 Cypress：Cypress 运行在浏览器内与应用同源，无法跨多标签、多域、多浏览器；Playwright 每个用例跑在独立 BrowserContext 里，进程外控制，天然隔离且可测多页签、iframe、扩展。
- 速度来源：长连接省往返、事件驱动等待（不用轮询 sleep）、Context 秒级启动（不重启浏览器）、原生并行分片。
- 追问钩子：能拿到浏览器之外的东西——网络请求、CPU 节流、地理定位，这是"测试工具"变"自动化平台"的关键。

```javascript
// Playwright 架构关键点：一条 WebSocket + 事件驱动
import { test, expect } from '@playwright/test';

test('事件驱动的等待，不需要轮询', async ({ page }) => {
  // page.on 推送事件：请求/响应/控制台，都是协议层推过来的
  page.on('response', (res) => {
    if (res.url().includes('/api/goods')) console.log('goods api:', res.status());
  });

  await page.goto('https://shop.example.com/list');
  // locator 点击：Playwright 内部轮询的是「元素状态」（可见/可点/稳定），
  // 不是测试脚本轮询页面——这就是 auto-wait 的本质
  await page.getByRole('button', { name: '加入购物车' }).first().click();
  await expect(page.getByText('已加入')).toBeVisible();
});
```
