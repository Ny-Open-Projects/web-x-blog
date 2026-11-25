---
title: [1152] 「计划→执行→复查」三阶段的工程实现要点
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 模式]
type: 面试题
---

## 1152：「计划→执行→复查」三阶段的工程实现要点

**答**：
- 计划阶段产出「可校验的计划」：步骤、依赖、每步的完成标准（可程序判断），计划本身先过「计划评审」（规则校验可行性 + LLM 挑漏洞），坏计划不进执行——执行返工的大头是计划缺陷。
- 执行阶段「边执行边校验」：每步完成即按标准自检，失败快速回退到最近一致点而不是从头再来。
- 复查阶段对照「原始任务」做终验：覆盖任务书全部验收标准 + 与计划比对（计划外的改动要解释），复查不通过附「差异报告」回执行或人工。
- 追问钩子：计划评审会不会太慢？——只对高风险/长任务开启全评审，短任务用「轻校验」（可行性规则），按预估时长与风险分级。

```ts
async function planExecReview(task) {
  const plan = await planner.run(task);
  const ok = await planReview(plan, { rules: feasibility, llm: task.risk === 'high' });
  if (!ok) return replan(task, ok.issues);
  const exec = await execute(plan, { checkpoint: true });   // 边执行边校验
  const final = await review(exec, task.acceptance);        // 对照任务书终验
  if (!final.pass) return escalate(task, final.diffReport);
  return exec;
}
```
