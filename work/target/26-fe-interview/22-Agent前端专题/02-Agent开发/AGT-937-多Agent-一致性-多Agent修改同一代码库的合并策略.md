---
title: [937] 多个 Agent 并行改同一代码库，怎么避免互相覆盖
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 一致性]
type: 面试题
---

## 937：多个 Agent 并行改同一代码库，怎么避免互相覆盖

**答**：
- 物理隔离优先：每个子 Agent 在独立 worktree/分支上工作，编排器统一合并；比「共享工作区加锁」少了大量协调成本。
- 合并策略分级：改动集文件不相交直接快进；相交时按「冲突文件归属优先级」（任务书里声明主责 Agent）合并，冲突超阈值降级为串行重跑。
- 合并后必须回归验证：跑受影响测试 + 构建，失败则二分定位到某个 Agent 的分支回滚。
- 追问钩子：为什么不用 CRDT 之类合并？——代码合并的语义正确性靠测试而不靠文本合并算法，工程上分支隔离 + 测试验证最可靠。

```ts
async function parallelEdit(tasks) {
  const branches = await Promise.all(tasks.map(t =>
    worktree.fork(t.id, t.files)));          // 文件集隔离分配
  const results = await Promise.all(tasks.map((t, i) =>
    agent.run(t, { cwd: branches[i] })));
  const merged = await mergeSequential(branches, {
    conflictOwner: t => t.ownerAgent,        // 冲突按主责归属
    verify: () => runTests(touchedFiles()),  // 合并后回归
  });
  if (!merged.ok) await rollback(merged.blamed); // 定位回滚
}
```

