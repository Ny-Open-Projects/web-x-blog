---
title: [AIC-783] 笔试：实现 AI 能力服务的统一 API 门面
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-783：笔试：实现 AI 能力服务的统一 API 门面

**需求**：实现 `createFacade(capabilities)`。`capabilities`: `Record<name, { handler: (input, ctx)=>any, version, schema }>`。返回一个 `invoke(name, input, ctx)` 函数，规则：1) name 不存在抛 `{ code:'NOT_FOUND' }`；2) 按 `schema.required` 校验 input 必填字段，缺失抛 `{ code:'INVALID_INPUT', missing: [...] }`；3) 调用 handler 前注入 `ctx.traceId`（无则生成 'auto-'+随机）；4) 捕获 handler 异常，包装为 `{ code:'HANDLER_ERROR', cause }` 抛出；5) 成功返回 `{ data, version, traceId }`。边界：capabilities 空（任何 invoke 都 NOT_FOUND）；handler 返回 undefined（data 为 null）。

**答**：
- 结论先行：门面统一了「校验、追踪、错误规范、版本返回」四件事，让能力服务对调用方呈现一致体验——这些横切关注点不该每个能力各自实现。
- traceId 要在门面层注入并贯穿，否则后续观测无法串联；错误要规范化（统一 code），便于调用方分类处理。
- 追问钩子：为什么错误要包装而非直接透传？——透传会让调用方依赖各能力的私有错误格式；统一 code 才能写通用的重试/告警逻辑。

```javascript
function createFacade(capabilities = {}) {
  return function invoke(name, input = {}, ctx = {}) {
    const cap = capabilities[name];
    if (!cap) throw { code: 'NOT_FOUND', name };
    const required = cap.schema?.required ?? [];
    const missing = required.filter(k => !(k in input));
    if (missing.length) throw { code: 'INVALID_INPUT', missing };
    const traceId = ctx.traceId ?? ('auto-' + Math.random().toString(36).slice(2, 8));
    try {
      const out = cap.handler(input, { ...ctx, traceId });
      return { data: out ?? null, version: cap.version, traceId };
    } catch (e) {
      throw { code: 'HANDLER_ERROR', cause: e.message ?? String(e) };
    }
  };
}
const facade = createFacade({
  'review': { version: '1.0', schema: { required: ['diff'] }, handler: (i, c) => ({ ok: true, t: c.traceId }) },
});
console.log(facade('review', { diff: [] }, { traceId: 'T1' }).traceId === 'T1');
try { facade('review', {}); } catch (e) { console.log(e.code, e.missing); } // INVALID_INPUT ['diff']
try { facade('nope'); } catch (e) { console.log(e.code); }                 // NOT_FOUND
```


**评分点**：
- 能力不存在 NOT_FOUND、必填校验 INVALID_INPUT
- traceId 门面注入并贯穿返回
- handler 异常包装 HANDLER_ERROR、返回 undefined 转 null
- 边界（空 capabilities）
