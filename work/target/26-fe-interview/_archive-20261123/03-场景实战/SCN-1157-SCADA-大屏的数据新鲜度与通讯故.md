---
title: [SCN-1157] SCADA 大屏的数据新鲜度与通讯故障显示
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1157：SCADA 大屏的数据新鲜度与通讯故障显示

**答**：
- 新鲜度：每个点位数据带时间戳/质量戳——数据过期（> 10s 未更新）标"通讯故障"（黄色闪烁）。
- 分组：采集链路分组展示（PLC1/PLC2 通讯状态），链路断整体置灰。
- 恢复：通讯恢复自动解除（恢复时间记录）。

```javascript
// 通讯故障
function commsHealth(tags, { staleMs = 10_000 } = {}) {
  const now = Date.now();
  const byLink = groupBy(tags, t => t.linkId);
  return Object.entries(byLink).map(([link, list]) => {
    const stale = list.filter(t => now - t.ts > staleMs);
    return { link,
      state: stale.length === list.length ? 'link-down'
        : stale.length ? 'partial' : 'ok',
      staleTags: stale.map(t => t.id),
      since: stale.length ? Math.min(...stale.map(t => t.ts)) : null };
  });
}
function groupBy(arr, fn) { const m = {}; arr.forEach(x => { const k = fn(x); (m[k] ??= []).push(x); }); return m; }
```
