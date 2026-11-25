---
title: [MFW-845] 怎么把 ISR 的陈旧内容服务窗口和业务 SLA 对齐
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-845：怎么把 ISR 的陈旧内容服务窗口和业务 SLA 对齐

**答**：
- 结论：用业务容忍的「最大陈旧时间」反推各层 max-age / SWR / revalidate 周期，形成路由分级策略表，不搞一刀切。
- 落地：路由打标强一致/弱一致/最终一致 → 映射缓存头与失效周期；响应带数据版本时间戳，拨测比对实际陈旧度，超 SLA 告警。
- 追问钩子：怎么度量「实际陈旧度」？——响应头带数据版本时间，客户端/拨测用当前时间减去它。

```javascript
const SLA = {
  strong: { maxAge: 0, swr: 0 },        // 价格/库存：实时
  weak:   { maxAge: 10, swr: 60 },      // 列表：秒级
  eventual: { maxAge: 300, swr: 3600 }  // 内容：分钟级
};
function headersFor(tier) {
  const { maxAge, swr } = SLA[tier];
  return { 'Cache-Control': `public, s-maxage=${maxAge}, stale-while-revalidate=${swr}` };
}
// 响应携带数据版本时间，用于度量实际陈旧度
function withVersion(headers, dataUpdatedAt) {
  return { ...headers, 'x-data-version': dataUpdatedAt };
}
console.log(headersFor('weak'));
// 拨测：staleness = now - x-data-version，超过 SLA 上限告警
```
