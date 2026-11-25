---
title: [AIC-677] 怎么用「价值流图」找 AI 真正加速了哪一环？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-677：怎么用价值流图（VSM）找 AI 真正加速了哪一环？

**答**：
- 结论先行：**价值流图把研发拆成「需求→设计→编码→评审→测试→部署」各阶段，记录每段的「增值时间 vs 等待时间」——AI 往往只加速了「编码」，但瓶颈可能不在编码**。优化了非瓶颈环节，整体交付速度不变（约束理论）。
- 画 VSM 的步骤：1) 选一个典型需求，记录它从提出到上线经过的每个阶段；2) 每段记「处理时间」（真正干活）和「等待时间」（排队/等审批/等依赖）；3) 标出 AI 介入的点与前后时间对比；4) 找出「等待时间最长」的瓶颈段。
- 常见发现：1) AI 把编码从 8h 缩到 2h，但评审排队等了 3 天——瓶颈在评审，优化编码无效；2) AI 生成测试快了，但测试环境排队跑——瓶颈在 CI 资源；3) 需求澄清不清楚导致返工——瓶颈在上游。
- 决策价值：**把 AI 投入放到真正的瓶颈上**——瓶颈在评审就投入 AI 审查/审查流程优化，而非再买更强的编码工具（AIC-671 审查净收益）。
- 追问钩子：为什么「优化非瓶颈环节」对整体交付没用？——因为整体流程速度由最慢的瓶颈决定；把编码从 8h 优化到 2h，如果评审要排队 3 天，总周期几乎不变——局部优化不转化为全局收益，这是系统思考的基本结论。

```typescript
type Stage = { name: string; processingH: number; waitingH: number; aiApplied: boolean };

function valueStream(stages: Stage[]) {
  const bottleneck = [...stages].sort((a, b) => b.waitingH - a.waitingH)[0];
  const total = stages.reduce((s, x) => s + x.processingH + x.waitingH, 0);
  const aiOnBottleneck = stages.some(s => s.name === bottleneck.name && s.aiApplied);
  return {
    totalLeadTime: total,
    bottleneck: bottleneck.name,
    aiOnBottleneck,
    advice: aiOnBottleneck ? 'AI 已投入瓶颈，继续优化' : `AI 未投入瓶颈 ${bottleneck.name}，优先把 AI 用在这里`,
  };
}

const stages = [
  { name: '编码', processingH: 2, waitingH: 0, aiApplied: true },   // AI 加速了
  { name: '评审', processingH: 1, waitingH: 72, aiApplied: false }, // 瓶颈！没 AI
  { name: '测试', processingH: 2, waitingH: 4, aiApplied: true },
];
const r = valueStream(stages);
console.log(r.bottleneck === '评审' && r.aiOnBottleneck === false);
console.log(r.advice.includes('评审')); // 建议把 AI 投到评审瓶颈
```
