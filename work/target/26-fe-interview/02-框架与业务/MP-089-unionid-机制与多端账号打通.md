---
title: [MP-089] unionid 机制与多端账号打通？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-089：unionid 机制与多端账号打通？
**答**：
- 同一用户在同一**微信开放平台账号**下的不同应用（公众号/小程序/APP）openid 不同，但 **unionid 相同**。
- 获取途径：绑定开放平台后，code2Session 直接返回 unionid（满足条件时）；或通过公众号 unionid 机制/开放数据解密。
- 打通模式：以 unionid 为中心建统一用户表，各端 openid 作为端内标识映射到同一账号。

```javascript
// 云函数中获取 openid 与 unionid
const { OPENID, UNIONID, APPID } = cloud.getWXContext()
// UNIONID 存在条件：小程序已绑定到微信开放平台账号
await db.collection('users').add({
  data: { unionid: UNIONID, weappOpenid: OPENID, source: 'weapp' }
})
```
