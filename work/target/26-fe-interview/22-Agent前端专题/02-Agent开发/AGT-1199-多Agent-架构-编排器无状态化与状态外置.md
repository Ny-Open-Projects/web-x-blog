---
title: [1199] 编排器怎么做到无状态（可水平扩展）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 架构]
type: 面试题
---

## 1199：编排器怎么做到无状态（可水平扩展）

**答**：
- 无状态化三外置：任务状态外置（黑板/步骤进度进 Redis/DB，编排器实例只做计算）、会话上下文外置（按 taskId 存取）、预算计数外置（原子操作防并发超支）——实例随时可增减/崩溃重启，任务不丢。
- 技术要点：状态读写加版本乐观锁（并发步骤写同一状态）、实例崩溃后的任务接管（锁 TTL 过期由健康实例续跑，幂等前提是步骤可重入）。
- 收益：编排器可按任务量水平扩展，发布重启不停服务（在途任务由其他实例接管）。
- 追问钩子：状态外置的性能代价？——每步多一次状态读写（毫秒级），相对 Agent 步骤的秒级耗时占比小；但高频小步骤（循环内）要批量合并读写，否则状态层成为新瓶颈。

```ts
// 无状态编排器：状态全外置
async function runTask(task) {
  const state = await store.load(task.id);          // 每步从外部读
  for (const step of state.pending) {
    const lock = await store.lock(task.id, step.id, { ttl: 60000 });
    if (!lock) continue;                            // 其他实例在跑
    const r = await execute(step);                  // 步骤可重入（幂等）
    await store.cas(task.id, { done: { [step.id]: r } }, lock.ver); // 乐观锁写
  }
}
```

