---
title: [MFW-479] 笔试：手写 SSE 刷新与 revalidate 协调器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-479：SSE 推送与 RSC 增量刷新协调器
**需求**：实现 `createRefreshHub()`：1) `subscribe(routeId, res)`：SSE 订阅，同一客户端同 routeId 去重（重复订阅只留一份）；2) `broadcast(routeId, { tag, version })`：写 `event: refresh` 帧，带节流：同 routeId 1s 内多次 broadcast 合并成一次（高频写场景保护客户端）；3) `onClientEvent` 收到客户端 ack 后才计投递完成，3s 无 ack 判死连接并清理（半开连接清理）；4) `count(routeId)` 查看活跃订阅数（服务端决定是否降级为轮询）。

```javascript
export function createRefreshHub() {
  const subs = new Map()   // routeId -> Map(clientId -> { res, lastAck })
  const timers = new Map()

  function subscribe(routeId, clientId, res) {
    if (!subs.has(routeId)) subs.set(routeId, new Map())
    subs.get(routeId).set(clientId, { res, lastAck: Date.now() })
  }

  function broadcast(routeId, payload) {
    if (timers.has(routeId)) return          // 节流中，合并
    timers.set(routeId, setTimeout(() => {
      timers.delete(routeId)
      const m = subs.get(routeId); if (!m) return
      for (const [cid, { res }] of m) {
        res.write(`event: refresh\ndata: ${JSON.stringify({ ...payload, cid })}\n\n`)
      }
    }, 1000))
  }

  function ack(routeId, clientId) {
    const e = subs.get(routeId)?.get(clientId)
    if (e) e.lastAck = Date.now()
  }

  setInterval(() => { // 半开清理：3s 无 ack 踢出
    for (const [rid, m] of subs)
      for (const [cid, e] of m)
        if (Date.now() - e.lastAck > 3000) { e.res.end(); m.delete(cid) }
  }, 3000).unref?.()

  return { subscribe, broadcast, ack, count: rid => subs.get(rid)?.size ?? 0 }
}
```

**评分点**：
- 同 route 1s 节流合并（高频写不放大到 N 客户端 × M 次）
- ack 判活 + 3s 清理（SSE 半开连接堆积是内存泄漏主因）
- 订阅去重（同客户端重复 EventSource 不叠加）
- count 暴露用于降级决策（订阅过多退回轮询）
