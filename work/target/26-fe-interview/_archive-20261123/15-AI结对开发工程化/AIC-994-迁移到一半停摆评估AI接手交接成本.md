---
title: [AIC-994] 一个遗留迁移项目做到一半停摆了，现在想让 AI 接手剩余部分，如何评估「接手成本」是否划算？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-994：一个遗留迁移项目做到一半停摆了，现在想让 AI 接手剩余部分，如何评估「接手成本」是否划算？
**答**：
- 先评估「上下文可恢复性」：迁移进度、已做决策、未完成原因是否有清晰记录（ADR/看板/测试）——结论：如果这些信息缺失，AI 接手要先花大量成本「补眼睛」（呼应 AIC-990），可能得不偿失。
- 量化对比：估算「人接手成本 vs AI 接手成本（含上下文重建 + 生成 + 验证 + 返工）」；AI 的优势在机械转换，若剩余部分多是决策密集型（边界判断），AI 优势小。
- 做「小样验证」：挑一个小模块让 AI 试迁移，用其质量/耗时外推整体，而非凭感觉决定；同时判断是否值得继续——有时答案是「止损，冻结迁移」。
- 追问钩子：能提出「接手成本评估本身要包含一个选项：不迁移（维持现状/封装隔离）」，避免陷入『必须迁完』的思维定式——这是更高层的决策。

```typescript
// 接手成本对比 + 小样外推
function handoffDecision(ctx) {
  const aiCost = ctx.contextRecoverCost + ctx.trialTime*ctx.remainingModules
    + ctx.expectedRework;
  const humanCost = ctx.humanRate*ctx.remainingModules;
  const viable = aiCost < humanCost && ctx.trialQuality>=0.8;
  return {
    aiCost:+aiCost.toFixed(1), humanCost:+humanCost.toFixed(1),
    decision: viable?'AI接手':'人接手/冻结评估',
    note: ctx.contextRecoverCost>ctx.humanRate*2?'上下文缺失严重，先补记录':'' ,
  };
}
console.log(handoffDecision({contextRecoverCost:20,trialTime:2,remainingModules:10,
  expectedRework:5,humanRate:40,trialQuality:0.9}));
```
