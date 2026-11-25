---
title: [TST-858] 弱网/离线场景如何自动化测试（Network API / 离线优先 PWA）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-858：弱网/离线场景如何自动化测试（Network API / 离线优先 PWA）？
**答**：
- 结论：弱网/离线测试要验证「降级体验而非崩溃」——断网时展示离线提示、操作进队列待恢复、Service Worker 缓存命中正确。
- Network API：Playwright context.setOffline(true) 或 CDP 注入延迟/丢包，覆盖完全离线与高延迟两态。
- 离线优先(PWA)：测 Service Worker 安装/激活、缓存策略（cache-first/network-first）、缓存未命中时的兜底 UI。
- 恢复验证：从离线恢复在线后，队列中的操作自动重放且幂等，数据不重复、不丢失。
- 追问钩子：离线时用户提交的表单，恢复网络后重复提交了两次，这类问题如何用测试发现？

```javascript
// 离线 -> 恢复的自动化测试
async function testOfflineFlow(context, page) {
  await page.goto('/form');
  await context.setOffline(true);           // 断网
  await page.getByText('提交').click();
  const offlineTip = await page.getByText('已离线，操作已保存').isVisible();
  await context.setOffline(false);          // 恢复
  await page.waitForResponse(r => r.url().includes('/submit'));
  const submits = await page.evaluate(() => window.__submitCount);
  return { offlineTip, submits, idempotent: submits === 1 }; // 应只提交一次
}
```
