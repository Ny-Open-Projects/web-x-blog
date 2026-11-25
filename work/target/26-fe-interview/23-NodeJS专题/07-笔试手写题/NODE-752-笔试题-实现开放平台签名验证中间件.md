---
title: [NODE-752] 笔试题——实现开放平台签名验证中间件（防重放/防篡改）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-752：手写开放平台验签

**需求与边界**：
- 需求：开放平台验签（SCN-NODE-687）——① 签名验证（HMAC 参数摘要——时序安全比较 timingSafeEqual）；② 重放防御（nonce SETNX + 时间戳窗口）；③ appKey 状态校验（封禁/配额）；④ 错误区分（签名错/过期/重放——开发者可修）。
- 边界：① timingSafeEqual（防时序攻击——恒时比较）；② nonce 窗口与时间戳窗口一致（±5min——nonce TTL 同步）；③ body 摘要的规范化（排序后摘要——防参数顺序攻击）。

**答**：
```javascript
function verifySignature({ appKey, ts, nonce, sign, body }) {
  const app = apps[appKey];
  if (!app || app.banned) throw new AppError('AUTH-001', 'app 无效', { http: 401 });
  if (Math.abs(Date.now() - ts) > 5 * 60_000)
    throw new AppError('AUTH-002', '时间戳过期（±5min）', { http: 401 });   // 时间窗
  if (!(await redis.set(`nonce:${appKey}:${nonce}`, 1, 'PX', 5 * 60_000, 'NX')))
    throw new AppError('AUTH-003', '重复请求（nonce）', { http: 401 });   // 重放防御
  const digest = sha256(canonicalize(body));           // 参数规范化摘要（排序）
  const expected = hmac(app.secret, `${appKey}\n${ts}\n${nonce}\n${digest}`);
  if (!timingSafeEqual(Buffer.from(expected), Buffer.from(sign)))   // 恒时比较（防时序）
    throw new AppError('AUTH-004', '签名错误', { http: 401 });
  return app;                                          // { scopes, quota }
}
const canonicalize = (body) => JSON.stringify(
  Object.keys(body).sort().reduce((o, k) => (o[k] = body[k], o), {}));   // 排序防顺序攻击
```

**评分点**:
- 四层校验（appKey/时间窗/nonce/签名）错误码区分（开发者可修）。
- timingSafeEqual 恒时比较（防时序攻击）。
- nonce TTL 与时间窗一致（±5min——重放窗口闭合）。
- 参数规范化摘要（排序——防参数顺序攻击）。
