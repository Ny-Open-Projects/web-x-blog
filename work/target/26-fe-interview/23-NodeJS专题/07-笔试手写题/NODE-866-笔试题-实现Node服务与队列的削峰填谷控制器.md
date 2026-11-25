---
title: [NODE-866] 笔试题——实现削峰填谷控制器（队列积压自适应消费）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-866：手写削峰控制器

**需求与边界**：
- 需求：削峰填谷（SCN-NODE-856/693）——① 积压监控（队列深度——SCN-NODE-693）；② 自适应消费并发（积压大 → 扩消费 worker——SCN-NODE-834 弹性）；③ 下游保护（消费限流——SCN-NODE-736）；④ 消费优先级（SCN-NODE-693 保底）。
- 边界：① 扩消费的下游校验（SCN-NODE-699）；② 积压告警（SCN-NODE-647 ETA——预估清空时间）；③ 优先级饥饿防御（SCN-NODE-693）。

**答**：
```javascript
class BackpressureController {
  async tick() {
    const depth = await queue.depth();
    const eta = depth / consumerThroughput();          // ETA（SCN-NODE-647）
    if (eta > 2 * 3600_000) alert({ type: 'QUEUE_BACKLOG', depth, eta });   // 告警
    const desiredWorkers = Math.min(Math.ceil(depth / 1000), downstreamSafe());   // 自适应（SCN-NODE-834）
    if (desiredWorkers > workers) scaleWorkers(desiredWorkers);   // 扩消费（SCN-NODE-699 校验）
    else if (depth < 100 && workers > baseWorkers) scaleWorkers(baseWorkers);   // 缩（SCN-OPS-237 冷却）
  }
}
```

**评分点**:
- 积压监控 + ETA（SCN-NODE-647）。
- 自适应消费并发（SCN-NODE-834 弹性）。
- 下游保护限流 + 全局校验（SCN-NODE-736/699）。
- 优先级保底（SCN-NODE-693）。
