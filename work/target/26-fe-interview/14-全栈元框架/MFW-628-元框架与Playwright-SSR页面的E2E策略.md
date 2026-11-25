---
title: [MFW-628] SSR 页面的 E2E 策略：Playwright 与流式/水合的协同
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-628：SSR 页面 E2E 策略

**答**:
- SSR 页面 E2E 的特殊断言：1) **流式时序断言**（骨架先现 → 内容后到——waitForSelector 顺序断言 RBL-549）；2) **网络空闲 vs 渲染完成**（networkidle 在流式页不可靠——流可能 long-running：用「语义标记」（data-loaded）断言渲染完成而非 networkidle）；3) **水合完成断言**（交互可执行 = 水合完成——click 前等待 hydration：waitForFunction(window.__hydrated)）。
- 测试的服务端状态：MSW mock API（SSR fetch 拦截——node 端 + client 端双拦截 RBL-549）；「测试的确定性」：SSR 的 fetch 与 client fetch 都 mock（同一 handler 集）。
- 断言的反模式：waitForTimeout（固定等待——flaky 源头：改用语义条件等待）；「E2E 的 flaky 治理」（RBL-957 静默清单的 E2E 版）。
- 追问钩子：为什么 SSR E2E 中「networkidle」是反模式断言？——流式页面（SSE/长轮询/Action streaming）连接可能不断开——networkidle 永不触发 → 超时；「渲染完成」的语义 = 语义标记（data-loaded/data-hydrated）而非网络状态——断言的语义与实现解耦：页面开发者标记语义、测试消费标记——网络无关的完成信号（RBL-540 水合检测的 E2E 化）。

```typescript
// SSR E2E 模板
test('product page', async ({ page }) => {
  await page.goto('/product/42');
  // 1) 流式时序：骨架 → 内容
  await page.waitForSelector('[data-loading="product"]', { state: 'attached', timeout: 2000 });
  await page.waitForSelector('[data-loaded="product"]');    // 语义标记：不依赖 networkidle
  // 2) 水合完成：交互可执行
  await page.waitForFunction(() => (window as any).__hydrated === true);
  await page.click('[data-testid="add-to-cart"]');          // 水合后点击
  await page.waitForSelector('[data-testid="cart-count"]:has-text("1")');
});
// 反模式
// await page.waitForTimeout(3000);                       ← flaky：慢了不够快了浪费
// await page.waitForLoadState('networkidle');            ← 流式页永不 idle
// harness（RBL-549）：MSW + dev server 生命周期 + 状态注入矩阵
```
