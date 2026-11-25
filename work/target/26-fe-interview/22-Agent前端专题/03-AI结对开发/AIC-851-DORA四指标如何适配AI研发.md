---
title: [AIC-851] DORA 四指标放到 AI 辅助研发里还适用吗？怎么改造？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-851：DORA 四指标放到 AI 辅助研发里还适用吗？怎么改造？
**答**：
- DORA 四指标（部署频率、变更前置时间、变更失败率、恢复时间）依然**方向正确**——AI 的价值最终要体现在流动效率与稳定性上——但需要扩展以覆盖 AI 特有的质量风险。
- 改造点：**变更前置时间**要拆成「人类构思时间 / AI 生成时间 / review 时间」，否则无法判断 AI 到底省在哪；**变更失败率**要标注「是否涉及 AI 生成代码」，识别 AI 是否拉高失败率。
- 新增第五维：**AI 代码存活率 / 回滚率**作为质量护栏——AI 可能让部署频率飙升但回滚率也飙升，这种「虚假提速」DORA 原指标看不出来。
- 注意度量口径：AI 让提交粒度变细（小步快跑），部署频率天然升高，不能简单和 AI 前对比，要用「价值交付周期」做归一化校准。
- 追问钩子：能说出「DORA 要加 AI 专属护栏指标，且要拆分前置时间才看得到 AI 的真实作用点」的候选人，既有框架又有改良能力。

```typescript
type Change = {
  id: string; humanMinutes: number; aiMinutes: number; reviewMinutes: number;
  failed: boolean; aiGenerated: boolean; rolledBack: boolean;
};

function doraAI(changes: Change[]) {
  const elapsed = (k: 'humanMinutes'|'aiMinutes'|'reviewMinutes') =>
    changes.reduce((s, c) => s + c[k], 0) / (changes.length || 1);
  const withAI = changes.filter(c => c.aiGenerated);
  return {
    leadTimeBreakdown: { human: elapsed('humanMinutes'), ai: elapsed('aiMinutes'),
      review: elapsed('reviewMinutes') },          // 拆开看 AI 省在哪
    changeFailureRate: +(changes.filter(c => c.failed).length / (changes.length || 1)).toFixed(3),
    aiFailureGap: +( // AI 代码 vs 非 AI 代码的失败率差
      withAI.filter(c => c.failed).length / (withAI.length || 1) -
      changes.filter(c => !c.aiGenerated && c.failed).length /
      (changes.filter(c => !c.aiGenerated).length || 1)).toFixed(3),
    aiRollbackRate: +(withAI.filter(c => c.rolledBack).length / (withAI.length || 1)).toFixed(3),
  };
}
// aiFailureGap > 0 且 rollbackRate 高 → AI 在"虚假提速"，需要干预
```
