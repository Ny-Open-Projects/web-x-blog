---
title: [TST-231] 视觉测试的 flaky 来源与治理（字体加载/动图/首屏异步）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-231：视觉测试的 flaky 来源与治理（字体加载/动图/首屏异步）？
**答**：
- 字体未加载完截图 → 文字回退闪烁：等待 document.fonts.ready。
- 首屏异步内容（图片懒加载）截到一半：等待网络空闲 + 图片 complete。
- 治理三件套：冻结时钟/禁动画/等待资源就绪，把「不确定」变「确定」。
- 剩余 flaky 用 AI 分类或直接 mask——不要靠重试掩盖视觉 flaky。

```javascript
await page.goto('/goods');
await page.evaluate(() => document.fonts.ready);
await page.waitForFunction(() =>
  [...document.images].every(img => img.complete));
await expect(page).toHaveScreenshot('goods.png');
r
```
