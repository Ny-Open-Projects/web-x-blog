---
title: [AIC-952] 笔试：实现「token 成本预估器」（多模型定价 + 预算预警 + 优化建议）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-952：笔试：实现「token 成本预估器」（多模型定价 + 预算预警 + 优化建议）
**答**：
- 核心需求：实现 `estimateCost(plan, models, budget)`。`plan: { model, inTok, outTok, cachedTok? }[]`；`models: { name, inRate, outRate, cacheRate? }[]`（每千 token 单价）。返回 `{ items, total, overBudget, suggestions }`。
- 计算：命中缓存的输入 token 用 cacheRate（缺省为 inRate 的 0.1 倍），其余用 inRate；输出用 outRate；每项 cost = (inTok*inRate + outTok*outRate)/1000。
- 预警：total > budget 则 overBudget=true；suggestions 根据情况给建议（如「某任务可用小模型」「缓存命中率低建议优化前缀」）——用简单规则生成。
- 边界：未知模型按最贵模型计价并给警告；inTok/outTok 缺失按 0；空 plan 返回 total=0。
- 语义：这是「事前预估」——帮助在跑之前判断成本，实际账单以后台计量为准；预估误差要如实说明。
- 追问钩子：能指出「预估要区分输入/输出/缓存三种单价，且建议要可执行（指向具体任务），而非泛泛说『优化 prompt』」的候选人理解可用性的细节。

```typescript
function estimateCost(plan=[], models=[], budget=0) {
  const modelMap = new Map(models.map(m=>[m.name,m]));
  const maxRate = Math.max(...models.map(m=>m.inRate), 0);
  const items = plan.map(p => {
    const m = modelMap.get(p.model);
    if (!m) return { task:p.task, cost:Infinity, warn:'未知模型' };
    const cached = p.cachedTok||0, inNorm=(p.inTok||0)-cached;
    const cost = ((inNorm*m.inRate + cached*(m.cacheRate??m.inRate*0.1) + (p.outTok||0)*m.outRate)/1000);
    return { task:p.task, cost:+cost.toFixed(4) };
  });
  const total = +items.reduce((s,i)=>s+(isFinite(i.cost)?i.cost:0),0).toFixed(4);
  const suggestions = [];
  if (total>budget) suggestions.push('总成本超预算，考虑将低风险任务切到小模型');
  if (items.some(i=>i.warn)) suggestions.push('存在未知模型，按最贵计价('+maxRate+')');
  return { items, total, overBudget:total>budget, suggestions };
}
console.log(estimateCost([{task:'列表',model:'gpt-x',inTok:8000,outTok:1000,cachedTok:5000}],
  [{name:'gpt-x',inRate:3,outRate:15}], 0.02));
```
**评分点**：
- 区分输入/输出/缓存三种单价，cacheRate 缺省为 inRate×0.1。
- cost 计算与缓存抵扣正确，total 累加、空 plan 返回 0。
- 未知模型按最贵计价并警告，overBudget 与 suggestions 生成合理。
- inTok/outTok 缺失按 0 等边界处理，结果可运行。
- 明确「事前预估、实际以后台计量为准」（加分项）。
