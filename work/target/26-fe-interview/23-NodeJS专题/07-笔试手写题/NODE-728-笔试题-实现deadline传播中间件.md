---
title: [NODE-728] 笔试题——实现 deadline 传播中间件（剩余预算分配）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-728：手写 deadline 传播

**需求与边界**：
- 需求：入口 deadline（SCN-NODE-642）——① 入口中间件生成 deadline（header 传入或默认）；② ALS 存储剩余预算；③ 下游调用自动带 deadline（header 传播——剩余量）；④ 剩余不足快速失败（预算 <100ms 不发起下游——必超时）。
- 边界：① 跨 MQ 的 deadline（消息头带绝对时间戳——消费时重算剩余）；② 绝对时间戳 vs 相对（跨服务时钟漂移——容忍 ±1s）；③ deadline 的监控（超时率按级统计——SCN-NODE-642 三级）。

**答**：
```javascript
function deadlineMiddleware(total = 2000) {
  return (req, res, next) => {
    const abs = req.headers['x-deadline'] ?? Date.now() + total;   // 绝对时间戳（跨服务）
    als.run({ deadline: +abs, start: Date.now() }, next);
  };
}
function remaining() { return als.getStore().deadline - Date.now(); }
async function callDownstream(fn, { minBudget = 100 } = {}) {
  const left = remaining();
  if (left < minBudget) throw new DeadlineExhausted(left);   // 预算不足快速失败（必超时不白干）
  return fn({ signal: AbortSignal.timeout(left), headers: { 'x-deadline': als.getStore().deadline } });
}
// MQ 消费重算（绝对时间戳——SCN-NODE-642 预算制）
consumer.on('message', (m) => { const left = m.headers.deadline - Date.now(); ... });
```

**评分点**:
- 绝对时间戳 deadline（跨服务时钟漂移容忍——SCN-NODE-642）。
- ALS 上下文 + 剩余预算自动分配。
- 预算不足快速失败（不发起必超时调用——资源浪费防御）。
- MQ 消费重算剩余（异步链路的 deadline 贯穿）。
