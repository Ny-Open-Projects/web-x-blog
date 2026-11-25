---
title: [WCN-994] 从框架组件迁 WC 的技术债怎么还：兼容性债务管理
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-994：从框架组件迁 WC 的技术债怎么还：兼容性债务管理

**答**：
- 结论先行：迁移技术债主要是「双轨并存期的兼容成本」——新旧组件共存时，API 语义差异、样式 dual、事件适配都要维护，债务管理核心是「限定双轨期 + 明确偿还计划」。
- 识别：列出迁移清单，标记每个组件的债务类型（API 不一致、样式重复、适配层 hack、文档缺失）与偿还优先级。
- 控制：双轨期设上限（如一个季度），新功能禁止在旧组件上加；用适配层把差异收敛到一处，避免散落 hack。
- 偿还：按「使用量 × 债务成本」排序，先还高频高成本组件；每还一个就删对应适配代码并更新监控。
- 追问钩子：面试官问「旧组件有业务方死活不迁怎么办」——答：用治理手段（新场景禁用、a11y/体积门禁只对 WC 放宽）引导，而非无限期维护双轨。

```javascript
// 迁移债务清单与偿还排序
const debts = [
  { comp:'ds-button', usage:9000, cost:8, type:'API不一致' },
  { comp:'ds-old-table', usage:200, cost:20, type:'样式重复' },
  { comp:'ds-modal', usage:3000, cost:12, type:'适配层hack' },
  { comp:'ds-toast', usage:1500, cost:5, type:'文档缺失' },
];
// 按 使用量×成本 排序，先还高频高成本
debts.sort((a,b)=> b.usage*b.cost - a.usage*a.cost);
console.log(debts.map(d=>d.comp)); // ds-button 优先
// 制定一个季度内的偿还计划
const plan = debts.map(d=> ({ comp:d.comp, due:'一个季度内', action:'删适配层+切WC' }));
plan.forEach(p => console.log(p.comp, p.action));
// 双轨期红线：新功能禁止加在旧组件上
function canAddLegacy(comp) {
  return !debts.some(d => d.comp === comp); // 在债务清单里的旧组件禁止新增
}
console.log('ds-button 可加新功能:', canAddLegacy('ds-button')); // false
console.log('新组件可加:', canAddLegacy('ds-new')); // true
```
