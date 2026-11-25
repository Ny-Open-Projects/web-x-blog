---
title: [NODE-838] 笔试题——实现搜索查询构建器（bool 组合 + 权重）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-838：手写查询构建器

**需求与边界**：
- 需求：ES 查询构建器（SCN-NODE-658）——① 多条件 bool 组合（must/should/filter——SCN-联想-803 词源）；② 字段权重（multi_match boost——相关性）；③ 过滤器分离（filter 不算分——性能）；④ 分页与深度限制（SCN-NODE-696 游标 search_after）。
- 边界：① 用户输入的安全构建（注入防御——ES 查询注入参数化）；② 深分页限制（search_after 替代 from+size——ES 深分页限制）；③ 高亮与裁剪（SCN-联想-658 结果加工）。

**答**：
```javascript
function buildQuery({ q, filters, sort, after }) {
  const bool = {
    must: { multi_match: { query: q, fields: ['title^3', 'desc'],     // 字段权重（SCN-NODE-658）
      fuzziness: 'AUTO' } },
    filter: Object.entries(filters ?? {}).map(([f, v]) =>   // filter 不算分（性能）
      ({ term: { [f]: v } })),
  };
  return {
    query: { bool },
    sort: sort ?? [{ _score: 'desc' }, { ts: 'desc' }],
    search_after: after,                               // 深分页（SCN-NODE-696 游标）
    size: 20, highlight: { fields: { title: {}, desc: {} } },   // 高亮（SCN-联想-658）
  };
}
// 注入防御：用户输入只进参数位（term/multi_match query）——不拼接 DSL
```

**评分点**:
- bool 组合 + 字段权重（SCN-NODE-658 相关性）。
- filter 分离（不算分——ES 性能）。
- search_after 深分页（SCN-NODE-696 游标语义）。
- 注入防御（用户输入参数化——不拼 DSL）。
