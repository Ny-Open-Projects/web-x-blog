---
title: [TST-945] AB 实验 / 个性化推荐导致页面内容不同，视觉回归怎么屏蔽这种「非回归变化」？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-945：AB 实验 / 个性化推荐导致页面内容不同，视觉回归怎么屏蔽这种「非回归变化」？
**答**：
- 结论：把「内容差异」与「视觉回归」解耦——对动态内容区做语义归一化或打码，只对布局、样式、静态结构做像素 diff。
- 做法：测试时固定实验分组（强制命中同一 variant）、mock 推荐接口返回固定数据；无法 mock 的区域用 mask 排除。
- 边界：不能把所有动态区都 mask 掉——否则布局错乱这类真回归也会被漏掉。
- 追问钩子：推荐位今天展示 3 个商品明天 4 个，但容器高度应该固定，你怎么既允许内容变又抓住容器高度异常？

```javascript
// 固定实验分组 + mask 动态内容，但保留容器几何断言
await page.addInitScript(() => { window.__AB_VARIANT__ = 'control'; });
await page.route('**/api/recommend', route => route.fulfill({
  json: [{ id: 1 }, { id: 2 }], // 固定推荐数据
}));
await expect(page.locator('#recommend-list')).toHaveCSS('height', '300px'); // 几何断言
await expect(page.locator('#recommend-list')).toMatchSnapshot({
  mask: [page.locator('.item-title')], // 只 mask 文案，不 mask 容器
});
```
