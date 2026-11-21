---
title: [AGT-232] 中心化编排——主 Agent 怎么做任务分解与派发？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-232：Orchestrator-Worker 模式里，主 Agent 的任务分解怎么做好？

**答**:
- 分解质量决定一切：好的分解=子任务边界清晰（可独立验收）+ 依赖关系显式（哪些可并行哪些串行）+ 粒度适中（太细则协调成本高，太粗则单子任务过重）——分解失败是编排系统失败的第一原因。
- 任务书规范：每个子任务必须自带完整上下文（目标/背景/约束/产出格式/验收标准），不能假设子 Agent"知道"主对话的内容（AGT-228 隔离原则）——任务书是两个 Agent 间唯一的契约。
- 派发调度：无依赖子任务并行发（吞吐），有依赖的按 DAG 拓扑序执行；子任务失败的重试与降级策略在派发时声明（重试几次/失败是否阻塞全局）。
- 汇总与验收：主 Agent 收到结果先验格式与完整性（结构化校验），再做质量抽验（可对高风险子任务追加验证子任务），最后聚合——不合格打回而不是带病聚合。

```javascript
async function orchestrate(goal) {
  const plan = await planLLM(`分解任务：
    输出 [{id, goal, deps:[], accept, maxSteps}]`, goal);
  validateDAG(plan);                       // 环检测
  const done = new Map();
  for (const batch of topoBatches(plan)) { // 逐层并行
    const rs = await Promise.all(batch.map(t =>
      runWithRetry(() => worker(t, {
        goal: t.goal, accept: t.accept,    // 任务书含验收标准
        context: depsContext(t, done) }),  // 只注入依赖结果
        t.retries)));
    rs.forEach((r, i) => verify(r, batch[i].accept)); // 验收
    batch.forEach((t, i) => done.set(t.id, rs[i]));
  }
  return aggregate([...done.values()]);
}
```
