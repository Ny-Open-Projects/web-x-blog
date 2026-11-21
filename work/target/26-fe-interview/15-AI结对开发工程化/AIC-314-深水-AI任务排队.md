---
title: [AIC-314] 把 20 个 AI 任务并行扔给多个 Agent 跑，如何避免冲突与混乱？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-314：把 20 个 AI 任务并行扔给多个 Agent 跑，如何避免冲突与混乱？
**答**：
- 冲突预检：按任务触碰文件集计算交集，交集大的任务串行或分区并行（git worktree 隔离）。
- 统一集成点：各 Agent 在独立分支产出，串行合并 + 每次合并后跑全量门禁。
- 共享资源排队：数据库迁移、依赖变更类任务全局串行队列。
- 失败隔离：单任务失败不阻塞队列，产出统一汇总报告给人裁决。

```javascript
function schedule(tasks: TaskCard[]) {
  const groups = packByFileConflict(tasks); // 文件冲突分桶
  return groups.map(g => ({
    mode: g.length > 1 ? 'worktree-parallel' : 'direct',
    serialQueue: g.filter(t => t.touchesMigration).map(t => t.id), // 全局串行
  }));
}
r
```
