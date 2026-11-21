---
title: [ARC-002] 自研、开源二次开发、采购 SaaS，三类方案如何决策？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-002：自研、开源二次开发、采购 SaaS，三类方案如何决策？
**答**：
- 判断核心是"这件事是不是公司的差异化竞争力"：核心域倾向自研/深度定制，支撑域用开源，非技术核心且变化慢的可采购。
- 还要算总拥有成本 TCO：不只是开发成本，含维护人力、升级成本、人员离职风险。
- 自研的隐性成本最容易被低估（文档、测试、故障值班），要有明确的退出策略。

```typescript
type Option = 'build' | 'openSource' | 'buy';

interface DecisionInput {
  isCoreCompetency: boolean;   // 是否核心差异化能力
  teamHeadcount: number;       // 可投入人力
  timeToMarketWeeks: number;   // 交付窗口
  tco: { build: number; openSource: number; buy: number }; // 三年总成本(人日)
}

function decide(input: DecisionInput): Option {
  // 核心域且人力充足：自研掌握主动权
  if (input.isCoreCompetency && input.teamHeadcount >= 5) return 'build';
  // 非核心域：在开源和采购之间比 TCO 与定制空间
  if (!input.isCoreCompetency) {
    const needHeavyCustom = input.tco.openSource > input.tco.buy * 1.5;
    return needHeavyCustom ? 'buy' : 'openSource';
  }
  // 核心域但人力不足：开源二开 + 沉淀自研补丁层，保留替换能力
  return 'openSource';
}
// 要点：无论选哪个，都在业务与方案之间留一层防腐层（adapter），降低未来替换成本
```
