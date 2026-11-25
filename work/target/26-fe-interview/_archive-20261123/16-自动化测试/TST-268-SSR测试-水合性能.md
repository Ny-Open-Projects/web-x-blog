---
title: [TST-268] 水合性能（TTI/INP 受水合影响）的回归测试？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-268：水合性能（TTI/INP 受水合影响）的回归测试？
**答**：
- 指标采集：实验室（Lighthouse）+ 现场水合耗时（performance API 打点）。
- 断言水合时长预算：hydration complete 事件在交互前完成（或可交互时间 < 2s）。
- 大页面拆分：选择性水合（先水合交互区）后，断言「可交互时间」提前。
- 回归门禁：Lighthouse CI 的 TTI/TBT 预算，超预算 block。

```javascript
test('可交互时间预算', async ({ page }) => {
  await page.goto('/home');
  const tti = await page.evaluate(() => performance.getEntriesByName('interactive')[0]?.startTime);
  expect(tti).toBeLessThan(2000);
});
r
```
