---
title: [AIC-890] 怎么向不懂技术的老板解释「AI 到底提效了多少」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-890：怎么向不懂技术的老板解释「AI 到底提效了多少」？
**答**：
- 老板关心的不是「采纳率 85%」这种技术指标，而是**业务结果**：需求交付快了多少、成本省了多少、质量有没有变差。要把技术指标翻译成业务语言。
- 用**业务叙事 + 对照**：不说「AI 代码存活率提升 15%」，说「同样一个需求，以前要 5 天现在 3 天，我们抽了 20 个相似需求做了对照」——用对方能感知的单位（天、钱、事故数）。
- 要给**置信度与边界**：诚实说明「这是同类任务的统计趋势，不是每个需求都快 40%」，避免被追问时露馅；同时列出「哪些场景 AI 帮不上忙」——建立可信度而非画大饼。
- 用**具体案例**代替抽象数字：讲一个真实故事（某需求怎么被 AI 加速、遇到什么问题、如何解决），比一页 PPT 的数字更有说服力。结论前置、细节按需展开。
- 追问钩子：能说出「把技术指标翻译成业务结果 + 用对照和案例支撑 + 诚实说明边界」的候选人，具备技术领导力中的沟通能力。

```typescript
// 技术指标 → 业务语言的翻译层
function explainToBusiness(tech: { adoption:number; survival:number;
  cycleDaysBefore:number; cycleDaysAfter:number; bugsBefore:number; bugsAfter:number }) {
  const savedDays = tech.cycleDaysBefore - tech.cycleDaysAfter;
  return {
    headline: `同类需求交付周期缩短 ${savedDays} 天（约 ${Math.round(savedDays/tech.cycleDaysBefore*100)}%）`,
    quality: `线上缺陷 ${tech.bugsBefore} → ${tech.bugsAfter}，质量护栏未退化`,
    evidence: '基于 20 个相似需求的对照，非全部场景',
    caveat: '探索性/高风险任务提速有限，收益集中在标准化任务',
    // 不输出 adoption/survival 这类技术黑话
  };
}
console.log(explainToBusiness({ adoption:0.85, survival:0.75,
  cycleDaysBefore:5, cycleDaysAfter:3, bugsBefore:4, bugsAfter:3 }));
// headline: '同类需求交付周期缩短 2 天（约 40%）' + 质量与边界说明
```
