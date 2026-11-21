---
title: [AGT-464] 笔试题——实现计划修正器（失败步骤分析+计划重排+依赖更新）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-464：手写计划修正：失败归因、计划重排、依赖图动态更新、回滚选择

**需求与边界**：
- 输入：原计划（DAG）、失败步骤与原因；输出：修正后的计划。
- 边界要求：① 失败归因（可重试/需换法/需新步骤）；② 重排只影响受影响子图（不推翻全局）；③ 新步骤注入依赖图（环检测 AGT-407 联动）；④ 已成功步骤保留（不重做）。

**答**：
```javascript
async function replan(plan, failure, { llmAnalyze, detectCycle }) {
  // 1. 归因
  const cause = await llmAnalyze({
    step: failure.step, error: failure.error,
    options: ['retry', 'alternative', 'new_step', 'skip'] });
  const done = plan.filter(s => s.status === 'done');
  if (cause.action === 'retry') {
    failure.step.retries = (failure.step.retries ?? 0) + 1;
    if (failure.step.retries <= 2) return plan;    // 重试上限内
    cause.action = 'alternative';                  // 超限换法
  }
  if (cause.action === 'alternative') {
    // 2. 换方法：替换该步骤实现，保留目标
    failure.step.implementation = cause.alternative;
    failure.step.status = 'pending';
    failure.step.retries = 0;
  } else if (cause.action === 'new_step') {
    // 3. 注入前置步骤（含依赖声明）
    const steps = cause.newSteps.map(s => ({
      ...s, status: 'pending',
      deps: [...(s.deps ?? []), ...done.map(d => d.id)] }));
    plan.splice(plan.indexOf(failure.step), 0, ...steps);
    failure.step.deps.push(...steps.map(s => s.id));
    if (detectCycle(plan))                         // 环检测
      throw new Error('修正后计划存在环');
  } else {
    // 4. 跳过：下游依赖降级（部分结果）
    failure.step.status = 'skipped';
    plan.filter(s => s.deps.includes(failure.step.id))
      .forEach(s => { s.degraded = true;
        s.degradedBy = failure.step.id; });
  }
  // 已成功步骤保留（不重做），只重排 pending
  return plan;
}
```

**评分点**:
- 四类归因处置（retry 带上限/alternative 换法/new_step 注入/skip 降级下游）。
- new_step 注入后环检测（计划图完整性）。
- 已完成步骤保留不重做，只重排 pending——修正最小化。
- 下游降级标记（degradedBy）可追溯。
