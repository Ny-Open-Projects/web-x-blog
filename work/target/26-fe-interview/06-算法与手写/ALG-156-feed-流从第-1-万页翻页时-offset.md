---
title: [ALG-156] feed 流从第 1 万页翻页时，offset 方案越来越慢还可能漏数据。游标分页为什么能解决？前端如何实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-156：feed 流从第 1 万页翻页时，offset 方案越来越慢还可能漏数据。游标分页为什么能解决？前端如何实现？
**答**：offset（`LIMIT 100000, 20`）要让存储引擎扫过并丢弃前 10 万条，且翻页期间有写入会漏/重；游标把"上一页最后一条的排序键"作为下一次查询的起点条件，走索引直接定位，O(log n + pageSize) 恒定，且写入不影响（按序推进）。前端实现：每页响应带 `nextCursor`，请求时原样带回，用户跳页能力需另行设计（或用页号到游标的映射缓存）。

```javascript
// offset 分页：LIMIT 100000, 20 —— 扫过 10 万条丢弃，越深越慢，写入还会漏/重
// 游标分页：WHERE (sort_key, id) < (cursor) ORDER BY sort_key DESC, id DESC LIMIT 20
function buildCursorQuery(lastItem, pageSize = 20) {
  const params = new URLSearchParams({ limit: pageSize });
  if (lastItem) {
    // 游标 = 排序键 + 唯一 id，防同刻重复导致漏行
    params.set('cursor', encodeURIComponent(JSON.stringify({
      sk: lastItem.createdAt,
      id: lastItem.id,
    })));
  }
  return `/api/feed?${params}`;
}
function decodeCursor(cursor) {
  return cursor ? JSON.parse(decodeURIComponent(cursor)) : null;
}
// 消费方：const next = buildCursorQuery(page.items.at(-1))
```
