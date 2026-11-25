---
title: [TST-803] 笔试：手写一个「测试投资回报率(ROI)」计算模型，量化测试投入的价值
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-803：笔试：手写一个「测试投资回报率(ROI)」计算模型，量化测试投入的价值
**答**：
- 需求：实现 calcTestROI(input) —— 输入测试成本、各等级缺陷逃逸数量与修复成本、测试拦截缺陷数量，输出 ROI 与结论。
- 公式：ROI = (测试拦截节省的成本 - 测试投入成本) / 测试投入成本；节省成本 = Σ(逃逸缺陷数 × 该缺陷线上修复成本)。
- 边界：成本为 0 时避免除零返回 null；负数输入抛错；结果保留两位小数；ROI>0 才值得投入。

```javascript
function calcTestROI({ testCost, intercepted, escapedByLevel }) {
  const FIX_COST = { P0: 50000, P1: 10000, P2: 2000, P3: 500 };
  if (testCost < 0 || intercepted < 0) throw new RangeError('成本不可为负');
  if (testCost === 0) return null; // 避免除零
  // 逃逸缺陷的「本可避免」成本
  const avoided = Object.entries(escapedByLevel).reduce((sum, [lv, n]) => {
    if (!(lv in FIX_COST)) throw new Error(`未知缺陷等级 ${lv}`);
    if (n < 0) throw new RangeError('缺陷数不可为负');
    return sum + n * FIX_COST[lv];
  }, 0);
  const saved = avoided + intercepted * FIX_COST.P2;
  const roi = Number(((saved - testCost) / testCost).toFixed(2));
  return { saved, roi, worthwhile: roi > 0,
    verdict: roi > 0 ? '值得投入' : '投入产出失衡，需优化' };
}
console.log(calcTestROI({
  testCost: 200000, intercepted: 80,
  escapedByLevel: { P0: 1, P1: 3, P2: 10 }
})); // P0/P1 逃逸拉高 avoided，roi 通常 > 0

// 对照：只拦普通缺陷、无高危逃逸时 ROI 可能为负
console.log(calcTestROI({ testCost: 200000, intercepted: 60,
  escapedByLevel: { P3: 5 } })); // 需引入更多 P0 拦截才能回本
```
**评分点**：
- 正确实现 ROI 公式并区分「拦截节省」与「逃逸本可避免」两部分成本。
- 边界处理：除零返回 null、负数输入抛错、未知缺陷等级报错。
- 能指出「线上缺陷修复成本远高于测试阶段」这一数量级差异是核心加分项。
- 结果保留两位小数并给出可执行的 worthwhile/verdict 结论。
