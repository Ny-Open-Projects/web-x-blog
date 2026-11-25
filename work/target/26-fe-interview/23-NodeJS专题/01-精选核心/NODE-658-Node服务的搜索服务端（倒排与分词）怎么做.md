---
title: [NODE-658] Node 服务的搜索服务端（倒排/分词/相关性）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-658：搜索服务端怎么做？
**答**：
- 索引层：ElasticSearch/MeiliSearch（倒排索引——分词后 term→doc 映射）；中文分词（IK/jieba——分词质量决定召回）；索引更新链路（业务写入 → MQ → 索引同步——延迟可控，SCN-NODE-651 消费幂等）。
- 查询层：查询解析（用户输入 → 分词 → bool 组合）、相关性排序（BM25 + 业务加权——点击率/新近度）、结果裁剪与高亮。
- 与 DB 检索的分工：DB like 查询（小数据精确匹配）vs ES（全文+聚合+排序）——数据量/查询模式决定选型，不盲目 ES 化。
- Node 的角色：搜索网关（鉴权/限流/聚合/结果加工——ES 直连客户端是安全负债，SCN-NODE-649 鉴权中间件统一）。
- 追问钩子：为什么「索引同步走 MQ 而不是双写」——双写（DB 写完写 ES）在 ES 故障时数据丢失（双写无事务）；MQ 解耦让 ES 故障时消息积压（恢复后追平）——最终一致 + 可靠投递（SCN-NODE-653 本地消息表模式），索引延迟秒级可接受。

```javascript
// 索引同步（MQ 消费）
consumer.run({ eachMessage: async ({ message }) => {
  const { action, doc } = JSON.parse(message.value);
  action === 'upsert' ? await es.index({ index: 'goods', id: doc.id, document: doc })
                      : await es.delete({ index: 'goods', id: doc.id });
}});
// 搜索网关
app.get('/search', auth(), rateLimit(), async (req, res) => {
  const q = await es.search({ index: 'goods', body: buildQuery(req.query) });
  res.json(hydrate(q.hits, { highlight: true }));      // 结果加工
});
```
