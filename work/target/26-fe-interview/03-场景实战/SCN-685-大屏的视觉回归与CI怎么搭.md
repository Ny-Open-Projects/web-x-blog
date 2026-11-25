---
title: [SCN-685] 大屏的视觉回归与 CI 怎么搭？3D 场景截图对比靠谱吗？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-685：大屏视觉回归 CI 怎么搭？
**答**：
- 分层回归：布局层（面板位置/尺寸，DOM 断言稳定可靠）、图表层（ECharts 快照，固定 mock 数据）、3D 层（固定相机位 + 固定种子渲染截图对比，容忍度放宽 + 忽略动效区域）。
- 3D 截图对比要点：禁用随机动效（粒子种子固定）、等 p95 渲染完成后再截（加载时序稳定）、色差阈值（像素 diff 1%~3%）——否则天天假阳性没人看。
- 多分辨率矩阵：核心 3 种分辨率各跑一轮；告警状态/数据空洞等异常态用 fixture 驱动截图。
- 审核流：diff 超阈值 → 人工确认 → 更新基线（基线变更强制关联 PR 说明）。
- 追问钩子：3D 回归 CI 耗时高怎么办——只对受影响面板/场景跑（按改动文件映射）+ 夜间全量、提交时冒烟。

```javascript
// Playwright 大屏回归
test('layout stable @ 3840x2160', async ({ page }) => {
  await page.setViewportSize({ width: 3840, height: 2160 });
  await page.goto('/screen/park?fixture=steady');          // 固定数据
  await page.waitForFunction(() => window.__sceneReady);   // 3D 就绪信号
  await expect(page).toHaveScreenshot('park-4k.png', {
    maxDiffPixelRatio: 0.03,                               // 3D 层容忍度
    mask: [page.locator('.particle-layer')],               // 忽略动效区
  });
});
```
