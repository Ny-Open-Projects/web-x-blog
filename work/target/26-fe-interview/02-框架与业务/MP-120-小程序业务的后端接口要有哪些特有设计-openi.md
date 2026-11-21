---
title: [MP-120] 小程序业务的后端接口要有哪些特有设计（openid/unionid 维度）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-120：小程序业务的后端接口要有哪些特有设计（openid/unionid 维度）？
**答**：
- 接口鉴权以**自有 token → userId** 为准，openid/unionid 只在用户体系表做映射；unionid 用于打通多端（公众号/小程序/App）。
- 幂等设计全面化：下单/支付回调/领券都要幂等键（小程序网络不稳、用户重复点击是常态）。
- 接口要区分**场景值与来源渠道**（渠道号/分享链路参数），便于拉新归因。
- 响应体按小程序特性裁剪：首屏合并接口（BFF 聚合）、分页游标化、大字段（列表详情）拆分按需拉取。
- 服务端要校验 formId/订阅消息配额、频率限制（小程序端无浏览器防护层）。

```javascript
// BFF 聚合接口设计：首页一次拉全
router.post('/api/mp/home/aggregate', auth, async (req, res) => {
  const userId = req.auth.userId        // 由统一 token 解出，而非 openid
  const [user, banner, feed, couponCount] = await Promise.all([
    userService.summary(userId),
    cmsService.banners(req.query.scene),   // scene 为场景值/渠道参数，用于归因
    feedService.firstPage(userId, { cursor: req.query.cursor }),
    couponService.usableCount(userId)
  ])
  res.json({
    code: 0,
    data: { user: { nick: mask(user.nick), level: user.level }, banner, feed, couponCount },
    nextCursor: feed.cursor   // 游标分页
  })
})
```
