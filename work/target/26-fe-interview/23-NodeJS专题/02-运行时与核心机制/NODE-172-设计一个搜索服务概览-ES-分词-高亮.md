---
title: [NODE-172] 设计一个搜索服务概览（ES 分词/高亮）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-172：设计一个搜索服务概览（ES 分词/高亮）？
**答**：
- 索引设计：中文分词 `ik_max_word`（索引细切提高召回）+ `ik_smart`（查询粗切防过度拆分）；过滤字段用 keyword 不分词。
- 查询要点：`multi_match` 多字段 + 标题权重 `title^3`；过滤条件放 **filter 子句**（不算分且可缓存）；深分页用 `search_after` 而非 from+size。
- 高亮：highlight 返回 `<em>` 包裹片段，前端渲染必须防 XSS（按富文本处理，NODE-057）。
- 写入链路：binlog/MQ → 异步更新索引（最终一致）；重建索引用别名切换（零停机）。

```javascript
const mapping = {
  properties: {
    title: { type: 'text', analyzer: 'ik_max_word', search_analyzer: 'ik_smart' },
    content: { type: 'text', analyzer: 'ik_max_word' },
    status: { type: 'keyword' },       // 过滤字段不分词
    publishedAt: { type: 'date' },
  },
};

async function search(q, { page = 1 } = {}) {
  const { hits } = await es.search({
    index: 'articles',
    body: {
      query: { bool: {
        must: [{ multi_match: { query: q, fields: ['title^3', 'content'],
          type: 'best_fields', fuzziness: 'AUTO' } }],
        filter: [{ term: { status: 'published' } }],  // filter 不算分且可缓存
      }},
      highlight: {
        fields: { title: {}, content: { fragment_size: 80 } },
        pre_tags: ['<em>'], post_tags: ['</em>'],
      },
      sort: [{ _score: 'desc' }, { publishedAt: 'desc' }],
      search_after: page > 1 ? cursorOf(page) : undefined, // 深分页用 search_after
      size: 20,
    },
  });
  return hits.hits.map((h) => ({ id: h._id, score: h._score, ...h._source, hl: h.highlight }));
}
```
