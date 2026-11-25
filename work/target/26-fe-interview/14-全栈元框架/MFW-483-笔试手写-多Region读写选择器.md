---
title: [MFW-483] 笔试：手写多 Region 读写分离选择器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-483：多 Region 写主读从选择器
**答**：实现 `pickDb(req, { primary, replicas, lag })`：1) 写操作（POST/PUT/DELETE/Action）一律走 primary（无论其距离）；2) 读走最近副本，但页面有"读己之写"需求（header 带 `x-after-write: <ts>`）且副本滞后 > ts 时强制回落 primary；3) 副本健康不佳（lag 超阈值 5s）摘除；4) 全副本摘除时回落 primary 并打标 `degraded`（读压力转移比拒绝服务好）。

```javascript
const LAG_LIMIT = 5000

export function pickDb(req, { primary, replicas = [], lag = {}, afterWrite }) {
  const method = (req.method || 'GET').toUpperCase()
  const isWrite = !['GET', 'HEAD'].includes(method)
  if (isWrite) return { url: primary, reason: 'write-to-primary', degraded: false }

  const writeTs = afterWrite || Number(req.headers.get('x-after-write') || 0)
  const healthy = replicas.filter(r => (lag[r] ?? 0) < LAG_LIMIT)

  // 读己之写：副本落后于本次写入时间 → 回主库
  if (writeTs && healthy.length) {
    const best = nearest(healthy)
    if ((lag[best] ?? 0) >= writeTs) return { url: primary, reason: 'read-your-write', degraded: false }
    return { url: best, reason: 'replica-fresh-enough', degraded: false }
  }
  if (healthy.length) return { url: nearest(healthy), reason: 'replica', degraded: false }
  return { url: primary, degraded: true, reason: 'all replicas unhealthy' }

  function nearest(list) {
    // 演示：取列表第一个（真实场景接 geo 延迟表）
    return list[0]
  }
}
```

**评分点**：
- 写必走主（多副本下写从库 = 数据丢失，不可协商）
- 读己之写用时间戳比较（x-after-write 头贯穿写→跳转→读链路）
- lag 阈值摘除副本（滞后副本给旧数据比不给更糟的除外——但默认摘）
- 全摘回落主 + degraded 标记（可观测降级优于硬失败）
