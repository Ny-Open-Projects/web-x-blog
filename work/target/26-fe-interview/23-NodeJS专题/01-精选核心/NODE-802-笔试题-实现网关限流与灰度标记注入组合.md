---
title: [NODE-802] 笔试题——实现网关层组合中间件（限流+灰度+trace）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-802：手写网关组合

**需求与边界**：
- 需求：网关横切组合（SCN-NODE-701）——① 顺序语义（trace 注入 → 灰度重写 → 限流 → 转发——每层职责单一）；② trace 先注入（限流日志带 traceId——SCN-NODE-645）；③ 灰度重写在限流前（限流按桶维度——SCN-OPS-216）；④ 网关不做业务（SCN-NODE-701 边界断言——注册表校验无业务字段）。
- 边界：① 各层失败透传（trace 失败不阻断——非关键层容错）；② 限流的维度从灰度桶取（桶维度限流——SCN-OPS-216 联动）；③ 组合顺序可配置（per 路由覆盖）。

**答**：
```javascript
const gatewayPipeline = [
  tracing(),                                           // 1. trace 注入（限流日志带 traceId）
  grayMark(),                                          // 2. 灰度重写（SCN-OPS-216 权威）
  rateLimit({ dims: ['gray', 'ip'] }),                 // 3. 限流（桶维度——SCN-NODE-731）
  forward(),
];
app.use(compose(gatewayPipeline));                     // 顺序语义（compose）
// 容错：非关键层失败不阻断
function compose(mws) {
  return mws.reduceRight((next, mw) => (req, res) => {
    try { return mw(req, res, next); }
    catch (e) { if (mw.critical) throw e; logger.warn(e); next(); }   // 非关键容错
  }, (req, res) => forward(req, res));
}
// 网关边界断言（SCN-NODE-701）
test('网关不含业务逻辑', () => {
  for (const mw of gatewayPipeline)
    assert(!mw.businessFields?.length, '网关不得引用业务字段');
});
```

**评分点**:
- 顺序语义（trace→灰度→限流——依赖关系明确）。
- 非关键层容错（trace 失败不阻断——可用性分层）。
- 网关边界断言（不含业务——SCN-NODE-701 纪律 CI 化）。
- 限流按灰度桶维度（SCN-OPS-216 联动）。

## 变体与延伸（补充）

**变体与延伸**：

1. 限流放在灰度重写之后，桶维度变了会不会让同一用户配额翻倍 → 会，桶 key 要用重写后的稳定业务标识而不是原始 host，灰度切换期给桶加过渡期合并计数。
2. trace 层失败不阻断，但限流日志要 traceId，缺失时怎么办 → trace 层失败仍生成兜底 traceId，保证下游日志能关联，只是无法串联上游，并在日志里标记 fallback。
3. 各层顺序可配置，配错顺序引发的事故怎么防 → 顺序白名单校验加启动时打印实际链路，灰度环境用流量回放比对两种顺序的限流结果差异后再放行。
