---
title: [1283] 笔试手写：实现 Agent 任务队列公平调度器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## 1283：笔试手写：实现 Agent 任务队列公平调度器

**答**：实现 fairScheduler()：多会话任务队列。enqueue(sessionId, task)；每轮调度在「任务数最多的会话」优先取任务（长会话公平），同数时 FIFO；任务执行返回 Promise，未完成的会话下轮继续。输出 schedule(all) 执行顺序数组。同会话任务保持原序（会话内串行）。

```js
function fairScheduler() {
  const queues = new Map();
  return {
    enqueue(sessionId, task) {
      if (!queues.has(sessionId)) queues.set(sessionId, []);
      queues.get(sessionId).push(task);
    },
    schedule() {
      const order = [];
      while ([...queues.values()].some(q => q.length)) {
        // 取任务数最多的会话（平局取最早入 Map 的）
        let best = null, max = 0;
        for (const [sid, q] of queues) {
          if (q.length > max) { max = q.length; best = sid; }
        }
        order.push({ sessionId: best, task: queues.get(best).shift() });
      }
      return order;
    },
  };
}
```

**评分点**：
- 按会话队列长度取下一任务（多会话公平性核心）
- Map 迭代序保证平局 FIFO（插入序稳定）
- 同会话 shift 保持会话内串行
- 能讨论：公平策略与优先级/SLA 的冲突（公平 vs 重要先行的权衡）
