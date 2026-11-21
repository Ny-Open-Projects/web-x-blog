---
title: [NODE-130] JWT 的算法混淆攻击（alg none / RS256→HS256）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-130：JWT 的算法混淆攻击（alg none / RS256→HS256）？
**答**：
- 攻击一：把 header 的 `alg` 改为 `none` 并去掉签名——若 verify 不指定算法白名单，旧版本库"信 header 不信配置"直接放行。
- 攻击二：服务端用 RS256 公钥当 HMAC 密钥验证 HS256 token——公钥人人可得，攻击者可自签任意 token。
- 防御核心：**`algorithms` 白名单硬编码**，与签发侧算法严格一致；密钥分离管理（私钥只在签发方）。
- 附加校验：`issuer/audience` 断言、`clockTolerance` 容忍时钟偏移、kid 参数视为不可信输入（防注入）。

```javascript
const jwt = require('jsonwebtoken');

// 正确姿势：白名单 + 声明断言
function verifyAccess(token) {
  return jwt.verify(token, PUBLIC_KEY, {
    algorithms: ['RS256'],          // 关键：显式白名单，none/HS256 一律拒绝
    issuer: 'auth.example.com',
    audience: 'bff',
    clockTolerance: 5,              // 5s 时钟偏移容忍
  });
}

// 反例一（禁止）：jwt.verify(token, PUBLIC_KEY) —— 未限制 algorithms
// 反例二（禁止）：按 header.alg 动态选密钥/算法
// const alg = jwt.decode(token).header.alg; // 解码结果不可信，绝不能作为验证依据

// 网关层统一校验 + 传递身份；业务层只信网关注入的 ctx.state.uid
```
