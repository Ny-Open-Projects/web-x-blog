---
title: [TST-226] 多主题（暗色模式）/多视口下视觉测试的规模控制？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-226：多主题（暗色模式）/多视口下视觉测试的规模控制？
**答**：
- 组合爆炸控制：主题 × 视口矩阵只覆盖「组件级」，整页只测代表性组合。
- 暗色模式主要差异在 token 层——优先测「token 映射正确」而非全页像素。
- 用例内多视口循环断言关键组件，而非复制用例。
- 基线数量监控：基线数 = 用例 × 组合，超预算（如 2000）触发精简评审。

```javascript
for (const vp of [viewports.mobile, viewports.tablet, viewports.desktop]) {
  await page.setViewportSize(vp);
  await expect(page.getByTestId('card')).toHaveScreenshot(
    `card-${vp.width}.png`, { maxDiffPixelRatio: 0.005 });
}
r
```
