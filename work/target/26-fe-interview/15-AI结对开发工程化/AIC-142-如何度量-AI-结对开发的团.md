---
title: [AIC-142] 如何度量 AI 结对开发的团队级 ROI？把季度数据串起来的「价值链」长什么样？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-142：如何度量 AI 结对开发的团队级 ROI？把季度数据串起来的「价值链」长什么样？
**答**：
- 价值链四环：投入（成本 AIC-119）→ 过程（接受率、任务成功率、轮次）→ 产出（交付周期、吞吐）→ 结果（缺陷率、存活率、线上事故）。每环都有指标，串起来才能归因。
- 关键链路验证：投入增加 → 过程指标改善（成功率高）→ 产出改善（周期缩短）→ 结果不恶化（缺陷率不升）——任何一环断裂都说明「提效」是假的。特别是「产出改善但缺陷率上升」= 用质量换速度，净收益可能是负的。
- 季度报告结构：链路四环各一页 + 结论页（净 ROI、下季动作）；对照基线（引入 AI 前的季度）。
- 陷阱提醒：吞吐量上升可能是 AI 虚增代码行，必须看「结果环」指标兜底；价值链的意义就是防止单指标自欺。
- 追问钩子：这题把 AIC-070（度量）、AIC-050（review 指标）、AIC-119（成本）串成体系，能讲出「断链诊断」是高级答案。

```javascript
// 价值链健康度检查
function chainHealth(q) { // q: 季度数据
  const links = [
    { from: '投入→过程', ok: q.taskSuccessRate > q.prev.taskSuccessRate },
    { from: '过程→产出', ok: q.cycleDays < q.prev.cycleDays },
    { from: '产出→结果', ok: q.defectRate <= q.prev.defectRate * 1.1 }, // 结果不恶化
  ];
  const broken = links.filter(l => !l.ok);
  return { healthy: !broken.length, broken, diagnosis: broken.length ? '净收益存疑，需归因' : 'ROI 成立' };
}
```
