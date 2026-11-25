---
title: [AIC-925] 大促前多个 Agent 并行改「价格与优惠规则」，如何避免彼此覆盖导致规则互相打架？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-925：大促前多个 Agent 并行改「价格与优惠规则」，如何避免彼此覆盖导致规则互相打架？
**答**：
- 价格规则是典型的「共享可变状态」——结论：不要让多 Agent 直接改同一份规则配置，应由「单一规则源 + 分层覆盖」来管理。
- 用「分层优先级」模型：基础价 ← 品类折扣 ← 活动价 ← 优惠券，每层独立配置、有明确优先级，Agent 各改一层而非改最终价，就不会互相覆盖。
- 每次改动产出「规则差异快照」，合并时用决策表跑全量组合测试（如 100 组商品 × 规则组合），任何异常叠加立即阻断。
- 追问钩子：能提出「把规则编译成纯函数管线，每层是可独立验证的 transform，最终价是管线输出」的候选人，用函数式思路消除了覆盖问题。

```typescript
// 分层规则管线：每层独立，避免互相覆盖
const layers = [
  { name:'base',    apply:(p)=>p.price },
  { name:'category',apply:(p)=> p.cat==='digital' ? p.price*0.95 : p.price },
  { name:'promo',   apply:(v)=> v>=300 ? v-50 : v },
  { name:'coupon',  apply:(v,c)=> c==='VIP' ? v*0.9 : v },
];
function finalPrice(product, coupon) {
  let v = product.price;
  for (const layer of layers.slice(1)) v = layer.apply(v, coupon);
  return Math.max(0, +v.toFixed(2));
}
// 每个 Agent 只负责一层，产出可用决策表独立验证，不会覆盖他人
console.log(finalPrice({price:400,cat:'digital'}, 'VIP'));
```
