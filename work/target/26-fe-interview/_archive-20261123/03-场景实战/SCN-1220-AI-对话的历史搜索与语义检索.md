---
title: [SCN-1220] AI 对话的历史搜索与语义检索
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1220：AI 对话的历史搜索与语义检索

**答**：
- 搜索：历史会话关键词搜索（全文）+ 语义搜索（向量检索"上次聊过的那个方案"）。
- 性能：向量检索服务端（前端防抖传参），结果高亮命中片段。
- 管理：会话归档/删除（含向量清理）。

```javascript
// 会话检索
async function searchHistory(q, { semantic = true } = {}) {
  const rows = await api('/history/search', { q, semantic });
  return rows.map(r => ({ ...r,
    snippet: highlight(r.matchText, q),
    score: r.score,
    type: semantic && r.vector ? '语义命中' : '关键词命中' }));
}
function highlight(text, q) {
  return text.replace(new RegExp(q, 'gi'), m => `<mark>${m}</mark>`);
}
```
