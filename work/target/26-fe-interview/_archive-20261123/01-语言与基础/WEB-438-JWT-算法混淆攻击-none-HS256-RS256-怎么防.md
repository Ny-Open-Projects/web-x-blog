---
title: [WEB-438] JWT 算法混淆攻击（none/HS256-RS256）怎么防
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-438：JWT 算法混淆攻击怎么防

**答**：
- 攻击一 alg:none：老库允许 header.alg = none 时跳过验签，攻击者把 payload 改成 admin 后直接过
- 攻击二 RS256→HS256：服务端代码用公钥当 HMAC 密钥验签，而公钥是公开的，攻击者自己也能签出合法 token
- 防御：服务端白名单写死算法（如只允许 RS256），解析 header 后校验 alg 在白名单内，其余拒绝
- 附加检查：kid 参数可能引发路径穿越/SQL 注入（有的库拿 kid 查密钥文件），要过滤
- 前端角色：不必解业务 JWT，但接入第三方登录时可提醒后端「验签库版本与算法白名单」

```javascript
// 后端伪代码：算法白名单
const payload = jwt.verify(token, PUBLIC_KEY, {
  algorithms: ['RS256'],   // 不写这个参数 = 允许 header 任意算法，等于裸奔
  issuer: 'https://auth.example.com',
  audience: 'web-app',
});
```
