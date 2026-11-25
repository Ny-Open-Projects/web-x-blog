---
title: [TST-236] 第三方组件/图表库（ECharts 等渲染随机）视觉测试怎么处理？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-236：第三方组件/图表库（ECharts 等渲染随机）视觉测试怎么处理？
**答**：
- Canvas/随机渲染：关闭动画 + 固定随机种子（图表库支持 seed 时）。
- 仍不稳定则降级为「区域存在性 + 语义断言」（图表容器存在、图例文本正确）。
- 或者截图后按「非像素比对」检查（尺寸/颜色主色调）。
- 第三方升级时手动批量更新其基线并集中人审（变更集中在一次 PR）。

```javascript
await page.goto('/chart');
await page.evaluate(() => { chart.setOption({ animation: false }); chart.clear(); chart.setOption(fixedOption); });
await expect(page.getByTestId('chart')).toHaveScreenshot('chart.png',
  { maxDiffPixelRatio: 0.02 }); // 图表类放宽阈值
r
```
