---
title: [AIC-083] Agent 执行长任务半路失败（构建挂/测试红）该怎么恢复？「失败即回滚」还是「失败即修复」？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-083：Agent 执行长任务半路失败（构建挂/测试红）该怎么恢复？「失败即回滚」还是「失败即修复」？
**答**：
- 策略取决于失败类型：agent 自己引入的失败（它改坏的）→ 修复优先，agent 拿着报错自迭代（这是它的核心能力）；存量失败（动手前测试就是红的）→ 先记录快照，修复不属于本任务的失败要显式分离 PR。
- 防止无限修复循环：设修复轮次上限（如 5 轮），超限停下来输出「失败报告 + 已尝试方案」，交人决策——agent 常见的坏行为是越修越烂还不停。
- 断点续作：长任务每步成功后提交 git（绿色快照），失败时回退到最后绿色快照重试而不是全盘重来；这也是「失败即回滚」的正确用法——按步回滚而非任务级回滚。
- 关键前提：任务开始前的基线必须是绿的（AIC-052），否则失败归因完全混乱。
- 追问钩子：恢复机制设计是区分「玩具 agent」和「生产 agent」的分水岭，面试能讲出轮次上限+快照回退就是加分的工程思维。

```javascript
// agent 修复循环（轮次上限 + 绿色快照回退）
async function agentFixLoop(task, { maxRounds = 5 } = {}) {
  const green = git.commitSnapshot('baseline');   // 任务前基线
  for (let i = 1; i <= maxRounds; i++) {
    await agent.step(task);
    const ok = await run(['tsc', '--noEmit']).then(() => run(['vitest', 'run'])).catch(() => false);
    if (ok) return { done: true, rounds: i };
    if (i < maxRounds) { git.resetTo(green); }    // 回到绿色快照重试，不叠加烂修复
  }
  return { done: false, report: await agent.summarizeFailures() }; // 超限交人
}
```
