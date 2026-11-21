---
title: [TST-225] 视觉回归应该对「整页」还是「组件级」做 diff？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-225：视觉回归应该对「整页」还是「组件级」做 diff？
**答**：
- 组件级优先：Storybook/组件测试页截图，diff 粒度小、可归因、误报低。
- 整页快照作为补充：覆盖「组件组合后的布局回归」（间距塌陷/遮挡），但噪声大。
- 整页 diff 必须 mask 动态区 + 分辨率固定，否则维护成本失控。
- 分层策略：组件级高阈值频跑，整页低频（夜间）人工审。

```javascript
// 组件级（推荐）
await mount(<Button variant="primary">提交</Button>);
await expect(page.locator('button')).toHaveScreenshot('button-primary.png');
r
```
