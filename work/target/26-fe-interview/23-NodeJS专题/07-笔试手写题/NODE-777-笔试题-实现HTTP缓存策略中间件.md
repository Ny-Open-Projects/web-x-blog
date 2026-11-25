---
title: [NODE-777] 笔试题——实现 HTTP 缓存策略中间件（分级 + Vary 校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-777：手写缓存策略

**需求与边界**：
- 需求：HTTP 缓存中间件（SCN-NODE-692）——① 策略分级（public/private/no-store——按接口声明）；② ETag 协商（304——动态内容轻量缓存）；③ Vary 自动校验（响应依赖的请求头强制 Vary——灰度/端 profile 漏 Vary 告警）；④ 授权响应强制 private（越权缓存防线）。
- 边界：① 弱 ETag（动态内容——内容微变不失效）；② Vary 漏配检测（灰度桶参与响应但未 Vary——自动化校验，SCN-OPS-216）；③ 304 的成本（ETag 计算开销 vs 传输节省——大响应才值得）。

**答**：
```javascript
function cachePolicy(rules) {
  return (req, res, next) => {
    const rule = rules[req.route?.path] ?? { level: 'private', maxAge: 0 };
    if (req.headers.authorization && rule.level === 'public')
      rule.level = 'private';                          // 授权响应强制 private（越权缓存防线）
    res.setHeader('Cache-Control',
      rule.level === 'no-store' ? 'no-store'
        : `${rule.level}, max-age=${rule.maxAge}${rule.immutable ? ', immutable' : ''}`);
    if (rule.etag && ['POST', 'GET'].includes(req.method)) onEtag(res, body =>
      res.setHeader('ETag', `W/"${sha256(body).slice(0, 16)}"`));   // 弱 ETag
    next();
  };
}
// Vary 漏配校验（SCN-OPS-216）
res.on('finish', () => {
  if (req.grayBucket && !res.getHeader('Vary')?.includes('X-Gray-Bucket'))
    alert({ type: 'VARY_MISSING', path: req.path });   // 灰度参与但未 Vary——串缓存风险
});
```

**评分点**:
- 授权响应强制 private（越权缓存防线——SCN-NODE-692 红线）。
- 弱 ETag 协商（304——动态内容）。
- Vary 漏配自动化校验（灰度桶——SCN-OPS-216 贯穿联动）。
- 策略分级声明（public/private/no-store per 路由）。
