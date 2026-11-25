---
title: [SOFT-535] 手写 calcROI：成本/收益分项、区间估计、回收期、出处标注校验？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-535：手写 calcROI：成本/收益分项、区间估计、回收期、出处标注校验

**需求与边界**：
- 实现 calcROI(input)。
- 边界要求：① 成本与收益分项每项必须带 source 字段（缺出处标 error 不计入汇总）；② 收益支持区间（min/max），输出保守（min）与乐观（max）两套 ROI；③ 回收期 = 总成本 ÷ 月净收益（保守口径），除零/负收益返回 Infinity 或标注；④ 输出可读文本摘要。

**答**：
```javascript
function calcROI({ costs, gains }) {
  const errs = [], ok = [];
  for (const x of [...costs, ...gains]) {
    if (!x.source) errs.push(x.name);
    else ok.push(x);
  }
  const sumOf = (arr, f) => arr.filter(x => x.source)
    .reduce((a, x) => a + f(x), 0);
  const cost = sumOf(costs, x => x.value);
  const gainMin = sumOf(gains, x => x.min ?? x.value);
  const gainMax = sumOf(gains, x => x.max ?? x.value);
  const monthly = (g) => (g - cost) / 12;
  const payback = (g) => monthly(g) > 0
    ? +(cost / monthly(g)).toFixed(1) : Infinity;
  return { errors: errs, cost,
    roi: { conservative: gainMin / cost, optimistic: gainMax / cost },
    paybackMonths: { conservative: payback(gainMin),
      optimistic: payback(gainMax) },
    summary: payback(gainMin) === Infinity
      ? '保守口径下不回收：需说明战略/风控理由'
      : `保守回收期 ${payback(gainMin)} 个月`,
    missingSource: errs };                        // 出处缺失清单
}
```

**评分点**:
- 出处强制（无 source 不进汇总，防拍脑袋数字）。
- 区间双口径（保守/乐观）+ 回收期除零与负收益处理。
- 不回收时输出诚实话术（而非硬凑正数）。

