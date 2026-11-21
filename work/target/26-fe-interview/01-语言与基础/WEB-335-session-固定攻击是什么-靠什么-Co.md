---
title: [WEB-335] session 固定攻击是什么？靠什么 Cookie 属性防住？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-335：session 固定攻击是什么？靠什么 Cookie 属性防住？
**答**：
- 攻击：攻击者先拿到一个 session id，诱导受害者用该 id 登录，登录后攻击者用同一 id 即冒充受害者。
- 防御核心：登录成功后服务端重新生成 session id（session regeneration），旧 id 全作废。
- 配套：HttpOnly 防脚本改写 Cookie、SameSite 限制跨站携带、token 类方案里对应"登录后重签 jti"。

```javascript
// 登录成功 → 强制换 session
app.post('/login', (req, res) => {
  const user = auth(req.body);
  req.session.regenerate(err => {          // 新 id，旧的作废
    req.session.userId = user.id;
    res.cookie('sid', req.session.id, { httpOnly: true, sameSite: 'strict' });
  });
});
console.log('固定攻击的本质是"id 复用"， regeneration 一招毙命');
```
