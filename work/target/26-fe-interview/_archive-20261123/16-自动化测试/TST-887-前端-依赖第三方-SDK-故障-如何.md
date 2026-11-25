---
title: [TST-887] 前端「依赖第三方 SDK 故障」如何用混沌测试覆盖？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-887：前端「依赖第三方 SDK 故障」如何用混沌测试覆盖？
**答**：
- 结论：第三方 SDK（统计/广告/客服/支付）必须「可失败而不阻塞」——混沌测试要故意让 SDK 加载失败/超时/抛错，验证主流程不受影响。
- 注入手段：mock SDK 脚本返回 404/超时，或让 SDK 的全局对象方法抛错，观察页面是否仍可交互。
- 验证点：核心功能（浏览/下单）不依赖 SDK；SDK 失败有超时兜底（不能无限等待）；不产生未捕获异常。
- 架构前提：SDK 异步非阻塞加载 + 超时熔断 + 错误隔离（沙箱 iframe 或 try/catch）。
- 追问钩子：某 SDK 同步阻塞渲染且失败时抛错导致白屏，混沌测试发现后你如何推动改造？

```javascript
// 第三方 SDK 故障注入：脚本加载失败不应阻塞主流程
async function sdkFailureTest(page) {
  await page.route('**/third-party/sdk.js', route => route.abort('failed')); // SDK 加载失败
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto('/checkout');
  const canCheckout = await page.getByText('提交订单').isEnabled();
  return {
    canCheckout,            // 主流程可用性
    uncaughtErrors: errors, // 应为空（SDK 失败被隔离）
    pass: canCheckout && errors.length === 0,
  };
}
```
