---
title: [WEB-221] JWT 的结构与校验流程？签名防篡改的原理？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-221：JWT 的结构与校验流程？签名防篡改的原理？

**答**：
- 结构三段：Header（算法）.Payload（claims）.Signature，均为 base64url，前两段是明文可解码——JWT 只防篡改不防偷看，敏感数据不能放 payload。
- 签名：`HMACSHA256(base64(header).base64(payload), secret)`。改任何一个字符，签名对不上，服务端直接 401。用 RS256 时用服务端私钥签、公钥验，支持多服务分布式验签。
- 校验流程：验签 → 查 exp/nbf 过期 → 查 aud/iss 是否本服务 → 通过后信任 payload 里的用户信息，不查库（这是无状态的优势也是风险——签发后无法撤回）。
- 常见漏洞：alg: none 攻击（不校验算法）、弱密钥被暴力破解、把用户角色放 payload 且前端信任。

```javascript
// 手写最小 JWT 校验（理解原理用，生产用 jsonwebtoken 库）
const crypto = require('crypto');
function verify(token, secret) {
  const [h, p, s] = token.split('.');
  const expect = crypto.createHmac('sha256', secret).update(`${h}.${p}`).digest('base64url');
  if (s !== expect) throw new Error('签名校验失败');
  const payload = JSON.parse(Buffer.from(p, 'base64url').toString());
  if (payload.exp * 1000 < Date.now()) throw new Error('已过期');
  return payload;
}
```

**评分点**：
- 能说出三段结构与 base64url
- 强调 payload 明文可读、不放敏感信息
- 明确 alg: none 攻击
- 指出无法主动撤回的局限
