---
title: [1196] 检索服务高峰期怎么排队（水位控制）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 容量]
type: 面试题
---

## 1196：检索服务高峰期怎么排队（水位控制）

**答**：
- 水位两级：服务水位（并发检索数 / 容量）与队列水位（排队长度）；水位超过阈值触发「准入控制」——新请求排队或降级，而不是让所有请求一起变慢。
- 排队策略：按「用户可感知优先级」排序（在线会话 > 批量任务），队列超长时快速失败并给出预计等待——无限排队比失败更伤（用户干等）。
- 队头阻塞防护：单条慢查询（超大 top-k / 复杂过滤）会卡住队列，慢查询设独立队列 + 单独超时，与常规查询隔离。
- 追问钩子：水位阈值怎么定？——压测拐点的 70%；水位是「提前预警」不是「事后熔断」，到 70% 就要扩容或降级，等 100% 就晚了。

```ts
const pool = new Pool({ max: CAPACITY * 0.7 });      // 水位阈值 70%
async function search(q, { priority = 'online' } = {}) {
  if (pool.util() > 0.7 && priority === 'batch') return queue.push(q, { slow: true });
  if (queueLen() > MAX_QUEUE) throw new Busy(eta());  // 快速失败+预计等待
  return pool.run(() => engine.search(q, { timeout: slow(q) ? SLOW_TIMEOUT : NORMAL }));
}
```

