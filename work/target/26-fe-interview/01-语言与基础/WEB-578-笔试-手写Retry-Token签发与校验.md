---
title: [WEB-578] 笔试：手写 QUIC Retry Token 签发与校验
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-578：笔试：手写 QUIC Retry Token 签发与校验

**答**：实现 Retry token 的应用层模拟（理解机制）：① `issue(ipPrefix, ts, secretKey)`：对 `ipPrefix + ts` 计算 HMAC 签名，token = base64(ts) + '.' + base64(hmac)；② `verify(token, ipPrefix, secretKey, ttlMs)`：拆包重算 HMAC（恒定时间比较）、校验 ts 未过期、IP 前缀匹配；③ 三项任一失败返回 false；④ 说明多实例部署时密钥共享的必要性与恒定时间比较防的攻击。Node 环境实现。

```javascript
const crypto = require('crypto');

function issue(ipPrefix, ts, secretKey) {
  const mac = crypto.createHmac('sha256', secretKey)
    .update(`${ipPrefix}|${ts}`).digest();
  return Buffer.from(String(ts)).toString('base64') + '.' + mac.toString('base64');
}

function verify(token, ipPrefix, secretKey, ttlMs = 30_000) {
  const [tsB64, macB64] = token.split('.');
  if (!tsB64 || !macB64) return false;
  const ts = Number(Buffer.from(tsB64, 'base64').toString());
  if (!Number.isFinite(ts)) return false;
  if (Date.now() - ts > ttlMs) return false;          // 过期
  const expect = crypto.createHmac('sha256', secretKey)
    .update(`${ipPrefix}|${ts}`).digest();
  const given = Buffer.from(macB64, 'base64');
  if (given.length !== expect.length) return false;
  return crypto.timingSafeEqual(given, expect);       // 恒定时间比较
}

console.log(verify(issue('203.0.113.', Date.now(), 'k'), '203.0.113.', 'k')); // true
```

**评分点**：
- HMAC 覆盖「IP 前缀 + 时间戳」，理解 token 必须绑定地址防搬运重放
- 校验用 `timingSafeEqual` 恒定时间比较，说清防时序侧信道
- TTL 校验防旧 token 长期有效；格式异常有防御不抛异常
- 指出多实例必须共享 secretKey，否则 LB 路由到不同实例验证失败
