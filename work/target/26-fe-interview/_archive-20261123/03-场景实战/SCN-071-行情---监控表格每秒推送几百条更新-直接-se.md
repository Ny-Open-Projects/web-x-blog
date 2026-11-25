---
title: [SCN-071] 行情 / 监控表格每秒推送几百条更新，直接 setState 导致渲染风暴，如何合并更新？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-071：行情 / 监控表格每秒推送几百条更新，直接 setState 导致渲染风暴，如何合并更新？
**答**：
- 推送只写 buffer（同一行多次推送自然合并为最新值），用 requestAnimationFrame 节流，每帧最多 flush 一次、整批通知一次。
- 行组件 memo + version 字段比较，只有数据真变化的行重渲染，其余行零开销。
- 涨跌闪烁等视觉效果交给 CSS 动画（改 class），不进 JS 渲染路径。

```javascript
// 高频推送合并：数据写 buffer，requestAnimationFrame 批量 flush
class LiveTableStore {
  rows = new Map();
  buffer = new Map();            // rowId -> 新数据，同行多次推送只留最新
  scheduled = false;
  listeners = new Set();

  push(updates) {                // ws 每秒数百条只写缓存不渲染
    for (const u of updates) {
      this.buffer.set(u.id, { ...this.rows.get(u.id), ...u, version: (u.version ?? 0) + 1 });
    }
    this.scheduleFlush();
  }
  scheduleFlush() {
    if (this.scheduled) return;
    this.scheduled = true;
    requestAnimationFrame(() => {          // 一帧最多渲染一次
      this.scheduled = false;
      this.rows = new Map([...this.rows, ...this.buffer]);
      this.buffer.clear();
      this.listeners.forEach((fn) => fn([...this.rows.values()]));  // 整批通知一次
    });
  }
}

// 行组件 memo：version 不变的行零重渲染
const Row = React.memo(({ row }) => (
  <tr data-flash={row.direction}>        {/* 涨跌闪烁交给 CSS 动画 */}
    <td>{row.price}</td>
  </tr>
), (prev, next) => prev.row.version === next.row.version);
```
