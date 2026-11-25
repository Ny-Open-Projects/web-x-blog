---
title: [TST-238] 视觉回归与可访问性检查如何结合？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-238：视觉回归与可访问性检查如何结合？
**答**：
- 截图只验「看起来对」，a11y 断言验「用得上」——对比度/焦点顺序/语义结构并行检查。
- axe-core 扫描进同一测试流程，视觉 diff 通过但 a11y 失败照样 block。
- 焦点样式（:focus-visible）是视觉与 a11y 的交集——专门用例：Tab 后截图断言焦点环。
- 报告里视觉与 a11y 结果合并呈现，避免两套流程割裂。

```javascript
import AxeBuilder from '@axe-core/playwright';
test('卡片视觉与可访问性', async ({ page }) => {
  await page.goto('/card-demo');
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
  await page.keyboard.press('Tab');           // 焦点环视觉断言
  await expect(page.getByRole('link')).toBeFocused();
  await stableShot(page, 'card-focus.png');
});
r
```
