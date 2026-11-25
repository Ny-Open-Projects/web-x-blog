---
title: [SCN-1233] AI 对话的会话列表管理（置顶/归档/自动命名）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1233：AI 对话的会话列表管理（置顶/归档/自动命名）

**答**：
- 管理：会话列表（置顶/归档/删除），自动命名（首条消息摘要生成）。
- 分组：按时间分组（今天/昨天/更早），搜索定位（1220）。
- 同步：多端会话列表同步（lastMsg 预览）。

```javascript
// 会话列表
function sessionListGroup(sessions) {
  const group = s => Date.now() - s.lastAt < 86400_000 ? '今天'
    : Date.now() - s.lastAt < 2 * 86400_000 ? '昨天' : '更早';
  return groupBy(sessions, group).map(([g, list]) => ({
    group: g, sessions: list.sort((a, b) => b.lastAt - a.lastAt)
      .map(s => ({ ...s, title: s.title ?? s.firstMsg.slice(0, 20) })),
  }));
}
function groupBy(arr, fn) { const m = new Map(); arr.forEach(x => { const k = fn(x); (m[k] ??= []).push(x); }); return [...m.entries()]; }
```
