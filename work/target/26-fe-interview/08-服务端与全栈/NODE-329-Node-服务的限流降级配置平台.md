---
title: [NODE-329] Node 服务的限流降级配置平台？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-329：Node 服务的限流降级配置平台？
**答**:
- 平台化：限流/降级规则进配置平台（NODE-150/323），规则结构化（route/维度/阈值/动作）——值班一键执行（ARC-270 SOP）。
- 规则模型：限流（key=uid|ip|global、窗口、阈值）、降级（route→占位响应/缓存模式）、熔断（错误率阈值→半开恢复）。
- 执行引擎：中间件统一消费规则（热更即时生效）；规则变更全审计。
- 演练：大促前按预案批量下发降级规则并验证（NODE-249）。

```typescript
// 规则模型与执行
interface Rule { route: string; type: 'rate-limit' | 'degrade' | 'breaker';
  key?: 'uid' | 'ip'; windowMs?: number; limit?: number; placeholder?: unknown; }
async function ruleMiddleware(ctx, next) {
  const rules = config.get('rules').filter(r => matchRoute(ctx, r.route));
  const rl = rules.find(r => r.type === 'rate-limit');
  if (rl && !(await rateLimit(keyOf(rl, ctx), rl))) return ctx.throw(429);
  const dg = rules.find(r => r.type === 'degrade');
  if (dg) { ctx.body = dg.placeholder; metrics.inc('degrade', { route: dg.route }); return; }   // 直接降级
  await next();
}
// 值班动作：platform.degrade('/recommend', placeholder) → 配置中心下发 → 全实例热生效
```
