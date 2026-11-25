---
title: [AIC-893] 怎么评估团队 AI 协作能力到了哪一级？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-893：怎么评估团队 AI 协作能力到了哪一级？
**答**：
- 成熟度模型要**可观测、可落地**，别搞五级九等的主观打分。一个实用框架分 4 级：**L1 个人使用**（少数人用 AI 补全，无规范）、**L2 团队规范**（有规则文件、统一工具、review 要求）、**L3 工程化**（评测集、门禁、血缘、度量平台，质量可量化）、**L4 平台化/自治**（自助服务、能力市场、域自治，平台隐形化）。
- 每级要有**客观判据**而非感觉：如 L2 的判据是「80% 的 PR 经过 AI review + 有版本化的规则文件」；L3 是「核心模块有 golden 集 + 线上问题可自动归因」；L4 是「自助率 > 80%」。
- 评估目的是**找下一步改进点**，不是给团队贴标签排名；不同团队因业务性质目标级别不同（探索型业务可能 L2 足够，大规模业务需要 L4）。
- 成熟度要**动态**：团队会进退（人员流动、项目变化），定期复评；晋级要有「稳定保持 N 个月」的要求，避免为冲级做表面功夫。
- 追问钩子：能说出「每级有客观判据 + 评估是为了找改进点而非排名 + 不同业务目标级别不同」的候选人，把成熟度模型用成了改进工具而非 KPI。

```typescript
type Level = 1 | 2 | 3 | 4;
const criteria: Record<Level, (m: any) => boolean> = {
  1: () => true,
  2: m => m.ruleFilesVersioned && m.aiReviewCoverage > 0.8,
  3: m => criteria[2](m) && m.goldenSets > 0 && m.autoAttribution,
  4: m => criteria[3](m) && m.selfServiceRate > 0.8 && m.capabilityMarket,
};
function maturity(m: any): Level {
  for (const l of [4, 3, 2, 1] as Level[]) if (criteria[l](m)) return l;
  return 1;
}
console.log(maturity({ ruleFilesVersioned:true, aiReviewCoverage:0.85,
  goldenSets:3, autoAttribution:true, selfServiceRate:0.5, capabilityMarket:false }));
// 3（L3 达成，L4 自助率不足）
// 用途：指出下一步该补什么（自助化）而非给团队排名
```
