---
title: [NODE-960] 笔试题——实现发布决策自动执行器（决策→动作→验证）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-960：手写决策执行

**需求与边界**：
- 需求：决策自动执行（SCN-OPS-960/242）——① 决策→动作映射（放行/熔断/回滚——SCN-OPS-242）；② 执行的权限（SCN-OPS-253）；③ 执行的验证（SCN-联想-865）；④ 执行的审计（SCN-OPS-273）。
- 边界：① 自动执行的边界（≤25% 自动——SCN-OPS-242）；② 执行的幂等（SCN-NODE-655）；③ 执行失败的处理（SCN-OPS-227）。

**答**：
```javascript
const ACTIONS = { ramp: setGray, break: circuitBreak, rollback: multidimRollback };
async function executeDecision(decision) {
  requireRole(decision.by, decision.requires ?? 'release-owner');   // 权限（SCN-OPS-253）
  const idem = await withIdempotency(`dec:${decision.id}`, async () => {   // 幂等（SCN-NODE-655）
    const r = await ACTIONS[decision.action](decision.context);
    const verified = await verify(decision.verify ?? 'metric-stable');   // 验证（SCN-联想-865）
    return { r, verified };
  });
  audit({ decision, result: idem });                   // 审计（SCN-OPS-273）
  return idem;
}
```

**评分点**:
- 决策→动作映射（SCN-OPS-242）。
- 权限 + 幂等（SCN-OPS-253/655）。
- 执行验证（SCN-联想-865）。
- 审计（SCN-OPS-273）。
