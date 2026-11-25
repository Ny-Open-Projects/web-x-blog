---
title: [XP-313] 跨端测试：UI 快照与视觉回归
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-313：跨端测试：UI 快照与视觉回归

**答**：
- 快照：各端渲染同一组件截图对比基线（像素 diff < 0.5% 通过）。
- 基准：固定环境（分辨率/DPR/字体）截图，避免环境噪声。
- 流程：MR 触发快照，变化走 diff 图人工确认后更新基线。

```javascript
// 视觉回归
async function visualDiff(platform, component, baseline) {
  const shot = await screenshot(platform, component, { dpr: 2, w: 375 });
  const diff = pixelDiff(shot, baseline, { threshold: 0.5 });
  return { pass: diff.pct < 0.5, pct: diff.pct,
    diffImg: diff.pct > 0.5 ? diff.image : null,
    note: diff.pct > 0.5 ? '生成 diff 图人工确认' : 'ok' };
}
```
