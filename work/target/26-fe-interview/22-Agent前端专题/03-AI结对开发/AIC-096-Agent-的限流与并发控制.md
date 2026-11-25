---
title: [AIC-096] 多个 Agent 并发改同一仓库怎么办？文件锁、任务队列与冲突检测怎么做？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-096：多个 Agent 并发改同一仓库怎么办？文件锁、任务队列与冲突检测怎么做？
**答**：
- 并发场景真实存在：多个 ai-fix 任务、多个成员的 agent 同时工作、CI 机器人与本地 agent 撞车——不加控制会产生互相覆盖与「修 A 破 B」。
- 控制三层：① 任务队列——同仓库任务串行化或按包分区并行（ui 包队列、goods 包队列）② 文件锁——任务申请它计划改动的文件集锁，冲突任务等待或重排 ③ 冲突检测——合并前 rebase + 语义冲突检查（都改了同一函数），冲突则回炉。
- 实操简化：多数团队规模下「每仓库同时只跑 1 个写任务」就够，并行收益远小于冲突成本；读任务（检索、分析）可无限并发。
- git 层兜底：agent 每个 task 独立分支，合并走正常 PR 流程，冲突由人类解决——绝不允许多 agent 直接 push 同一分支。
- 追问钩子：这个问题的本质是「agent 也需要并发控制原语」，能把经典工程手段（锁/队列/幂等）迁移过来就是加分。

```javascript
// 简化任务队列 + 文件锁
class AgentQueue {
  #locks = new Map(); // file -> taskId
  async enqueue(task) {
    const conflict = task.files.some(f => this.#locks.has(f));
    if (conflict) return this.#waitAndRetry(task);
    task.files.forEach(f => this.#locks.set(f, task.id));
    try {
      const branch = `agent/${task.id}`;
      git.checkout(branch);
      await agent.run(task);
      return await openPR(branch, { label: 'agent' });
    } finally {
      task.files.forEach(f => this.#locks.delete(f));
    }
  }
}
```
