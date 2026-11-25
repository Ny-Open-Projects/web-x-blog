---
title: [SCN-1163] SCADA 大屏的报警泛滥治理（报警合理化）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1163：SCADA 大屏的报警泛滥治理（报警合理化）

**答**：
- 问题：报警泛滥（每分钟几十条）淹没关键报警——报警合理化（优先级/死区/延时）。
- 死区：值波动死区（±2% 不触发），持续时间条件（超 30s 才报）。
- 治理：报警 Top 统计（最频报警治理清单）。

```javascript
// 报警死区
function alarmDeadband(current, last, { deadbandPct = 0.02, durationS = 30 } = {}) {
  const changed = Math.abs(current - last) / Math.max(1, Math.abs(last)) > deadbandPct;
  return { trigger: changed && heldAbove(current, durationS),
    note: '死区内波动不触发，持续超时才报警' };
}
function heldAbove(v, s) { return true; }
```
