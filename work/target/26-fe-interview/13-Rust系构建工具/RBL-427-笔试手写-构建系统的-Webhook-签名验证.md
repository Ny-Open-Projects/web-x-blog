---
title: [RBL-427] 笔试：手写构建系统 Webhook 签名验证
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-427：手写 Webhook 签名验证
**答**：实现 `verifyWebhook(req, secret)`：1) 签名头：`X-Signature: t=<ts>,v1=<hmac>`——HMAC-SHA256(secret, `${ts}.${rawBody}`)；2) 防重放：ts 与当前差超 5 分钟拒绝；3) 时序安全比较（constant-time，防计时攻击）；4) 原始 body 校验（JSON 解析前先验签——解析后重签不等价）；5) 密钥轮换：支持多有效密钥（按 kid 头选择——旧密钥宽限期）；6) 返回 { ok, reason? }。

```javascript
import crypto from 'node:crypto'

const MAX_SKEW = 5 * 60 * 1000

function safeEqual(a, b) {
  const ba = Buffer.from(a), bb = Buffer.from(b)
  return ba.length === bb.length && crypto.timingSafeEqual(ba, bb)   // constant-time
}

export function verifyWebhook(rawBody, headers, secrets /* { kid: secret } */) {
  const sig = headers['x-signature']
  if (!sig) return { ok: false, reason: 'missing signature' }
  const parts = Object.fromEntries(sig.split(',').map((p) => p.split('=')))
  const ts = +parts.t, v1 = parts.v1, kid = headers['x-kid'] ?? 'default'
  if (!ts || !v1) return { ok: false, reason: 'malformed signature' }

  if (Math.abs(Date.now() - ts) > MAX_SKEW)
    return { ok: false, reason: 'timestamp skew (replay?)' }           // 防重放

  const secret = secrets[kid]
  if (!secret) return { ok: false, reason: `unknown kid ${kid}` }      // 轮换按 kid

  const expected = crypto.createHmac('sha256', secret).update(`${ts}.${rawBody}`).digest('hex')
  return safeEqual(expected, v1) ? { ok: true } : { ok: false, reason: 'signature mismatch' }
}

// 用法：必须在 JSON.parse 之前对 rawBody 验签（express 用 raw body 中间件）
```
**评分点**：
- 签名输入 = `${ts}.${rawBody}`（timestamp 参与——防签名重放）
- 时序安全比较（timingSafeEqual + 长度前置判断——计时攻击防护）
- 防重放时间窗（5 分钟偏移拒绝）
- kid 密钥轮换（多密钥宽限期——轮换不断流）
- 原始 body 验签时机（JSON 解析前——重解析后字节不等价）
