---
title: [AIC-665] DORA 指标怎么适配 AI 结对开发的度量？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-665：DORA 四指标怎么适配 AI 结对开发？

**答**：
- 结论先行：**DORA 四指标（部署频率、变更前置时间、变更失败率、恢复时间）依然适用，但要「按 AI 参与拆分」才能看出 AI 的真实影响**——整体指标变好不等于 AI 的功劳，可能是别的因素（AIC-302 归因）。
- 逐项适配：1) **部署频率**：AI 加速了代码产出，部署频率是否提升？按「AI 辅助 PR / 人工 PR」分组对比；2) **变更前置时间**（commit→上线）：AI 主要缩短「编码」段，但评审/测试段可能成为新瓶颈——要看时间花在哪段（AIC-307）；3) **变更失败率**：AI 代码的失败率是升是降？这是提效幻觉的照妖镜（AIC-305）；4) **恢复时间**（MTTR）：AI 能否加速故障定位与修复（AIC-332 事故复盘）？
- 关键洞察：AI 把瓶颈从「写代码」转移到「评审与验证」——如果前置时间没缩短，大概率是人审不过来了，此时该优化的是审查流程而非再买 AI 工具。
- 归因方法：用「对照组」——同一团队引入 AI 前后的同期对比，或 AI 组 vs 非 AI 组，控制团队规模/项目复杂度变量。
- 追问钩子：为什么「变更失败率」是 AI 度量里最该盯的 DORA 指标？——因为速度类指标（部署频率/前置时间）容易被 AI 灌水式产出抬高，而失败率直接关联质量；如果失败率随 AI 使用上升，说明速度提升是「以质换速」的假象，必须停下来治理质量而非继续提速。

```typescript
type Change = { aiAssisted: boolean; leadTimeH: number; failed: boolean; restoreH: number };

function doraByGroup(changes: Change[]) {
  const calc = (g: Change[]) => ({
    count: g.length,
    avgLeadTime: g.reduce((s, c) => s + c.leadTimeH, 0) / (g.length || 1),
    failRate: g.filter(c => c.failed).length / (g.length || 1),
    avgRestore: g.reduce((s, c) => s + c.restoreH, 0) / (g.length || 1),
  });
  return {
    ai: calc(changes.filter(c => c.aiAssisted)),
    human: calc(changes.filter(c => !c.aiAssisted)),
  };
}

const changes: Change[] = [
  { aiAssisted: true, leadTimeH: 4, failed: true, restoreH: 2 },
  { aiAssisted: true, leadTimeH: 5, failed: false, restoreH: 0 },
  { aiAssisted: false, leadTimeH: 12, failed: false, restoreH: 0 },
];
const d = doraByGroup(changes);
console.log(d.ai.avgLeadTime < d.human.avgLeadTime);  // AI 前置时间短
console.log(d.ai.failRate > d.human.failRate);        // 但失败率更高 —— 提效幻觉信号
```
