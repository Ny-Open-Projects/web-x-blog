---
title: [NODE-546] Node 服务的系统通知消息（官方账号/公告）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-546：系统通知消息
**答**:
- 系统通知形态：一对一通知（订单状态/审核结果——事务性通知 NODE-453/394）、公告广播（全员/按人群——亿级扇出）、官方会话（客服/官方号消息——IM 形态）。
- 广播扇出方案：写扩散（亿用户一人一条——存储爆炸不可行）→ 读扩散 + 用户水位（公告存公共表 + 用户已读水位——登录拉取未读公告列表）、增量拉取（公告 ID 游标——端上已读最大 ID 增量）、定向公告（按人群圈选——人群标签 join 公告列表）。
- 展示协议：公告分类（系统/营销/安全——用户可按类关闭偏好 ARC-523）、强提醒类（安全公告：置顶强提醒——产品分级）。
- 性能：公告发布风暴（全员公告发布瞬间查询洪峰——公告列表缓存 + 分批生效 NODE-438 预热思想）、已读水位存储优化（bitmap/区间压缩——亿级已读状态存储）。
- 合规：营销公告的退订与频控（NODE-453 频控——公告也是骚扰面）。
```javascript
// 读扩散公告
app.get('/notices', async (ctx) => {
  const since = ctx.query.since ?? 0;                            // 端上已读游标
  const list = await noticeRepo.publicAfter(since, { audience: await audienceOf(ctx.user) });
  return { items: list, cursor: list.at(-1)?.id };               // 公共表 + 游标：无写扩散
});
```
