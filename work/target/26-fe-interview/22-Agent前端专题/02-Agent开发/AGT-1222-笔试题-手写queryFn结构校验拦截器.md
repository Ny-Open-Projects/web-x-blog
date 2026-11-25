---
title: [1222] 笔试手写：实现响应入缓存前的 schema 拦截
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, TanStack Query]
type: 笔试题
---

## 1222：笔试手写：实现响应入缓存前的 schema 拦截

**答**：实现 guardedFetcher(fetchFn, schemas)：schemas 为 { [keyDomain]: { validate(data) -> { ok, errors } } }。包装 fetchFn：按 key[0] 找 schema（无 schema 直接放行并记录 unvalidated）；校验失败抛 ValidationError（携带 errors 与 key），不写缓存语义由调用方保证。记录 stats { validated, unvalidated, rejected }。

```js
class ValidationError extends Error {
  constructor(key, errors) { super('schema reject: ' + key.join('.')); this.key = key; this.errors = errors; }
}
function guardedFetcher(fetchFn, schemas, stats = { validated: 0, unvalidated: 0, rejected: 0 }) {
  return async (key, ...rest) => {
    const schema = schemas[key[0]];
    const data = await fetchFn(key, ...rest);
    if (!schema) { stats.unvalidated++; return data; }
    const v = schema.validate(data);
    if (!v.ok) { stats.rejected++; throw new ValidationError(key, v.errors); }
    stats.validated++;
    return data;
  };
}
const schemas = {
  user: { validate: d => d && typeof d.id === 'string'
    ? { ok: true } : { ok: false, errors: ['id required'] } },
};
const stats = { validated: 0, unvalidated: 0, rejected: 0 };
const f = guardedFetcher(async key => ({ id: 'u1' }), schemas, stats);
console.log(await f(['user', 1]), stats);   // { id: 'u1' } validated 1
```

**评分点**：
- 无 schema 放行但计入 unvalidated（可观测的治理缺口——不是静默）
- 校验失败抛结构化错误（携带 key 与 errors——缓存投毒在入口拦截）
- stats 三态统计
- 能讨论：schema 与 TS 类型的关系（运行时 vs 编译期——双保险）、拒收后的 UI 降级

