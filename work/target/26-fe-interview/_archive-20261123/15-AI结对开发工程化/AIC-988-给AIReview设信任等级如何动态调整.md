---
title: [AIC-988] 想给 AI Review 设一个「信任等级」决定它能自动阻断到什么程度，这个等级如何动态调整？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-988：想给 AI Review 设一个「信任等级」决定它能自动阻断到什么程度，这个等级如何动态调整？
**答**：
- 信任等级应「靠数据挣得」：基于该规则/模型的历史精确率、误报治理效果、人工复核一致率来计算，而非拍脑袋设定——结论：信任是可量化的统计量。
- 动态调整机制：定期用最近 N 次反馈重算精确率，达标升级（可自动阻断）、不达标降级（仅提示）；等级变化要有下限保护（安全规则始终至少提示）。
- 要有「信任衰减与审计」：长期无反馈的规则信任度缓慢衰减（因为环境变化），避免陈旧的信任；等级调整记录可供审计。
- 追问钩子：能提出「信任等级要分维度——对不同文件类型/不同问题类型的信任可能不同，全局单一等级太粗糙」的候选人设计更精细。

```typescript
// 信任等级：靠近期精确率动态挣得
const feedback=[];
function trustLevel(ruleId) {
  const recent=feedback.filter(f=>f.rule===ruleId).slice(-20);
  if(!recent.length) return 'provisional'; // 无数据：临时级
  const precision=recent.filter(f=>f.actioned).length/recent.length;
  if(precision>=0.9) return 'high';
  if(precision>=0.7) return 'medium';
  return 'low';
}
function authority(level) {
  return { high:'可自动阻断', medium:'强提醒', low:'仅记录', provisional:'仅提示' }[level];
}
console.log(authority(trustLevel('SECRET')));
```
