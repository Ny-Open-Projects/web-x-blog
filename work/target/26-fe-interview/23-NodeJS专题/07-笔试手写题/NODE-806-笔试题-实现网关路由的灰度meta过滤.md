---
title: [NODE-806] 笔试题——实现网关路由 meta 过滤（版本/地域/权重）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-806：手写 meta 过滤

**需求与边界**：
- 需求：服务发现 meta 过滤路由（SCN-NODE-776/703）——① 多维 meta 过滤（version/region/weight/degradation）；② 过滤后为空的处理（兜底链——全部 canary 不健康回 stable，SCN-NODE-776）；③ 权重路由（加权随机——SCN-NODE-769 平滑轮询）；④ 过滤规则的声明式（DSL 配置——路由规则版本化）。
- 边界：① 过滤链的短路（维度逐级收敛——先版本后地域后健康）；② 兜底链的可解释（为什么路由到 stable——日志声明）；③ 规则变更热更（SCN-NODE-663）。

**答**：
```javascript
// 路由规则 DSL（声明式）
const RULES = [
  { when: { gray: 'canary' }, filter: { version: 'canary' }, fallback: { version: 'stable' } },
  { when: { region: 'eu' }, filter: { region: 'eu' }, fallback: { region: 'any' } },
];
function routeMeta(instances, req) {
  const matched = RULES.filter(r => matchWhen(r.when, req));   // 条件匹配
  for (const rule of matched) {                        // 逐规则短路（SCN-OPS-638 链式）
    const pool = instances.filter(i => matchFilter(i.meta, rule.filter) && i.healthy);
    if (pool.length) { logWhy(rule, pool); return weightedPick(pool); }   // 兜底链可解释（SCN-NODE-776）
    logFallback(rule, rule.fallback);
  }
  return weightedPick(instances.filter(i => i.healthy));   // 最终兜底（全摘防御）
}
```

**评分点**:
- DSL 声明式路由规则（版本化热更——SCN-NODE-663）。
- 逐规则短路 + 兜底链可解释（logWhy——SCN-NODE-776）。
- 多维 meta 过滤（版本/地域/健康）。
- 加权随机（SCN-NODE-769 平滑轮询复用）。
