---
title: [NODE-632] Node 服务架构综合收束：一段话给出你的服务端方法论
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-632：Node 服务架构综合收束
**答**:
- 一句话方法论：以"可靠"为底座（幂等/对账/降级/优雅关闭——NODE-381/382/390/351），以"可观测"为眼睛（三支柱 + SLO + 告警治理——NODE-371~374/431/404），以"可演进"为骨架（分层边界/契约单源/适应度函数——NODE-612/528/396），以"业务语义"为度量（分层预算/业务级 SLO/成本分账——NODE-489/431/434）。
- 架构决策的优先序：先单库事务后 saga（NODE-380）、先缓存后扩容（NODE-353/433）、先声明后实现（依赖声明/降级声明/适应度函数——声明制让治理自动化）、先灰度后全量（NODE-370/446）。
- 常见坑防御：热点 key（NODE-384）、缓存击穿（NODE-378）、重试风暴（NODE-471）、任务悬挂（NODE-581/630）、配置漂移（NODE-606/535）——防御清单化。
- 前端协同视角：deadline 传播/标签透传/上下文贯穿/灰度同桶——前后端一致才是真正的全栈一致性（NODE-497/523/620/598）。
- 面试收束答法：先讲分层与边界 → 再讲可靠性设计（幂等/对账/降级）→ 可观测与 SLO → 灰度与演进 → 成本与容量——从"能跑"到"可运营"的完整叙事。
```javascript
// 方法论速查（面试白板）
const methodology = {
  reliability: ['idempotency', 'reconcile', 'degrade-matrix', 'graceful-shutdown'],
  observability: ['metrics/trace/logs', 'SLO+burn-rate', 'alert-hygiene'],
  evolvability: ['layered-boundary', 'contract-first', 'fitness-functions'],
  ops: ['canary+auto-rollback', 'capacity-headroom', 'finops']
};
```
