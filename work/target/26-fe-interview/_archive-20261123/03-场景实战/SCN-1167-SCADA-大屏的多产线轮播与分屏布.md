---
title: [SCN-1167] SCADA 大屏的多产线轮播与分屏布局
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1167：SCADA 大屏的多产线轮播与分屏布局

**答**：
- 布局：多产线分屏（2×2）或轮播（30s 切换），告警强插（报警时切到报警产线）。
- 管理：布局配置化（屏位绑定产线/视图）。
- 一致性：各分屏数据时间对齐（同一刷新周期）。

```javascript
// 多产线分屏
function multiLineLayout(lines, { mode = 'grid' } = {}) {
  return {
    grid: lines.map((l, i) => ({ line: l, slot: i })),   // 2x2 分屏
    alarmInterrupt: (line) => switchSlot(lines.indexOf(line)),   // 报警强插
    rotate: mode === 'rotate' ? 30_000 : null,
  };
}
function switchSlot(i) { return i; }
```
