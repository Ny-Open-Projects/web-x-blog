---
title: [MFW-458] 笔试：手写 Suspense fallback 优先级调度器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-458：Suspense 边界优先级调度器
**需求**：实现 `createSuspenseScheduler()`：1) `schedule(boundary)`，boundary = { id, priority(1 最高), estMs }；2) 并发渲染配额 `concurrency`（默认 3），同优先级按 estMs 短任务优先（SJF，先给用户可感知内容）；3) 任务完成/超时（estMs 超 5s 直接 reject 不占坑）释放配额并自动补位；4) 返回 `snapshot()` 查看运行/排队分布——用于流式 SSR 决定先 flush 哪个洞。

```javascript
export function createSuspenseScheduler({ concurrency = 3 } = {}) {
  const running = new Map() // id -> { priority, estMs }
  const queue = []
  const done = []
  const drain = () => {
    while (running.size < concurrency && queue.length) {
      queue.sort((a, b) => a.priority - b.priority || a.estMs - b.estMs)
      const t = queue.shift()
      running.set(t.id, t)
      setTimeout(() => settle(t), Math.min(t.estMs, 5000))
    }
  }
  const settle = (t) => {
    running.delete(t.id); done.push(t.id); drain()
  }
  return {
    schedule(b) {
      if (b.estMs > 5000) { done.push(b.id); return Promise.reject(new Error('over-budget')) }
      return new Promise(res => { queue.push({ ...b, res }); drain() })
    },
    snapshot: () => ({
      running: [...running.keys()], queued: queue.map(t => t.id), done: [...done],
    }),
  }
}
```

**评分点**：
- 配额约束（concurrency 上限——服务器不被慢洞占满）
- 同优先级 SJF（短洞先 flush，TTFB 内可见内容最大化）
- estMs 超 5s 拒绝（超时边界提前裁决，不无限占坑）
- 完成补位 + snapshot 可观测（调度器必须可调试）
