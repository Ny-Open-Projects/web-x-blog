---
title: [WCN-807] 从 React 迁到 WC，业务团队抵触怎么办？（变更管理）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-807：从 React 迁到 WC，业务团队抵触怎么办？（变更管理）

**答**：
- 结论先行：抵触本质上不是技术问题，而是「收益归平台、成本归业务」——变更管理的核心是重新分配收益与降低成本，而不是讲 WC 多先进。
- 先诊断抵触来源：常见四类——怕背锅（迁移出事故谁负责）、怕工作量（没给排期）、习惯惯性（React 用得顺手）、看不到收益（觉得跟自己无关）。
- 对症下药：给迁移排期与人力（成本归平台承担一部分）、设迁移专项 SLA 与兜底（降低风险）、提供 React 包装器让业务「几乎无感」过渡、用同行的量化收益案例建立动机。
- 分层推进：不要一刀切强制，先新页面/新模块用 WC，存量页面随自然迭代逐步替换，设「不迁移也不惩罚、迁移有激励」的软性机制。
- 追问钩子：面试官会问「如果 VP 强推但团队阳奉阴违怎么办」——答：把迁移指标纳入团队 OKR 但配足资源，同时建立反馈通道让业务方影响平台路线，让他们从「被动接受者」变「共建者」。

```javascript
// 抵触诊断 → 对策映射：先分类再开药方
const PLAYBOOK = {
  fearBlame:  '平台兜底 + 迁移专项 SLA，事故平台共担',
  noCapacity: '纳入排期 + 平台提供 codemod/脚手架降工作量',
  inertia:    '提供 React 包装器，零改造先用起来',
  noBenefit:  '用同 BU 的收益案例 + 计入团队 OKR',
};
function diagnose(signals) {
  const causes = [];
  if (signals.asksWhoToBlame) causes.push('fearBlame');
  if (signals.noSchedule) causes.push('noCapacity');
  if (signals.prefersReact) causes.push('inertia');
  if (signals.seesNoValue) causes.push('noBenefit');
  return causes.map(c => `${c}: ${PLAYBOOK[c]}`);
}
console.log(diagnose({ asksWhoToBlame: true, noSchedule: true, seesNoValue: true }));
```
