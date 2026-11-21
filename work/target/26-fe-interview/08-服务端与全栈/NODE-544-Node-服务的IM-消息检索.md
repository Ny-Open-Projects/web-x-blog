---
title: [NODE-544] Node 服务的 IM 消息检索（会话内/全局搜索）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-544：IM 消息检索
**答**:
- 检索范围：会话内搜索（当前会话历史）、全局搜索（所有会话找消息）、按发送者/时间/类型过滤——搜索服务（ES）索引消息（NODE-387 同步链路）。
- 索引设计：会话隔离（索引按会话过滤——权限：只能搜到自己有权会话的消息——查询必带会话权限过滤）、索引字段（内容全文 + sender/时间/类型过滤字段 + 撤回状态（撤回消息不入索引））。
- 权限与隐私：检索权限与会话权限一致（群成员变动——退群后搜不到该群）、敏感内容过滤（合规：命中敏感词的消息不入索引或单独标记 ARC-456）、用户删除语义（用户"删除本地"≠ 服务端漫游删除——语义明确：服务端保留（漫游/合规）用户端不可见）。
- 体验：结果高亮与定位（点击结果 → 定位到原消息——seq 定位 ARC-594 锚点思路）、按时间跳转（"在 2026-11-01 附近查找"——时间范围检索）。
- 性能：全局搜索限流（重查询——配额保护 NODE-360）、大群检索性能（索引分片按会话）。
```javascript
// 消息检索（权限内）
app.get('/search/messages', async (ctx) => {
  const allowed = await convIdsOf(ctx.user);                     // 有权会话集合
  const r = await es.search({ index: 'im-msg', body: {
    query: { bool: { must: [{ match: { content: ctx.query.kw } }],
      filter: [{ terms: { convId: allowed } }, { term: { recalled: false } }] } },
    highlight: { fields: { content: {} } } } });                 // 高亮 + 权限过滤
});
```
