---
title: [AGT-470] 笔试题——实现开放 API 网关（签名校验+分级限流+审计）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-470：手写 API 网关：HMAC 签名验签、重放防护、多级限流、审计

**需求与边界**：
- 输入：请求（headers 含签名）、API Key 配置；输出：放行或拒绝。
- 边界要求：① HMAC-SHA256 签名（含时间戳+路径+body hash）校验；② 重放防护（时间窗+nonce 去重）；③ 三级限流（全局/租户/key）；④ 拒绝原因标准化（429/401 带重试头）。

**答**：
```javascript
async function gateway(req, { keys, limiter }) {
  const { authorization, x-timestamp: ts,
    x-nonce: nonce } = headers(req);
  const key = keys.get(extractKeyId(authorization));
  if (!key) return reject(401, 'INVALID_KEY');
  // 1. 时间窗（±300s）+ nonce 防重放
  if (Math.abs(Date.now() - +ts) > 300e3)
    return reject(401, 'TIMESTAMP_SKEW');
  if (await limiter.seenNonce(key.id, nonce))
    return reject(401, 'REPLAY_DETECTED');
  // 2. HMAC 验签：method+path+ts+nonce+bodyHash
  const bodyHash = sha256(rawBody(req));
  const expected = hmacSha256(key.secret,
    [req.method, req.path, ts, nonce, bodyHash].join('\n'));
  if (!timingSafeEqual(expected, extractSig(authorization)))
    return reject(401, 'BAD_SIGNATURE');
  // 3. 三级限流：全局→租户→key
  const checks = [
    ['global', 'GLOBAL_LIMIT'],
    ['tenant:' + key.tenantId, 'TENANT_LIMIT'],
    ['key:' + key.id, 'KEY_LIMIT']];
  for (const [bucket, code] of checks) {
    const r = await limiter.check(bucket, key.tier);
    if (!r.ok) return reject(429, code,
      { 'Retry-After': r.retryAfter,               // 重试头
        'X-RateLimit-Remaining': r.remaining });
  }
  await limiter.markNonce(key.id, nonce, 600e3);  // nonce 记账
  await audit({ keyId: key.id, path: req.path,
    tenant: key.tenantId });
  return pass(req);
}
// timingSafeEqual 防时序攻击；tier 决定各桶限额。
```

**评分点**:
- HMAC 签名覆盖（method+path+ts+nonce+bodyHash）完整，timingSafeEqual 防时序攻击。
- 重放双重防护：时间窗+nonce 去重（用后记账）。
- 三级限流顺序检查，429 带 Retry-After（客户端友好）。
- 审计含 key/tenant/path 可归因。
