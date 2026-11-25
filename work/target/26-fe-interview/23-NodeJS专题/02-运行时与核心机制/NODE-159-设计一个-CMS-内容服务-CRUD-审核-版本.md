---
title: [NODE-159] 设计一个 CMS 内容服务（CRUD/审核/版本）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-159：设计一个 CMS 内容服务（CRUD/审核/版本）？
**答**：
- 数据模型：article 主表（当前态）+ article_version 版本表（每次发布快照）+ review_record 审核记录表。
- 状态机：draft → in_review → published → archived，非法流转直接 400；已发布内容改稿走"新版本 + 重新审核"，线上内容不中断。
- 并发编辑用**乐观锁**（version 字段 CAS）；发布成功发事件触发 CDN 预热与搜索索引更新。
- 敏感内容先过审核服务（NODE-096），审核通过才允许 publish。

```javascript
const TRANSITIONS = {
  draft: ['in_review'],
  in_review: ['published', 'draft'],   // 审核驳回退回草稿
  published: ['archived'],
  archived: ['draft'],
};

app.post('/cms/articles/:id/publish', auth('editor'), async (ctx) => {
  const article = await db.$transaction(async (t) => {
    const a = await t.article.findUnique({ where: { id: ctx.params.id } });
    if (!TRANSITIONS[a.status]?.includes('published')) ctx.throw(400, '状态机不允许发布');
    if (a.version !== ctx.request.body.baseVersion) ctx.throw(409, '内容已被他人修改'); // 乐观锁
    await t.articleVersion.create({     // 发布即快照，可回溯可回滚
      data: { articleId: a.id, version: a.version + 1, snapshot: a.content },
    });
    return t.article.update({
      where: { id: a.id },
      data: { status: 'published', version: { increment: 1 }, publishedAt: new Date() },
    });
  });
  await mq.publish('cms.article.published', article); // 触发 CDN 预热/搜索索引
  ctx.body = article;
});
```
