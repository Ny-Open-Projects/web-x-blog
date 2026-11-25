---
title: [AIC-114] 如何给 Agent 设计「任务队列」？任务优先级、重试与风暴保护怎么处理？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-114：如何给 Agent 设计「任务队列」？任务优先级、重试与风暴保护怎么处理？
**答**：
- 队列形态：按仓库/包分区的 FIFO 为主（写任务串行，AIC-096），优先级队列用于插队（线上 hotfix 任务）。
- 任务入队前过滤：重复任务去重（同一 bug 两条 issue）、低价值任务拦截（拼写修正在 CI 脚本处理，不值得 agent 出动）。
- 重试策略：区分可重试（限流、超时——退避重试）与不可重试（任务定义缺陷——重试只会烧钱）；失败 2 次的任务降级为「人工 backlog」。
- 风暴保护：单仓库并发上限（写任务 1 个）、单团队并发上限（防止成本风暴）、连续失败熔断（同一类型任务连续 5 次失败暂停该类任务入队并告警）。
- 追问钩子：队列 metrics（等待时长、失败分布）反哺任务分类——高频失败类别的任务卡模板要修（AIC-038）。

```javascript
// 任务队列核心（优先级 + 熔断）
class TaskQueue {
  #q = []; #failStreak = new Map();
  push(task, { priority = 0 } = {}) {
    if ((this.#failStreak.get(task.kind) ?? 0) >= 5) throw new Error(`${task.kind} 熔断中`);
    this.#q.push({ ...task, priority }); this.#q.sort((a, b) => b.priority - a.priority);
  }
  async next() {
    const t = this.#q.shift();
    try { return await this.#run(t); } catch (e) {
      t.retries = (t.retries ?? 0) + 1;
      if (t.retries < 2 && e.retryable) return this.push(t, { priority: t.priority });
      const s = (this.#failStreak.get(t.kind) ?? 0) + 1;
      this.#failStreak.set(t.kind, s);
      throw e;
    }
  }
}
```
