---
title: [AGT-335] 浏览器 Agent——网页自动化任务 Agent 怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-335：让 Agent 替用户操作网页（填表/比价/预订）怎么设计？

**答**:
- 页面理解：DOM/accessibility tree 结构化提取（优先）+ 截图视觉校验——DOM 给精确元素，视觉确认渲染状态一致（动态页面 DOM 与所见可能不一致）。
- 任务执行模式：计划先行（页面探索→生成操作计划→人确认计划→执行）优于边看边做——计划模式让用户预知 Agent 将做什么（信任+安全），执行中每步快照可回溯。
- 边界与安全：仅用户授权的站点与操作范围（域名白名单）、表单提交/支付类操作强确认（AGT-286）、登录凭证经安全通道注入不在上下文明文（AGT-285）、反爬与站点条款合规。
- 失败与降级：页面结构突变（A/B 实验/改版）导致定位失败——重试策略（视觉重定位/放宽匹配）+ 卡住转人（"该页面无法继续，请手动处理此步"）；任务日志供用户核查。

```javascript
async function browserTask(goal) {
  const plan = await exploreAndPlan(goal);   // 页面探索出计划
  await confirm(plan);                        // 计划级确认
  for (const step of plan.steps) {
    const el = locate(step, { dom: true, visual: true });
    await act(el, step.action);
    await verify(step);                       // 步后验证
    if (stuck()) return handoff(step);        // 转人
  }
}
// 域名白名单 + 支付强确认 +
// 凭证不进上下文。
```
