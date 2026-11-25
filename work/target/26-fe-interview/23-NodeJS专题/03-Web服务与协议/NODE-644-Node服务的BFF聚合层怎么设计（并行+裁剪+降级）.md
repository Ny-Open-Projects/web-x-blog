---
title: [NODE-644] BFF 聚合层怎么设计（并行聚合/字段裁剪/降级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-644：BFF 聚合层怎么设计？
**答**：
- 并行聚合：无依赖的下游请求并行（Promise.all），有依赖的串行（B 的入参来自 A）——聚合耗时 = 关键路径而非全链求和（SCN-NODE-642 deadline 预算分配）。
- 字段裁剪：BFF 按端/页面裁剪下游响应（移动端不要大字段——带宽与序列化省 50%+）；裁剪规则显式声明（schema 级——非手工 pick 散落）。
- 降级设计：每个下游声明降级值（默认值/缓存兜底/可空——SCN-NODE-558 降级链同构）；部分下游失败不阻塞整体（聚合部分成功）。
- BFF 的边界：不做业务逻辑（只做聚合/裁剪/协议适配）——业务逻辑进 BFF 会造成「逻辑双写」（BFF 与微服务各一份）。
- 追问钩子：为什么 BFF 的「部分成功」优于「全有全无」——聚合 5 个下游，1 个非核心失败时全有全无让页面整体挂掉；按下游声明 criticality（核心失败才失败，非核心降级渲染），页面可用性与信息完整度兼顾——「部分成功」要求 BFF 有统一的降级值体系，这是 BFF 设计的核心资产。

```javascript
async function aggregate(userId, { signal }) {
  const [profile, orders, recommend] = await Promise.allSettled([
    getUser(userId, { signal }),
    getOrders(userId, { signal }),
    getRecommend(userId, { signal }).catch(() => FALLBACK_RECOMMEND),   // 非核心降级
  ]);
  return {
    profile: must(profile),                            // 核心：失败即整体失败
    orders: must(orders),
    recommend: orFallback(recommend),                  // 非核心：降级渲染
  };
}
```
