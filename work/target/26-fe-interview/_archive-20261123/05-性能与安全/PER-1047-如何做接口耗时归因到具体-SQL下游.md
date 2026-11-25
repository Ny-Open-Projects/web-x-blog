---
title: [PER-1047] 如何做接口耗时归因到具体 SQL/下游服务的链路
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1047：如何做接口耗时归因到具体 SQL/下游服务的链路

**答**：
- 前提：traceId 贯穿（前端生成或网关注入）+ 各下游透传 + 统一采集（OpenTelemetry）。
- 前端可见：接口总耗时 + 各 span 时长（后端聚合接口返回 breakdown 或经查询平台获取）。
- 平台联动：性能平台的接口劣化告警直接附 trace 链接，前端不用追着后端要数据。
- 前端自查：串行请求链（A 完成才能发 B）的耗时累加是最常见的"后端正常但页面慢"。

```javascript
// 串行链耗时分析
function criticalPath(calls) {   // calls: [{ name, start, end, deps: [] }]
  const byName = Object.fromEntries(calls.map(c => [c.name, c]));
  function depth(c, seen = new Set()) {
    if (!c.deps.length || seen.has(c.name)) return c.end - c.start;
    seen.add(c.name);
    return Math.max(...c.deps.map(d => depth(byName[d], seen)),
      c.end - c.start);
  }
  return calls.map(c => ({ name: c.name, pathMs: Math.round(depth(c)) }))
    .sort((a, b) => b.pathMs - a.pathMs)[0];   // 关键路径最长的接口优先治理
}
```
