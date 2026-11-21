---
title: [MFW-266] 动态 IO 的缓存穿透与击穿防护（元框架版）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-266：缓存穿透与击穿防护

**答**:
- 穿透（查不存在 id 大量打到 DB）：路由层参数校验（uuid 格式先拒——Redis布隆可选）+ notFound 快速返回（占位缓存空值 30s——负缓存）
- 击穿（热 key 过期瞬间并发重建）：单飞（同渲染器进程内 Promise 共享）+ 分布式锁（Redis SET NX——跨实例单飞）+ 逻辑过期（旧值立即回、异步刷新——无空窗）
- 雪崩（同批 key 同时到期）：TTL 加随机抖动（±10%）+ 分批预刷新（临近过期的热 key 主动续）
- 元框架落位：这些语义不该散在组件里——封装进团队 cache 薄层（MFW-242 统一面），业务只见 get(key, { dedupe: true })

```javascript
// 单飞 + 逻辑过期（薄层内实现）
async function getWithGuard(key, fetcher, { ttl = 60_000 } = {}) {
  const cur = await store.get(key)
  if (cur && !isExpiredLogicaly(cur)) return cur.data          // 逻辑过期先回旧值
  const inflightKey = `lock:${key}`
  if (await redis.set(inflightKey, 1, 'NX', 'PX', 3000)) {     // 跨实例单飞
    try { const d = await fetcher(); await store.set(key, { data: d, exp: Date.now()+ttl }, 'PX', ttl*2); return d }
    finally { redis.del(inflightKey) }
  }
  return cur?.data ?? (await waitForRefill(key))               // 无旧值等待或占位
}
```
