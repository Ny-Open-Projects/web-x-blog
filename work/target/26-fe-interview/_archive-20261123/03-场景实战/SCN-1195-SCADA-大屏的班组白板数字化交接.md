---
title: [SCN-1195] SCADA 大屏的班组白板（数字化交接班看板）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1195：SCADA 大屏的班组白板（数字化交接班看板）

**答**：
- 白板：本班任务/待办/异常交接/注意事项——数字化白板（替代纸质交接本）。
- 交接：交接项逐条确认（接方签字），遗留问题高亮。
- 留存：白板历史归档（追溯交接记录）。

```javascript
// 交接白板
function shiftBoard(shift) {
  return {
    todos: shift.todos, abnormal: shift.abnormalEvents,
    carryover: shift.carryoverItems,                   // 遗留问题高亮
    ack: (item) => api('/board/ack', { item: item.id, by: currentUser() }),
    archive: () => api('/board/archive', { shift: shift.id }),
  };
}
```
