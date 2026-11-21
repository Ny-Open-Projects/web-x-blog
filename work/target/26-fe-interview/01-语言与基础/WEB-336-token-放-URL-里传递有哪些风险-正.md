---
title: [WEB-336] token 放 URL 里传递有哪些风险？正确的做法是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-336：token 放 URL 里传递有哪些风险？正确的做法是什么？
**答**：
- URL 会进：浏览器历史、服务器访问日志、Referer 头、代理/网关日志、收藏夹——任何一环都可能泄露 token。
- OAuth 回调的授权码必须"一次性 + 短时效"就是为了缓解 URL 暴露面；换成 token 则不可接受。
- 正确做法：凭证放 Authorization 头或 HttpOnly Cookie；确实需要链接凭证（邮件激活）时用一次性短时 token。

```javascript
// 反面: /api/data?token=eyJhbG...（进日志/Referer）
fetch('/api/data', { headers: { Authorization: 'Bearer ' + token } });
// 确需 URL 凭证：一次性 action token
const link = '/activate?uid=1&sig=' + oneTimeToken({ ttl: 600, once: true });
console.log('URL 凭证只做"一次性动作"，不做"会话凭证"');
```
