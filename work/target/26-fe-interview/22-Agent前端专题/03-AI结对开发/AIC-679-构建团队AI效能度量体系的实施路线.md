---
title: [AIC-679] 从零构建团队 AI 效能度量体系，路线怎么走？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-679：从零构建团队 AI 效能度量体系，路线怎么走？

**答**：
- 结论先行：**分四步走——「定义价值 → 埋点采集 → 建看板 → 闭环改进」，且从「少而准」的指标开始，别一上来搞大而全**（古德哈特定律 AIC-676）。
- 第一步定义价值：先回答「AI 要帮团队解决什么问题」——是提速、提质还是降本？围绕价值选 1 个北极星 + 2-3 个护栏指标（AIC-663），不要贪多。
- 第二步埋点采集：确定每个指标的数据来源——补全事件（IDE 遥测 AIC-178）、PR 数据（git）、缺陷数据（issue 系统）、存活判定（代码变更追踪）。缺数据的指标先放弃，别拍脑袋估。
- 第三步建看板：把指标做成团队可见的看板（AIC-050），重点是「趋势」和「分层」——按任务复杂度/人员经验拆开，防辛普森悖论（AIC-672）。看板是给团队自己看的，不是给上级考核用的。
- 第四步闭环改进：定期（如双周）复盘看板，针对「退化指标」找原因并调整（prompt 规范/流程/工具），验证改进效果——度量不闭环就是浪费。
- 追问钩子：为什么「从少而准开始」比「一次建全」更现实？——因为指标越多，采集成本越高、口径越难统一，且容易被游戏化；先跑通 1+2 个指标形成闭环，证明有价值后再逐步扩展——度量体系是「长出来的」不是「设计出来的」。

```typescript
type Phase = { step: number; name: string; output: string; done: boolean };

function roadmap(current: number): { next: Phase|null; progress: number } {
  const phases: Phase[] = [
    { step: 1, name: '定义价值', output: '北极星+护栏指标', done: current >= 1 },
    { step: 2, name: '埋点采集', output: '数据源接入', done: current >= 2 },
    { step: 3, name: '建看板', output: '分层趋势看板', done: current >= 3 },
    { step: 4, name: '闭环改进', output: '双周复盘机制', done: current >= 4 },
  ];
  return {
    next: phases.find(p => !p.done) || null,
    progress: phases.filter(p => p.done).length / phases.length,
  };
}

console.log(roadmap(2).next?.name === '建看板');
console.log(roadmap(4).next === null && roadmap(4).progress === 1);
```
