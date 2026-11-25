---
title: [AIC-088] Agent 模式下「人类审批点」应该设在哪些位置？审批太频繁和太少各有什么问题？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-088：Agent 模式下「人类审批点」应该设在哪些位置？审批太频繁和太少各有什么问题？
**答**：
- 推荐审批点：任务开始时（确认计划——成本最低的干预点）、高危动作前（删文件、执行未白名单命令、改公共 API）、任务结束时（验收 diff）——三点式覆盖了「事前同意、事中拦截、事后负责」。
- 太频繁的问题：每步都审批等于人变成打字员，且审批疲劳后会无脑点确认（比不审批更危险——伪监督）。
- 太少的问题：错误在长链条中累积放大，最后一团糟时已难定位是哪步走偏。
- 设计原则：审批点设在「不可逆动作」和「方向性决策」处；可逆的、机械的步骤（改代码、跑测试）放行。频率随信任度动态调整——连续 N 个任务全绿可放宽，出一次事故收紧。
- 追问钩子：审批点的选择反映「信任的颗粒度」——高级工程师和 agent 的协作应该从「每步审批」演进到「只审计划和结果」。

```javascript
// 三点式审批模型（可逆性决定是否拦）
const approvalPolicy = {
  onStart: 'plan_review',                      // 计划审批
  before: (action) => action.reversible === false || action.risk === 'high',
  onEnd: 'diff_acceptance',
};
function shouldPause(action) {
  return approvalPolicy.before(action); // 删文件/外发/改API → 不可逆 → 暂停等人
}
```
