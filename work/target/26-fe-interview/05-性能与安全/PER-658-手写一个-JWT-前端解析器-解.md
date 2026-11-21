---
title: [PER-658] 手写一个 JWT 前端解析器：解码 payload、本地预判过期、按需静默刷新（不引第三方库）
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-658：手写一个 JWT 前端解析器：解码 payload、本地预判过期、按需静默刷新（不引第三方库）

**答**：
- JWT 三段 base64url：header.payload.signature；前端不需要验签（那是服务端的事），只做解码与过期预判——`exp`（秒级时间戳）对比本地时间。
- 要点：base64url 解码注意 padding；时钟偏差容忍（本地时间可能不准，预留 30 秒提前量）；刷新并发控制（多个请求同时发现过期，只发一次刷新，其余等待——用共享 promise）。
- 边界：payload 解析失败（非 JWT）直接抛错不猜；`iat/nbf` 也要校验；刷新失败的兜底（登出）。
- 评分点：并发刷新共享 promise。

```javascript

const b64uDecode = (s) => JSON.parse(atob(s.replace(/-/g, '+').replace(/_/g, '/')
  .padEnd(Math.ceil(s.length / 4) * 4, '=')) || '{}');
class JwtClient {
  constructor(refreshFn, { skewSec = 30 } = {}) { this.refresh = refreshFn; this.skew = skewSec; }
  parse(token) {
    const [h, p, sig] = token.split('.');
    if (!sig) throw new Error('not a jwt');
    const payload = b64uDecode(p);
    const expiredAt = payload.exp * 1000 - this.skew * 1000;   // 提前量
    return { payload, willExpire: Date.now() >= expiredAt, expiredAt: new Date(expiredAt) };
  }
  async ensureToken(getToken, setToken) {                       // 并发安全刷新
    const t = getToken();
    if (t && !this.parse(t).willExpire) return t;
    this._pending ??= this.refresh().finally(() => delete this._pending); // 共享刷新
    const fresh = await this._pending;
    setToken(fresh);
    return fresh;
  }
}
// 多个请求同时 401：第一个触发 refresh，其余 await 同一个 promise，不会刷风暴
```
