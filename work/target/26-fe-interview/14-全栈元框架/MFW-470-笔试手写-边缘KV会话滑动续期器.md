---
title: [MFW-470] 笔试：手写边缘 KV 会话滑动续期器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-470：边缘 KV 会话滑动过期续期器
**答**：实现 `createEdgeSession(kv)`：1) `get(sid)`：KV 读 `{ userId, exp }`，过期删除返回 null；未过期且剩余寿命 < 1/2 时异步 `refresh`（滑动续期写回 exp = now + ttl，不阻塞本次请求——边缘写延迟高）；2) 同 sid 并发 refresh 去重（本实例内单飞；跨实例靠 KV 最后写胜出即可，不需要分布式锁——容忍双写幂等）；3) `destroy(sid)` 立即失效（登出）：删除 + 负缓存 60s（防已删会话被旧副本复活——KV 最终一致）；4) 全程不阻塞主流程超过 5ms（get 必须 await 一次读完成）。

```javascript
export function createEdgeSession(kv, { ttl = 3600_000 } = {}) {
  const refreshing = new Set()
  const tombstone = new Map() // sid -> until (负缓存)

  async function get(sid) {
    if ((tombstone.get(sid) || 0) > Date.now()) return null
    const raw = await kv.get(sid)
    if (!raw) return null
    const sess = JSON.parse(raw)
    if (sess.exp <= Date.now()) { kv.delete(sid); return null }
    if (sess.exp - Date.now() < ttl / 2 && !refreshing.has(sid)) {
      refreshing.add(sid)
      kv.put(sid, JSON.stringify({ ...sess, exp: Date.now() + ttl }))
        .catch(() => {}).finally(() => refreshing.delete(sid)) // 异步不 await
    }
    return sess
  }

  async function destroy(sid) {
    await kv.delete(sid)
    tombstone.set(sid, Date.now() + 60_000) // 拦最终一致的旧副本
  }

  return { get, destroy }
}
```

**评分点**：
- 剩余 < 1/2 触发续期（折衷避免每请求都写 KV）
- refresh 异步不阻塞 + 单飞去重（边缘写延迟与配额敏感）
- destroy 负缓存（KV 最终一致下登出可被旧副本复活——真考点）
- 过期即删（懒清理，不依赖定时任务）
