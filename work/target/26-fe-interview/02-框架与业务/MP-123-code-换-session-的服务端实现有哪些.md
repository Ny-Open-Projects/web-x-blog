---
title: [MP-123] code 换 session 的服务端实现有哪些安全要点（code 只能用一次）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-123：code 换 session 的服务端实现有哪些安全要点（code 只能用一次）？
**答**：
- `wx.login` 的 code **5 分钟有效且只能用一次**，服务端调用 `code2session` 必须幂等处理客户端重试（同 code 二次调用报 40029，直接返回缓存结果或要求重新 login）。
- session_key 属于**敏感凭证**：只能存在服务端，绝不能下发给前端（下发即泄露，官方明令禁止）。
- code2session 返回的 openid 做服务端身份，配合自签 token（JWT/自研）下发前端；token 要有过期与刷新。
- 接口必须校验 token 与 openid 的绑定关系，防止横向越权（用 A 的 token 操作 B 的数据）。

```javascript
// 服务端 code2session + 会话签发
const crypto = require('crypto')
app.post('/api/mp/login', async (req, res) => {
  const { code } = req.body
  if (this.inflight.has(code)) return res.json(this.inflight.get(code)) // code 重试幂等
  const url = `https://api.weixin.qq.com/sns/jscode2session?appid=${APPID}&secret=${SECRET}&js_code=${code}&grant_type=authorization_code`
  const { openid, session_key, unionid, errcode } = await fetchJSON(url)
  if (errcode) return res.status(401).json({ code: errcode })   // 40029 code 无效等
  // session_key 只存服务端，加密落库；前端只拿自签 token
  const token = jwt.sign({ uid: openid, t: Date.now() }, JWT_SECRET, { expiresIn: '7d' })
  await kv.set(`sk:${openid}`, encrypt(session_key), 86400 * 3)
  res.json({ token, expiresIn: 604800 })   // 不返回 session_key / openid 明文给非必要方
})
```
