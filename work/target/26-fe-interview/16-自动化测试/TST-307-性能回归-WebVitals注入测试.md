---
title: [TST-307] 在 Playwright 中如何精确采集 Web Vitals 用于回归断言？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-307：在 Playwright 中如何精确采集 Web Vitals 用于回归断言？
**答**：
- 注入 web-vitals 库或 PerformanceObserver（LCP/CLS/INP），事件缓冲收集。
- 交互后才能算 INP：用例内执行代表交互（点击主按钮）再取值。
- 采集值写入 report 供阈值断言与趋势对比。
- 环境标准化：CDP 节流 + 固定设备仿真，否则指标无比较意义。

```javascript
await page.addInitScript(() => {
  (window as any).__vitals = {};
  new PerformanceObserver(l => {
    const e = l.getEntries().pop();
    (window as any).__vitals.lcp = e.startTime;
  }).observe({ type: 'largest-contentful-paint', buffered: true });
});
await page.goto('/home');
expect(await page.evaluate(() => (window as any).__vitals.lcp)).toBeLessThan(2500);
r
```
