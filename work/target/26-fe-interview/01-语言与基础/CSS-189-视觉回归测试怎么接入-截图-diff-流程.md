---
title: [CSS-189] 视觉回归测试怎么接入（截图 diff 流程）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-189：视觉回归测试怎么接入（截图 diff 流程）？

**答**：
- 流程：首次生成基线截图 → CI 每次跑对比 → diff 超阈值失败 → 上传 diff 图人工确认 → 确认无问题后更新基线。
- 稳定性三要素：固定视口与主题、等待字体就绪（document.fonts.ready）、禁用动画与光标。
- 阈值：`maxDiffPixelRatio` 放行亚像素级渲染差异；组件级截图（locator.screenshot）比整页更稳。
- 适用边界：核心页面 + 组件库全量快照；营销页高频改版场景收益低。

```javascript
// card.spec.js —— Playwright 视觉回归
const { test, expect } = require('@playwright/test');

test('card 组件视觉快照', async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 720 });
  await page.goto('/components/card');
  await page.evaluate(() => document.fonts.ready);  // 字体就绪
  await page.addStyleTag({                          // 冻结动画防抖
    content: '*, *::before, *::after { animation: none !important; transition: none !important; }',
  });
  await expect(page.locator('.card')).toHaveScreenshot('card.png', {
    maxDiffPixelRatio: 0.01,   // 1% 容差放行渲染噪声
    animations: 'disabled',
    caret: 'hide',             // 输入框光标隐藏
  });
});
/* CI 流程：
   1. 无基线 → 生成 card.png 入库
   2. 有基线 → diff，超阈值失败并产出 card-diff.png
   3. 人工确认变更合法 → playwright test --update-snapshots 更新基线 */
```
