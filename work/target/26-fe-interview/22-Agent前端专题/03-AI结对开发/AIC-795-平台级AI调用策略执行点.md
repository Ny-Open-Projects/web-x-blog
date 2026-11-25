---
title: [AIC-795] 笔试：实现平台级 AI 调用的集中策略执行点（PEP）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-795：笔试：实现平台级 AI 调用的集中策略执行点（PEP）

**需求**：实现 `createPEP(policies)`，返回 `enforce(request)`。`request`: `{ team, capability, sensitivity, tokens }`；`policies`: `Array<{ match: (r)=>boolean, effect: 'allow'|'deny', transform?: (r)=>r, code?: string }>`（按顺序匹配，首个匹配生效）。规则：1) 遍历 policies，第一个 `match(request)` 为 true 的生效；2) effect='deny' 返回 `{ allowed:false, code: p.code ?? 'DENIED' }`；3) effect='allow' 且有 transform 则对 request 变形后继续评估后续策略（累积 transform），无 transform 则立即返回允许；4) 无任何匹配返回默认 `{ allowed:false, code:'DEFAULT_DENY' }`；5) 变形后的请求作为最终结果返回 `{ allowed:true, request: final }`。边界：policies 空（DEFAULT_DENY）；transform 抛异常视为 deny（code 'TRANSFORM_ERROR'）。

**答**：
- 结论先行：集中 PEP 把「鉴权、脱敏、限流」等策略统一在网关执行，业务方无法绕过；策略按顺序匹配、首个生效，规则优先级显式可控。
- transform 链式累积是高级用法（如先脱敏再打标），但要保证顺序确定；异常必须安全兜底为拒绝。
- 追问钩子：为什么策略执行要集中而非各能力自带？——自带会造成策略不一致和遗漏；集中 PEP 是唯一可控的强制点。

```javascript
function createPEP(policies = []) {
  return function enforce(request) {
    let current = { ...request };
    for (const p of policies) {
      if (!p.match(current)) continue;
      if (p.effect === 'deny') return { allowed: false, code: p.code ?? 'DENIED' };
      if (!p.transform) return { allowed: true, request: current };
      try { current = p.transform(current); }
      catch (e) { return { allowed: false, code: 'TRANSFORM_ERROR' }; }
    }
    return { allowed: false, code: 'DEFAULT_DENY' };
  };
}
const pep = createPEP([
  { match: r => r.sensitivity === 'secret', effect: 'deny', code: 'SECRET_BLOCKED' },
  { match: r => r.tokens > 1000, effect: 'deny', code: 'TOKEN_LIMIT' },
  { match: () => true, effect: 'allow', transform: r => ({ ...r, team: r.team.trim() }) },
]);
console.log(pep({ team: ' fe ', capability: 'review', sensitivity: 'low', tokens: 10 }).request.team); // 'fe'
console.log(pep({ team: 'fe', capability: 'x', sensitivity: 'secret', tokens: 10 }).code); // SECRET_BLOCKED
console.log(createPEP([])({}).code); // DEFAULT_DENY
```


**评分点**：
- 顺序匹配、首个生效策略
- deny 返回 code、allow+transform 链式变形
- 异常兜底 TRANSFORM_ERROR、无匹配 DEFAULT_DENY
- 能说明「集中 PEP 不可绕过」属加分
