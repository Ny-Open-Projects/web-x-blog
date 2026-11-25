---
title: [AIC-105] 如何度量团队的 AI 使用健康度？「过度依赖」的信号有哪些？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-105：如何度量团队的 AI 使用健康度？「过度依赖」的信号有哪些？
**答**:
- 健康度看板四象：产出质量（存活率、回滚率）、效率（合并周期）、能力保持（不查 AI 的手写考核通过率）、依赖结构（AI 产出占比、独立完成任务占比）。
- 过度依赖信号：① 成员无法解释自己提交的代码 ② 脱离 AI 后基础编码速度显著下降 ③ review 时间趋近于零但线上缺陷率上升 ④ 方案讨论时全部回答「问 AI」。
- 度量手段要温和：定期（季度）的「无 AI 实战演练」——30 分钟内手写一个小功能，看正确率分布而不是速度；个人数据只反馈本人，不做排名（避免变成监控）。
- 组织级信号更危险：新人成长曲线变缓（AIC-068）说明团队把学习外包了，这是慢性损伤。
- 追问钩子：健康度的目标是「AI 放大能力而不是替代能力」，度量是手段，谈话和制度调整才是行动。

```javascript
// 依赖结构健康度计算
function health(members) {
  return members.map(m => ({
    name: m.name,
    aiShare: m.aiCommits / m.totalCommits,
    soloPass: m.noAiAssessment.pass,       // 季度无AI演练
    explainRate: m.explainedOK / m.reviewedCommits,
    flag: m.explainRate < 0.6 || !m.noAiAssessment.pass ? 'TALK' : 'OK',
  }));
}
```
