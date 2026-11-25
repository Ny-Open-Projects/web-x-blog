---
title: [NODE-788] 笔试题——实现 BFF 接口防护门（限流 + 幂等 + 校验组合）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-788：手写防护门

**需求与边界**：
- 需求：接口防护组合（SCN-NODE-641/709/695）——① 组合中间件链（限流→校验→幂等——顺序语义）；② 幂等与限流的交互（重放命中幂等表不消耗限流——幂等命中先于限流判断？顺序设计）；③ 校验失败不计限流（校验失败是客户端错误——区分）。顺序：幂等命中 → 限流 → 校验 → handler。
- 边界：① 幂等键提取的容错（无键请求直接过——幂等可选）；② 限流的维度声明（ip/user/api 组合——SCN-NODE-731）；③ 中间件错误的统一出口（SCN-NODE-767 错误码）。

**答**：
```javascript
// 顺序：幂等命中（重放返回原结果，不消耗限流）→ 限流 → 校验 → handler
router.post('/pay',
  idempotent({ ttl: 86_400_000 }),                     // SCN-NODE-735 幂等（重放零成本）
  rateLimit([{ dim: 'user' }, { dim: 'api', value: 'pay' }]),   // SCN-NODE-731 限流
  validate(PaySchema),                                 // SCN-NODE-695 校验
  payHandler);
// 交互语义：幂等命中（DONE）直接返回原结果——不进限流（重放不消耗配额）；
// 幂等 miss（新请求）→ 限流判定 → 校验 → 执行 → 结果入幂等表。
// 校验失败（422）不消耗限流配额（客户端错误先修——限流是防滥用不是防错误）：
rateLimit.wrap(async (req, res, next) => {
  if (validationOnlyFailure(req)) return skipQuota(req);   // 校验失败不计限流
});
```

**评分点**:
- 组合顺序语义（幂等命中先于限流——重放不消耗配额）。
- 校验失败不计限流（错误与滥用区分——限流语义精确）。
- 各中间件复用前文实现（SCN-NODE-735/731/695 编号引用）。
- 统一错误出口（SCN-NODE-767 错误码）。
