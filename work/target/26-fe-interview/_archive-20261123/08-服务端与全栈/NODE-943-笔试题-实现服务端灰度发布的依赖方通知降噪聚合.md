---
title: [NODE-943] 笔试题——实现发布通知降噪聚合（事件→摘要卡片）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-943：手写通知聚合

**需求与边界**：
- 需求：通知聚合（SCN-OPS-320/612）——① 事件窗口聚合（放量步进合并——SCN-OPS-320）；② 关键穿透（回滚/熔断——SCN-OPS-320）；③ 摘要卡片（IM——SCN-OPS-325）；④ 聚合的配置（窗口/穿透规则——SCN-OPS-320）。
- 边界：① 穿透清空窗口（SCN-OPS-320）；② 聚合计数（SCN-联想-320）；③ 窗口的优先级分级（SCN-OPS-320）。

**答**：
```javascript
const bus = createNotifyDeduper({ windows: { low: 864e5, mid: 3600e3 } });   // SCN-OPS-320
releaseEvents.on('gray-advance', (e) => bus.push(e, { priority: 'low', channel: 'im' }));   // 合并
releaseEvents.on('rollback', (e) => bus.push(e, { priority: 'high', channel: 'im' }));   // 穿透（清空窗口）
// 摘要卡片（SCN-OPS-325）
bus.onDigest((channel, summary) => imCard({ title: `发布摘要 ×${summary.count}`,
  events: summary.events, links: { board: releaseBoardUrl(summary.releaseId) } }));
```

**评分点**:
- 窗口分级（low/mid/high——SCN-OPS-320）。
- 关键穿透清空窗口（SCN-OPS-320）。
- IM 卡片（SCN-OPS-325）。
- 聚合计数（SCN-联想-320）。
