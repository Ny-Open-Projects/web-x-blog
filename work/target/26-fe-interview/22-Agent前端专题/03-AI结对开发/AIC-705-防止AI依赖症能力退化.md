---
title: [AIC-705] 结对开发中如何防止 AI 依赖症导致的能力退化
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-705：结对开发中如何防止 AI 依赖症导致的能力退化

**答**：
- 结论先行：把 AI 定位成「加速器」而非「替代品」——关键能力（架构判断、调试、安全直觉）必须有「无 AI 保留训练」，否则团队会丧失验证 AI 输出的能力，而验证能力正是 AI 时代的核心竞争力。
- 三个机制：1) 定期「无 AI 演练」（断网手写核心模块 / 排障）；2) 新人必须先独立实现再对照 AI 版本，禁止一上来就 Copilot；3) 把「能解释 AI 代码为什么错」纳入能力评估，而非「能生成多少代码」。
- 风险本质：验证者一旦失去被验证的能力，就退化成「盲目点同意」，AI 错误会直接流入生产（RBL-550 盲目信任）。
- 追问钩子：为什么 senior 工程师比 junior 更能安全使用 AI？——senior 有「识别错误」的领域知识，能把 AI 产出当草稿而非答案。

```javascript
// 能力保留计划：按「是否可委托」分级训练
const SKILL_TIERS = {
  delegate: ['样板代码', '格式转换', 'mock 数据'],       // 可放心交给 AI
  verify: ['重构', '单测生成', 'API 迁移'],             // AI 生成 + 人强验证
  preserve: ['架构决策', '安全审查', '故障定位'],       // 无 AI 保留训练
};
function trainingPlan(skills) {
  return skills.map(s => ({
    skill: s,
    mode: SKILL_TIERS.preserve.includes(s) ? 'no-ai-drill'
        : SKILL_TIERS.verify.includes(s) ? 'ai-plus-review' : 'delegate',
  }));
}
console.log(trainingPlan(['架构决策', '重构', 'mock 数据']));
// [{架构决策:no-ai-drill}, {重构:ai-plus-review}, {mock 数据:delegate}]
```
