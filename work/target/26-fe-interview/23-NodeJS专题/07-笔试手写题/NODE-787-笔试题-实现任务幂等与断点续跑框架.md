---
title: [NODE-787] 笔试题——实现任务幂等与断点续跑框架？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-787：手写任务框架

**需求与边界**：
- 需求：长任务框架（SCN-NODE-667）——① 任务幂等（任务 ID + 步骤断点——重跑跳过已完成步骤）；② 断点存储（步骤进度——SCN-联想-499 断点续跑）；③ 超时杀与恢复（孤儿任务——SCN-NODE-667）；④ 任务状态查询（进度 API——SCN-FIN-512）。
- 边界：① 步骤幂等键（步骤级唯一约束——重跑跳过）；② 死任务的检测（心跳超时——任务进程崩溃后的孤儿标记）；③ 恢复策略（从断点步骤继续——非从头）。

**答**：
```javascript
class TaskRunner {
  async run(task) {
    const done = await getDoneSteps(task.id);          // 断点：已完成步骤（SCN-联想-499）
    for (const step of task.steps) {
      if (done.has(step.name)) continue;               // 幂等：跳过已完成
      const ok = await claimStep(task.id, step.name);  // 步骤级 claim（幂等键——SCN-NODE-655）
      if (!ok) continue;                               // 其他实例在做
      try {
        await step.exec({ task, signal: heartbeatSignal(task.id) });   // 心跳（SCN-NODE-667 孤儿检测）
        await markStepDone(task.id, step.name);        // 断点推进
      } catch (e) { markFailed(task.id, step.name, e); throw e; }
    }
    await complete(task.id);
  }
  report(taskId) {                                     // 进度 API（SCN-FIN-512）
    return { done: getDoneSteps(taskId).size, total: steps.length };
  }
}
// 孤儿检测：心跳超时 → 标记中断 → 断点恢复
cron('*/1m', () => tasksWithoutHeartbeat(5 * 60_000).forEach(requeueFromCheckpoint));
```

**评分点**:
- 步骤级断点 + claim（幂等键——SCN-联想-499/NODE-655）。
- 心跳 + 孤儿检测（超时任务回收重跑——SCN-NODE-667）。
- 断点恢复（从断点步骤继续——非从头）。
- 进度 API（SCN-FIN-512 任务化）。
