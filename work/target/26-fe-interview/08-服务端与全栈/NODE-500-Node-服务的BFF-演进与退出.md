---
title: [NODE-500] Node 服务的 BFF 层演进与退出（何时该拆/合/撤）如何决策？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-500：BFF 层演进与退出决策
**答**:
- 演进决策维度：规模（接口数/团队数——BFF 是编排层不是业务层，业务逻辑渗入 → 拆出领域服务）、重复（多 BFF 重复装配逻辑 → 收敛公共装配库/下沉数据服务）、性能（BFF 成为瓶颈 → 缓存下沉/并行化/评估去层）。
- 退出场景：单一前端 + 简单后端 → BFF 是多余一层（直连更简单）；后端演进为前端友好的聚合服务 → BFF 退出（ARC-144 引入与退出策略呼应）。
- 拆分决策：BFF 按端拆（web-bff/app-bff）还是按域拆（trade-bff/user-bff）——按"变更节奏与团队边界"（同团队同节奏的端合一个 BFF；跨团队域分——康威定律）。
- 演进路径管理：每次结构调整走 ADR（ARC-184：为什么拆/为什么合/代价）——BFF 结构频繁翻烧饼是治理失败信号。
- 健康指标：BFF 层厚度（业务逻辑占比——超过 20% 警惕变 FatBFF）、接口重复率、聚合延迟达标率。
```javascript
// BFF 健康度体检
function bffHealth(bff) {
  return {
    logicRatio: businessLogicLines(bff) / totalLines(bff),       // > 0.2 → 业务下沉评估
    dupRate: duplicatedAssembly(bff),                            // 重复装配 → 收敛
    p95: aggLatencyP95(bff),                                     // 聚合延迟
    verdict: logicRatio > 0.2 ? '拆领域服务' : dupRate > 0.3 ? '收敛公共库' : 'ok'
  };
}
```
