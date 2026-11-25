---
title: [MFW-870] 怎么做每路由成本账本：DB ms、出站 API 次数、边缘 GB-s 的归集
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-870：怎么做每路由成本账本：DB ms、出站 API 次数、边缘 GB-s 的归集

**答**：
- 结论：把一次请求的消耗按路由维度归集（DB 耗时/查询数、出站次数、边缘执行时长与内存），形成可排序账本，找出高成本低价值路由。
- 落地：AsyncLocalStorage 贯穿请求采集 span，路由名从匹配结果取，成本按权重折算（DB ms × 单价）；聚合到 dashboard。
- 追问钩子：采样会不会失真？——成本指标应全采（量可控），只 trace 抽样。

```javascript
const als = new AsyncLocalStorage();
function startRequest(route) {
  const ledger = { route, dbMs: 0, dbCalls: 0, outCalls: 0, edgeMs: 0 };
  return als.run(ledger, async () => {
    const t = Date.now();
    try { return await handle(); }
    finally { ledger.edgeMs = Date.now() - t; flush(ledger); }
  });
}
function trackDb(fn) {
  return async (...a) => {
    const l = als.getStore(); l.dbCalls++;
    const t = Date.now();
    try { return await fn(...a); }
    finally { l.dbMs += Date.now() - t; }
  };
}
// flush → 时序库；dashboard 按 (dbMs*单价 + outCalls*单价) 排序找成本热点
```
