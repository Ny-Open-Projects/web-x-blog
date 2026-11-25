---
title: [AIC-680] 给 AI Agent 设计任务队列，优先级和风暴保护怎么做？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-680：给 Agent 设计任务队列，优先级和风暴保护怎么做？

**答**：
- 结论先行：**任务队列要防两类问题——「饿死」（低优先级永远排不上）和「风暴」（瞬时大量任务打爆 API/资源）**。解法分别是「老化提升优先级」和「限流 + 背压 + 熔断」。
- 优先级设计：1) 多队列（高/中/低），高优先级先出队；2) **老化机制**：低优先级任务等待超过阈值自动提升一级，防止饿死；3) 年龄 + 优先级综合打分排序，而非纯 FIFO。
- 风暴保护：1) **令牌桶限流**：限制单位时间的 API 调用速率（AIC-174 限流器）；2) **并发上限**：同时运行的 Agent 任务数封顶，超出的排队；3) **背压**：队列满时拒绝新任务或降级（快速失败），而不是无限堆积；4) **熔断**：下游模型连续失败就暂停消耗，避免雪崩（AIC-324 成本异常）。
- 可观测性：队列长度、等待时长、拒绝数、各优先级吞吐量——这些指标暴露队列是否健康（AIC-114 任务队列）。
- 追问钩子：为什么「老化」对任务队列很重要？——因为纯优先级队列在高优先级任务持续流入时，低优先级任务会永远排不上（饿死）——这些任务可能是重要的清理/优化工作；老化让「等得够久」本身成为优先级提升的理由，保证每个任务最终都能执行。

```typescript
type Task = { id: string; priority: number; enqueuedAt: number };

class AgentQueue {
  private queue: Task[] = [];
  constructor(private maxConcurrent: number, private maxWaitMs: number) {}

  push(t: Task): boolean {
    if (this.queue.length >= this.maxConcurrent * 10) return false; // 背压：队列满拒绝
    this.queue.push(t);
    return true;
  }

  pop(now: number): Task | undefined {
    // 老化：等待超过阈值的任务优先级 +10
    const scored = this.queue.map(t => ({
      t,
      effective: t.priority + (now - t.enqueuedAt > this.maxWaitMs ? 10 : 0),
    }));
    scored.sort((a, b) => b.effective - a.effective);
    const picked = scored[0]?.t;
    this.queue = this.queue.filter(t => t.id !== picked?.id);
    return picked;
  }
}

const q = new AgentQueue(2, 1000);
q.push({ id: 'low', priority: 1, enqueuedAt: 0 });
q.push({ id: 'high', priority: 5, enqueuedAt: 500 });
console.log(q.pop(100)?.id === 'high'); // 高优先级先出
q.push({ id: 'low2', priority: 1, enqueuedAt: 100 });
console.log(q.pop(2000)?.id === 'low'); // low 等超1s，老化后反超
```
