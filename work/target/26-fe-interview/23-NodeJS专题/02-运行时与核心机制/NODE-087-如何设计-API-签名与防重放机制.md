---
title: [NODE-087] 如何设计 API 签名与防重放机制？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-087：如何设计 API 签名与防重放机制？
**答**：
- 适用：开放 API / 服务端对服务端（无浏览器 cookie 场景）。要素：`appKey`（标识）+ `appSecret`（密钥，不传输）+ 签名。
- 签名算法：按字典序排序所有参数 → 拼接 `k=v&` 串 + body 摘要 → `HMAC-SHA256(rawStr, appSecret)` → 放入 `X-Sign` 头。服务端用同样规则重算比对（时序安全比较）。
- 防重放三件套：**timestamp**（±5 分钟窗口，超窗拒绝）、**nonce**（随机串，Redis `SET NX EX 300` 去重，5 分钟内同 nonce 拒绝）、body 摘要参与签名（防篡改）。

```javascript
const crypto = require('node:crypto');

// 客户端签名
function signRequest(appKey, appSecret, params, body) {
  const timestamp = Date.now().toString();
  const nonce = crypto.randomBytes(8).toString('hex');
  const all = { ...params, appKey, timestamp, nonce };
  const canonical = Object.keys(all).sort()                 // 字典序
    .map((k) => `${k}=${all[k]}`).join('&');
  const bodyHash = crypto.createHash('sha256').update(body ?? '').digest('hex');
  const sign = crypto.createHmac('sha256', appSecret)
    .update(`${canonical}&body=${bodyHash}`).digest('hex');
  return { headers: { 'x-app-key': appKey, 'x-timestamp': timestamp, 'x-nonce': nonce, 'x-sign': sign } };
}

// 服务端校验中间件
const APP_SECRETS = { 'client-a': process.env.CLIENT_A_SECRET };

async function verifySign(ctx, next) {
  const appKey = ctx.get('x-app-key');
  const timestamp = ctx.get('x-timestamp');
  const nonce = ctx.get('x-nonce');
  const sign = ctx.get('x-sign');
  const secret = APP_SECRETS[appKey];
  if (!secret || !sign) ctx.throw(401, '非法客户端');

  // 1. 时间窗口：±5 分钟
  if (Math.abs(Date.now() - Number(timestamp)) > 5 * 60 * 1000) ctx.throw(401, '请求已过期');

  // 2. nonce 防重放：5 分钟内唯一
  const ok = await redis.set(`nonce:${appKey}:${nonce}`, '1', 'EX', 300, 'NX');
  if (!ok) ctx.throw(401, '重复请求');   // 重放攻击直接拒绝

  // 3. 重算签名比对
  const rawBody = ctx.state.rawBody ?? '';
  const bodyHash = crypto.createHash('sha256').update(rawBody).digest('hex');
  const all = { ...ctx.query, appKey, timestamp, nonce };
  const canonical = Object.keys(all).sort().map((k) => `${k}=${all[k]}`).join('&');
  const expected = crypto.createHmac('sha256', secret).update(`${canonical}&body=${bodyHash}`).digest('hex');
  const a = Buffer.from(expected), b = Buffer.from(sign);
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) ctx.throw(401, '签名校验失败');
  await next();
}
```
