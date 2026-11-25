---
title: [1192] 「先规划再执行」模式有哪些典型故障
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 模式]
type: 面试题
---

## 1192：「先规划再执行」模式有哪些典型故障

**答**：
- 四类典型故障：计划过时（执行环境变了计划未更新——文档删了计划还在引用）、计划过细（每步都定死，执行遇到小变化就卡死）、计划过粗（只有方向没有完成标准，执行自由发挥）、计划-执行脱节（执行者没理解计划意图，字面执行）。
- 对策：计划带「有效性条件」（执行每步前校验前置条件，失效即重规划）；完成标准可验证（程序判断）；关键意图写入计划（不只写步骤，写「为什么这么做」）。
- 重规划的成本控制：重规划触发条件预定义（前置失效/连续失败），不是每次小失败都重规划（避免震荡），重规划次数计入预算。
- 追问钩子：怎么判断「计划质量」？——用历史任务回放：好计划的指标是「零重规划完成率」和「步骤完成标准的可判率」，这两项进规划器的评估集。

```ts
async function planExecute(task) {
  let plan = await planner.run(task);           // 计划含完成标准与意图说明
  for (let i = 0; i < plan.steps.length; i++) {
    const s = plan.steps[i];
    if (!await valid(s.precondition)) {         // 前置失效 -> 重规划
      if (++replans > MAX_REPLAN) return escalate(task);
      plan = await planner.run(task, { remaining: plan.steps.slice(i), why: s.precondition });
      i = -1; continue;
    }
    await execute(s, { intent: plan.intent });  // 意图随步骤传递
  }
}
```

