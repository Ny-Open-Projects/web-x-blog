---
title: [NODE-699] 大促容量预案（服务端）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-699：大促容量预案怎么做？
**答**：
- 容量预估链：业务预估（GMV/UV 目标）→ 请求量换算（转化漏斗——每级接口的放大系数）→ 实例数（压测单实例稳态 × 系数——SCN-NODE-647 容量模型）→ 下游配额（DB/Redis/下游服务的全局校验）。
- 弹性预案：HPA 触发指标（QPS/CPU——提前扩容的 warm-up 预热）+ 预扩容（大促前固定扩——HPA 追不上瞬时洪峰）；扩容上限与下游容量对齐（扩了实例下游挂——全局容量一致性）。
- 降级预案（SCN-OPS-329 服务端版）：非核心接口降级清单/熔断阈值调整/只读模式——预案演练准入（未演练不启用，SCN-861）。
- 预案值守：大促值班表（SCN-OPS-210）、应急决策树（SCN-OPS-234）、监控大屏（SCN-NODE-679 值班看板）。
- 追问钩子：为什么「扩容要与下游容量对齐」是预案的第一校验——应用实例 ×5 后连接池 ×5——DB 连接打满（max_connections 爆）——扩容把应用层容量问题转化为 DB 层故障；预案必须做「全局容量一致性校验」：每层的最大并发 ≤ 下游容量——扩容不是单层决策。

```javascript
const capacityPlan = {
  estimate: funnelToQps({ uv, conversion }),           // 漏斗换算
  instances: Math.ceil(qps / steadyPerInstance),
  validate: { dbConn: instances * pool.max < db.maxConn,   // 全局一致性校验
              redisQps: instances * qps < redis.qpsCap },
  hpa: { metric: 'qps', warmup: 'T-1h 预扩容' },
  degrade: rehearsedOnly(degradeMatrix),               // 未演练不启用
};
```
