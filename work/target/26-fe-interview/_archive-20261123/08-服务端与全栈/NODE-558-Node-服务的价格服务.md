---
title: [NODE-558] Node 服务的价格服务（定价/活动价/到手价）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-558：价格服务
**答**:
- 价格层次：基准价（商品定价）→ 活动价（促销规则计算）→ 到手价（叠加券/会员——分层计算，每层规则版本化）。
- 计算引擎：促销规则引擎（满减/折扣/打包价——规则 DSL + 优先级/互斥/叠加规则 ARC-452 服务端版）、计算顺序确定性（同输入同输出——规则排序显式，防"改规则顺序价格变"）、计算可解释（每层输出明细——breakdown 树 ARC-644）。
- 一致性：展示价与结算价一致（同一服务同一版本计算——列表/详情/结算走同一价格服务接口；缓存键含规则版本——规则变更失效缓存 NODE-507）、价格快照（订单成交价快照——后续价格变动不影响已成交订单，退款按快照）。
- 性能：价格计算批量接口（列表页批量到手价——缓存热点商品价格 NODE-526）、规则变更时缓存失效风暴防护（批量失效合并 NODE-507）。
- 风控：价格配置审计（改价操作留痕——误改价应急回滚 NODE-442/470）、异常价格告警（低于成本价拦截——防羊毛定价事故）。
```javascript
// 分层价格计算
function priceOf(sku, ctx) {
  const base = catalog.price(sku);
  const promo = promoEngine.apply(base, ctx.promos);             // 规则引擎（版本化）
  const final = couponLayer.apply(promo, ctx.coupons);
  return { base, promo, final, breakdown: [...] };               // 可解释明细
}
// 订单落单：savePriceSnapshot(orderId, calc) —— 成交价快照
```
