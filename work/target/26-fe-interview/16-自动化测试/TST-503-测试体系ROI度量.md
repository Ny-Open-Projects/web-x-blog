---
title: [TST-503] 如何向管理层度量测试体系的 ROI
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-503：如何向管理层度量测试体系的 ROI

**答**：
- 结论：不要只报「用例数/覆盖率」这类活动指标，要报「缺陷逃逸率下降、回归周期缩短、发布信心提升」这类结果指标，并折算成钱。
- ROI 公式：(逃逸缺陷减少带来的止损 + 人工回归节省的工时成本) / 测试建设投入。关键是给逃逸缺陷定级标价（P0/P1 的线上损失），让收益可量化。
- 追问钩子：测试投入短期看不到收益怎么办？——用「缺陷发现成本曲线」说明：越晚发现成本指数上升，并展示拦截的一个 P0 案例即可建立信任。

```javascript
// ROI 估算：逃逸缺陷止损 + 人工节省 - 建设投入
const DEFECT_COST = { P0: 500000, P1: 80000, P2: 10000 };
function roi({ escapedBefore, escapedAfter, manualHours, hourly, invest }) {
  const savedLoss = Object.keys(DEFECT_COST).reduce((sum, sev) =>
    sum + (escapedBefore[sev] - escapedAfter[sev]) * DEFECT_COST[sev], 0);
  const savedLabor = manualHours * hourly;
  const gain = savedLoss + savedLabor - invest;
  return { savedLoss, savedLabor, roi: +(gain / invest).toFixed(2) };
}
console.log(roi({
  escapedBefore: { P0: 2, P1: 5, P2: 20 },
  escapedAfter:  { P0: 0, P1: 2, P2: 15 },
  manualHours: 200, hourly: 100, invest: 300000,
}));
```
