---
title: [MFM-443→MFW→MFW-443] 笔试：手写双运行时统一 fetch 包装（Edge/Node 自动降级）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-443：双运行时 fetch
**答**：实现 `unifiedFetch(spec)`：1) 运行时探测（Edge: 无 process/有 caches.default；Node: process.versions.node）——同一调用两端行为正确；2) 能力阶梯：Edge 用 Cache API + HTTP 驱动 DB；Node 用 LRU+连接池——上层同一签名；3) 差异抹平点：超时（Edge AbortSignal 支持/Node 用 timeout 参数——pg query_timeout）、重试（统一策略层与运行时无关）；4) 禁区守卫：Node 专有依赖在 Edge target 构建期报错（依赖审计 MFW-229 前移到 import 图）；5) 快照测试：两端各跑同断言集（行为一致性门禁——双端漂移早发现）。

```javascript
const IS_EDGE = typeof process === 'undefined' || !process.versions?.node

export const store = IS_EDGE
  ? { get: (k) => caches.open('v1').then(c => c.match(k)).then(r => r?.json())),
      set: (k, v, ttl) => caches.open('v1').then(c => c.put(k, jsonRes(v, ttl))) }
  : lruBacked(500, { ttlMs: 30_000 })                       // 同签名不同实现

export const data = {
  async query(q, params) {
    return IS_EDGE
      ? httpDriver.query(q, params, { timeout: 800 })       // HTTP 一命令一请求
      : pool.query(q, params, { queryTimeoutMs: 800 })      // 池化长连接
  },
}
// 构建期：edge target 下 import('pg') → 构建错误（依赖图审计）
// CI：同一套断言在两个 runtime 各跑一遍（矩阵最小单元）
```
**评分点**：
- 运行时探测 + 同签名双实现（业务无感——条件编译收敛在适配层）
- 差异抹平清单具体（超时/重试参数各 runtime 语义不同——逐项对齐）
- 构建期禁区（import 图审计——线上炸不如构建炸）
- 双端同断言 CI（行为漂移的门禁）
