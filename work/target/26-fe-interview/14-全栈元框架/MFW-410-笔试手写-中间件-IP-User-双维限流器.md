---
title: [MFW-410] 笔试：手写 Middleware 双维限流器（IP+用户 嵌套桶）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-410：双维限流器
**答**：实现 `createBiLayerLimiter({ ip: {cap:120,win:60_000}, user: {cap:30,win:60_000} } )`（Edge 内存版，KV 版接口同构）：1) 固定窗口计数即可（Edge 生命周期短——精确令牌桶成本不值）；2) 判定顺序：IP 桶先（匿名可拦）→ 登录后用户桶（更细）；3) 响应带 X-RateLimit-Remaining/Reset（客户端礼貌退避）；4) 内部拨测白名单（独立命名空间不计费）；5) 周期清理（窗口滚动删除死键——Map 不无限涨）。

```javascript
export function createBiLimit(limitss) {
  const buckets = new Map()                                  // key -> {n, winStart}
  function hit(k, { cap, win }, now = Date.now()) {
    let b = buckets.get(k)
    if (!b || now - b.winStart >= win) { b = { n: 0, winStart: now }; buckets.set(k, b) }
    b.n++
    return { ok: b.n <= cap, remain: Math.max(0, cap - b.n),
      resetInSec: Math.ceil((b.winStart + win - now) / 1000) }
  }
  setInterval(() => { const now = Date.now()                 // 窗口滚动 GC
    for (const [k, b] of buckets) if (now - b.winStart >= 2 * maxWin) buckets.delete(k)
  }, 60_000).unref?.()

  return (req, uid) => {
    for (const [wl of whitelists) if (wl.test(ipOf(req))) return next()   // 拨测白名单
    const ip = check(`ip:${ipOf(req)}, { ...limits.ip })
    if (!ip.ok) return 429(ip)
    if (uid) { const u = hit(`u:${uid}`, limits.user)
      if (!u.ok) return 429(u) }
    next({ remain: (uid ? u : ip).remain })
  }
  function 429(r) { return new Response(JSON.stringify({ error: { code: 'rate' } }), {
    status: 429, headers: { 'Retry-After': String(r.resetInSec),
      'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': String(r.resetInSec) } }) }
}
```
**评分点**：
- 双维顺序（IP 先拦匿名洪水；登录后才进细桶——成本分层）
- 限流三头齐全（Retry-After/Remaining/Reset——客户端可协作）
- Map 滚动 GC（Edge 短命进程也要防涨——unref 不阻退出）
- 白名单独立命名空间（拨测不计费）
