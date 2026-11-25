---
title: [NODE-489] Node 服务延迟敏感接口的分层设计（不同 RTT 目标）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-489：延迟敏感接口分层
**答**:
- 分层定义：毫秒级（鉴权/库存预检——内存/Redis 为主，预算 20ms）、百毫秒级（详情/列表——缓存为主 DB 兜底，预算 200ms）、秒级（搜索/复杂聚合/报表——预算 2s，异步化优先）。分层依据是用户体感阈值与业务价值（ARC-546 前端预算的服务端对齐）。
- 每层策略：毫秒级禁止 DB 直查（缓存必命中——miss 走降级默认值）、百毫秒级缓存优先 + 下游并行（预算内 max 并行度）、秒级允许重查询但限制并发（防挤占——独立资源池 NODE-418）。
- 预算传播：请求带层级标记（header x-tier）→ 超时/重试/缓存策略按层配置化（NODE-471/352）；上层给下层分配子预算（deadline 传播）。
- 容量隔离：秒级任务独立实例/线程池（NODE-418），毫秒级永不被秒级查询挤占。
- 度量：分层达标率（各层 P99 vs 预算——分层 SLO，NODE-431 级联）、跨层违规（毫秒级接口出现慢查询 → 立即治理）。
```javascript
// 分层策略配置
const tiers = {
  ms:   { budget: 20,  cacheOnly: true,  dbForbidden: true,  pool: 'main' },
  fast: { budget: 200, parallel: 4,     pool: 'main' },
  slow: { budget: 2000, parallel: 2,    pool: 'batch',        // 独立池隔离
          asyncPreferred: true }
};
// 中间件：ctx.tier = tiers[ctx.get('x-tier')] → 超时/缓存/池按 tier 生效
```
