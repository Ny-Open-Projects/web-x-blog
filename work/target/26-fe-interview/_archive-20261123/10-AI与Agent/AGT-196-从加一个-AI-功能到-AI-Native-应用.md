---
title: [AGT-196] 从「加一个 AI 功能」到 AI Native 应用，演进路线怎么规划？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-196：从「加一个 AI 功能」到 AI Native 应用，演进路线怎么规划？
**答**：
- 四阶段演进：Stage 1 单点增强（现有功能里加 AI 按钮，AI 是工具）；Stage 2 流程 AI 化（关键流程由 AI 编排，人做确认，AI 是副驾驶）；Stage 3 交互范式转变（以意图/对话为主要入口，传统 UI 退居精细化操作，AI 是界面）；Stage 4 AI Native（数据/权限/反馈闭环为 AI 而设计，产品形态本身由 AI 能力定义）。
- 判断卡点的信号：Stage 1→2 的门槛是「任务完成率与回滚机制」（AI 敢不敢碰主流程）；2→3 的门槛是「意图理解的覆盖与误触率」（对话入口的可用性）；3→4 的门槛是组织（数据闭环与团队结构）而非技术。
- 前端视角的形态变化：Stage 3 之后「页面」弱化为「画布」，组件由生成式 UI 动态组装（AGT-084），设计系统从视觉规范演进为「组件能力语义描述 + 约束」。
- 演进纪律：每阶段用指标验证价值后再进下一阶段（AGT-184 的指标体系），跳级推进通常死在信任度——用户还没信任 AI 碰主流程。

```typescript
// AI Native 成熟度评估与阶段门槛检查
interface StageSignals {
  taskCompletionRate: number;      // AI 任务完成率
  rollbackMechanism: boolean;      // 是否有回滚/撤销机制
  intentCoverage: number;          // 意图理解覆盖率
  falseTriggerRate: number;        // 误触率
  feedbackLoopClosed: boolean;     // 用户反馈是否闭环进训练/评测
}

export function assessStage(s: StageSignals): { stage: 1 | 2 | 3 | 4; nextGate: string } {
  if (!s.rollbackMechanism || s.taskCompletionRate < 0.6) {
    return { stage: 1, nextGate: '建设回滚机制，把任务完成率做到 60% 以上才进入流程 AI 化（Stage 2）' };
  }
  if (s.intentCoverage < 0.85 || s.falseTriggerRate > 0.05) {
    return { stage: 2, nextGate: `意图覆盖 ${s.intentCoverage} 需达 85% 且误触率降至 5% 以下，对话入口才可成为主界面（Stage 3）` };
  }
  if (!s.feedbackLoopClosed) {
    return { stage: 3, nextGate: '反馈闭环（用户行为 → 评测集 → 迭代）未闭环，无法支撑 AI Native 的持续进化（Stage 4）' };
  }
  return { stage: 4, nextGate: '已达标：重点转向数据资产、护栏体系与组织能力（AGT-198）' };
}
```
