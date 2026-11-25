---
title: [AGT-020] 什么是规划与反思（Plan-and-Reflect）？如何让 Agent 不跑偏？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-020：什么是规划与反思（Plan-and-Reflect）？如何让 Agent 不跑偏？
**答**：
- 规划：开始前让模型把目标拆成编号步骤清单，逐步执行，而不是一条 prompt 扔进去祈祷。
- 反思：每完成一步，让模型对照目标检查进展是否偏离，偏离则修正剩余计划。
- 修正后的计划替换原队列继续执行，形成"执行-检查-修正"闭环。
- 代价是反思本身多耗一次调用，简单任务可每 N 步反思一次。

```typescript
// Plan-and-Reflect：先拆解计划，执行中按需修正
async function planAndReflect(goal: string): Promise<string> {
  // 1. 规划：目标拆解为编号步骤
  const plan = await llmComplete(
    `目标：${goal}\n请拆解为编号步骤清单，每行一个步骤，只输出清单。`,
  );
  let results = '';
  let queue = plan.split('\n').filter((l) => /^\d+\./.test(l));

  while (queue.length > 0) {
    const step = queue.shift()!;
    const done = await agentLoop(`${results}\n执行步骤：${step}`);
    results += `\n[已完成] ${step}\n${done}`;

    // 2. 反思：对照目标检查，偏离则输出修正后的剩余计划
    const reflect = await llmComplete(
      `目标：${goal}\n当前进展：${results}\n剩余计划：${queue.join('\n') || '无'}\n` +
      '若进展偏离目标，输出修正后的剩余步骤清单；否则只输出 OK。',
    );
    if (reflect.trim() !== 'OK') {
      queue = reflect.split('\n').filter((l) => /^\d+\./.test(l));
    }
  }
  return results;
}
```
