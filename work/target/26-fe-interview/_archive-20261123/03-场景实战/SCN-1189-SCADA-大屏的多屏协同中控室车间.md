---
title: [SCN-1189] SCADA 大屏的多屏协同（中控室/车间/管理层）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1189：SCADA 大屏的多屏协同（中控室/车间/管理层）

**答**：
- 分层：中控室（全功能）/车间（本产线）/管理层（KPI 总览）——同一数据不同视图。
- 权限：各屏视图与操作权限按角色裁剪。
- 一致：核心 KPI 数字各屏一致（同源同刷新）。

```javascript
// 多屏协同
function multiScreenStrategy(screen) {
  const STRATEGIES = {
    control-room: { views: 'all', control: true },
    workshop: { views: 'own-line', control: false },
    management: { views: 'kpi-only', control: false },
  };
  return STRATEGIES[screen.type] ?? STRATEGIES['management'];
}
```
