---
title: [TST-223] 时间戳/头像/广告位等动态内容如何避免视觉误报？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-223：时间戳/头像/广告位等动态内容如何避免视觉误报？
**答**：
- mask 定位动态元素（locator.mask()），diff 时忽略该区域。
- 更优：测试前冻结动态源（固定时钟/确定性假数据）——从源头消除动态。
- mask 粒度别太大（整页 mask = 测试失效），遵循「最小遮盖」。
- 动画组件截图前禁用动画（prefers-reduced-motion 或 CSS 注入）。

```javascript
await page.addStyleTag({ content: `*, *::before, *::after {
  animation: none !important; transition: none !important; }` });
await expect(page).toHaveScreenshot('feed.png', {
  mask: [page.getByTestId('ad-slot'), page.getByTestId('live-clock')],
});
r
```
