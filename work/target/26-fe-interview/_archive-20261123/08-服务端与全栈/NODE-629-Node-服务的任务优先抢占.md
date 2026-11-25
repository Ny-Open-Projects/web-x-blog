---
title: [NODE-629] Node 服务的任务抢占与公平调度（worker 池调度策略）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-629：任务抢占与公平调度
**答**:
- 调度问题：worker 池被长任务占满 → 新的高优任务排队久。策略：任务分级队列（NODE-627）+ worker 分配策略（空闲 worker 按优先级取任务）、长任务拆分（大任务 chunk 化——每 chunk 之间检查更高优队列——变相抢占）、抢占点设计（不可抢占段最小化——事务边界即让点 NODE-628）。
- 公平调度：多租户公平（租户间配额——防单租户占满池：加权轮询/配额并发上限 NODE-462）、防饿死（低优任务最小保证份额—— starvation 防护）、年龄老化（等待越久优先级渐升——老化策略）。
- 实现要点：调度器参数（池大小/每任务资源估算——并发度计算）、任务资源画像（CPU 型/IO 型混跑——分池避免 CPU 任务阻塞 IO 任务 NODE-306）、动态扩缩（积压驱动 worker 扩容——NODE-603 任务维度）。
- 观测：排队时长分布（按优先级——调度有效性）、抢占触发率/池利用率。
- 权衡：抢占复杂度 vs 优先级收益——大多数场景"分级队列 + 拆分"够用（真抢占需要任务可中断设计——默认不做）。
```javascript
// 调度器（空闲 worker 按优先级取）
scheduler.pick(worker) {
  for (const q of ['high', 'normal', 'low']) {                   // 顺序扫描 + 加权
    const t = q.popIf(worker.tierCompatible);
    if (t) return t;
  }
}
// 长任务让点：for (chunk of chunks) { await process(chunk); if (await higherWaiting()) yield; }
```
