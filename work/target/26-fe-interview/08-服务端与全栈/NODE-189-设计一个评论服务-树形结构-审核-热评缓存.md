---
title: [NODE-189] 设计一个评论服务（树形结构/审核/热评缓存）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-189：设计一个评论服务（树形结构/审核/热评缓存）？
**答**：
- 树形存储用 **materialized path**：`path = 父path + '/' + id`，查整个子树 = `WHERE path LIKE 'root/123/%'`，比递归 CTE 简单且索引友好。
- 发表链路：入库 status=PENDING → 敏感词/机审（NODE-096）→ 通过置 VISIBLE 并失效热评缓存；举报走异步人工复核。
- 读路径：热评列表 Redis 缓存 60s（/articleId 维度）；计数（点赞）用 Redis INCR + 定时落库（NODE-190）。
- 防刷：同 uid 对同文章窗口限频 + 内容去重（hash 相似度）。

```javascript
// comment(id, article_id, parent_id, path, content, status, like_count)
app.get('/api/comments', async (ctx) => {
  const key = `comments:hot:${ctx.query.articleId}`;
  const hot = await redis.get(key);
  if (hot) return JSON.parse(hot);                    // 热评缓存 60s
  const rows = await db.comment.findMany({
    where: { articleId: ctx.query.articleId, status: 'VISIBLE', deletedAt: null },
    orderBy: { likeCount: 'desc' },
    take: 50,
  });
  await redis.setex(key, 60, JSON.stringify(rows));
  return rows;
});

// 子树查询：materialized path
const subtree = await db.comment.findMany({
  where: { path: { startsWith: `${rootComment.path}/` } }, // 一次查询取整个楼中楼
});
// 发表：status 先 PENDING，机审通过后置 VISIBLE + DEL 热评缓存
```
