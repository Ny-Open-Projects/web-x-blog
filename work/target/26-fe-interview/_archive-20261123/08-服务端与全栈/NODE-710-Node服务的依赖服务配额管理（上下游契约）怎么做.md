---
title: [NODE-710] 依赖服务的配额管理（上下游契约）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-710：上下游配额怎么管理？
**答**：
- 配额契约：与下游约定调用配额（QPS 上限——下游容量保护的契约化）+ 超配额语义（429 vs 排队——契约写入 SLA）。
- 配额执行：客户端配额器（本地下游配额限流——超配额不发，SCN-NODE-641 令牌桶 per-下游）+ 服务端强制（下游自己限流——双保险）。
- 配额协调：全局校验（每上游配额 × 上游实例数 ≤ 下游容量——SCN-NODE-699 全局一致性）；配额再分配（大促时上游之间调配——配额是可协商资源）。
- 观测：配额使用率（逼近上限告警——扩容/提配额的前置信号）。
- 追问钩子：为什么下游限流要「客户端自限 + 服务端强制」双层——只有服务端限流：客户端无感知被 429（体验差且重试风暴）；只有客户端自限：客户端计数漂移/绕过（契约无强制力）——双层让「客户端自限做第一道（不发超量），服务端做兜底（拦截漏网）」——契约的可执行性来自双层。

```javascript
// 客户端自限（per-下游令牌桶）
const quota = tokenBucket({ rate: downstreamContract.qps });
async function callDownstream(args) {
  if (!quota.tryTake()) return enqueueOrBackoff(args); // 超配额排队不发
  return rpc.call(args);
}
// 配额使用率告警
telemetry.push({ usedPct: quota.used / quota.cap });   // >80% 告警（提配额前置信号）
```
