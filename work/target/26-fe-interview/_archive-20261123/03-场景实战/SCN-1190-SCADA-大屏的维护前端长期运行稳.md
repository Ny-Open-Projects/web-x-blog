---
title: [SCN-1190] SCADA 大屏的维护（前端长期运行稳定性）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1190：SCADA 大屏的维护（前端长期运行稳定性）

**答**：
- 稳定：7×24 运行——内存监控（48h 泄漏自动重启）、WS 重连、渲染降级。
- 自动恢复：页面崩溃自动刷新（崩溃检测 + 3s 恢复）。
- 巡检：前端巡检脚本（每小时检查渲染/数据新鲜度）。

```javascript
// 长期运行
function longRunGuard(page) {
  return {
    memWatch: memoryGuard(48 * 3600_000),              // 泄漏自动重启
    crashRecover: () => { location.reload(); },
    heartbeat: reportAlive(60_000),
    inspect: hourlyInspect(page),
  };
}
function memoryGuard(t) { return true; }
function reportAlive(ms) { return true; }
function hourlyInspect(p) { return true; }
```
