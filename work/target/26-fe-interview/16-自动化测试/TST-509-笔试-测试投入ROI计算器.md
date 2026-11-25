---
title: [TST-509] 笔试：测试投入 ROI 计算器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-509：笔试：测试投入 ROI 计算器

**题目**：实现 calcROI(input)，input = { defectsBefore, defectsAfter, severities: [{level, escapeCost}], manualHoursSaved, hourlyCost, invest, months }。其中 defectsBefore/After 形如 {P0: n, ...}。要求：① 计算逃逸缺陷减少带来的止损（各级别 逃逸数差 × escapeCost）；② 加上人工节省；③ 输出净收益、ROI（净收益/投入）、月度摊销；④ 对异常输入（invest=0、缺 severity 定义）做边界处理。

**答**：
- 结论：ROI = (止损 + 省工 - 投入) / 投入；先归一化缺陷数据，再做差值 × 单价，最后处理边界。
- 实现要点：用 severity 表缺失级别默认 0 成本；invest<=0 时返回无效标记避免除零；months 用于月均摊销。
- 追问钩子：ROI 为负是否说明测试没价值？——不一定，需看是否处于投入期；应结合「逃逸缺陷趋势」与「上线信心」做综合判断，ROI 只是沟通工具之一。

```javascript
function calcROI(input) {
  const { defectsBefore = {}, defectsAfter = {}, severities = [],
    manualHoursSaved = 0, hourlyCost = 0, invest = 0, months = 12 } = input;
  if (!(invest > 0)) return { valid: false, reason: 'invest 必须为正数' };
  const costMap = Object.fromEntries(severities.map(s => [s.level, s.escapeCost]));
  const allLevels = new Set([...Object.keys(defectsBefore), ...Object.keys(defectsAfter)]);
  let saved = 0;
  for (const lv of allLevels) {
    const delta = (defectsBefore[lv] || 0) - (defectsAfter[lv] || 0);
    saved += delta * (costMap[lv] || 0);           // 缺定义默认 0 成本
  }
  const labor = manualHoursSaved * hourlyCost;
  const net = saved + labor - invest;
  return { valid: true, saved, labor, net, roi: +(net / invest).toFixed(2),
    monthly: +(net / months).toFixed(2) };
}
console.log(calcROI({ defectsBefore: { P0: 2 }, defectsAfter: { P0: 0 },
  severities: [{ level: 'P0', escapeCost: 500000 }], invest: 300000 }));
```

**评分点**：
- 按级别差值 × escapeCost 计算止损，缺定义默认 0。
- 净收益 = 止损 + 省工 - 投入，ROI 含除零边界处理。
- 支持月度摊销 months，缺省合理。
- 对 invest<=0 返回无效标记而非抛错/NaN。
