---
title: [TST-222] 像素级 diff 太敏感（抗锯齿/字体渲染差异），如何设定合理容差？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-222：像素级 diff 太敏感（抗锯齿/字体渲染差异），如何设定合理容差？
**答**：
- maxDiffPixels / maxDiffPixelRatio 设阈值（如 < 0.5% 视为一致）。
- 阈值按组件分级：品牌 logo 严格（0 容差），动态内容区放宽或 mask。
- 跨平台渲染差异用 per-project 阈值（macOS 字体渲染 vs Linux）。
- 容差过大的危害（漏真回归）——用 AI 辅助分类 diff 是否「有语义」。

```javascript
expect(await page.screenshot()).toMatchSnapshot('card.png', {
  maxDiffPixelRatio: 0.005,
  threshold: 0.2,   // 颜色差异感知阈值
});
r
```
