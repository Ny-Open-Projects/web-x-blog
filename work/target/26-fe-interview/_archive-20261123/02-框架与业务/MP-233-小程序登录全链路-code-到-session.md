---
title: [MP-233] 小程序登录全链路：code 到自建 session 的完整流程？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-233：登录全链路（code → session）？
**答**：
- ① wx.login 拿 code（5 分钟有效、一次性）。② code + appid 传自建服务端 → 服务端调 code2Session 换 openid/session_key。③ 服务端签发自定义 session token（自建用户体系绑定 openid），set-cookie 或返回 token。④ 后续请求带 token，服务端鉴权。⑤ session_key 丢失（用户重登）→ 重新 login。
- 误区：session_key 不能下发给前端（安全红线，解密敏感数据用）；openid 唯一标识用户但不是凭证。
- UnionID：多端（小程序+公众号+App）同一主体用 unionid 打通——绑定开放平台后返回。
- 会话续期：token 过期无 refresh 机制（小程序无 refresh_token）——静默重登（wx.login 无感）封装在请求层 401 拦截。
