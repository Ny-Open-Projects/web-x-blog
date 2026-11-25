---
title: [WCN-515] 企业落地度量：如何用「采用率 × 代码删除量 × bug 下降率」讲清 WCN 的 ROI？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-515：企业落地度量：如何用「采用率 × 代码删除量 × bug 下降率」讲清 WCN 的 ROI？

**答**：
- 结论：ROI 不是「组件好看」，而是三条曲线：复用规模上升、重复代码下降、同类缺陷收敛。
- 采用率：统计引用元素库的宿主仓库数与组件实例数，证明规模化。
- 代码删除量：迁移前后相似组件代码行数差值，折算人力节省（行数 × 单列成本模型）。
- 追问：bug 下降率如何归因到元素库而非业务变化？（答：按「组件类缺陷」分类，对比迁移前后同类问题数）

```javascript
function roi({ adoption, linesRemoved, defectBefore, defectAfter, costPerLine }) {
  const savedHumanCost = linesRemoved * costPerLine;
  const defectDrop = defectBefore ? (defectBefore - defectAfter) / defectBefore : 0;
  return {
    scale: adoption.repos + ' repos / ' + adoption.instances + ' instances',
    savedHumanCost, defectDrop: (defectDrop * 100).toFixed(1) + '%',
    verdict: adoption.instances > 1000 && defectDrop > 0.3 ? '正向' : '需观察',
  };
}
```
