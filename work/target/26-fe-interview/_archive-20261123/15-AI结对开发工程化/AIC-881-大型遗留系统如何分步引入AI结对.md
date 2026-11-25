---
title: [AIC-881] 一个十年的历史遗留系统，怎么分步引入 AI 结对而不翻车？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-881：一个十年的历史遗留系统，怎么分步引入 AI 结对而不翻车？
**答**：
- 遗留系统的难点不是 AI 不会写代码，而是 AI **不了解隐式约束**：那些「为什么这么写」只存在于老员工脑子里和十年前的工单里。上来就让 AI 大改必然翻车。
- 分步策略：**① 只读阶段**——先让 AI 做代码解释、生成文档、问答，人验证正确性，建立信任和上下文；**② 局部写入**——在边界清晰、测试完备的模块（如工具函数、新增接口）让 AI 改，严格 review；**③ 受限重构**——配合回归守卫（AIC-830）和规则文件，在核心模块做有测试的改动；**④ 常态化**——AI 成为默认工具，人聚焦架构与高风险决策。
- 前置基建：先补测试与回归守卫（没有安全网不敢让 AI 动老代码）、写规则文件记录「禁区」、整理模块 owner。
- 每个阶段设**退出条件**（如 AI 解释准确率 > 90% 才进入写入阶段），不靠感觉推进。
- 追问钩子：能说出「先补测试安全网再让 AI 动核心代码，且每阶段有量化准入门槛」的候选人，理解了遗留系统的风险控制。

```typescript
type Phase = { name: string; exitCriteria: (m: any) => boolean; hint: string };

const rollout: Phase[] = [
  { name:'只读问答', exitCriteria:m => m.explainAccuracy > 0.9,
    hint:'先让 AI 解释代码、补文档，人验证' },
  { name:'局部写入', exitCriteria:m => m.testCoverage > 0.6 && m.reviewPassRate > 0.8,
    hint:'在测试完备的模块小步改' },
  { name:'受限重构', exitCriteria:m => m.regressionGuards > 20 && m.escapedBugs === 0,
    hint:'靠回归守卫保护核心模块' },
  { name:'常态化', exitCriteria:() => true, hint:'AI 成默认工具，人管架构' },
];
function currentPhase(metrics: any) {
  return rollout.find(p => !p.exitCriteria(metrics))?.name ?? 'done';
}
console.log(currentPhase({ explainAccuracy:0.95, testCoverage:0.5 })); // '局部写入'（覆盖率不足，卡在此阶段）
```
