---
title: [AIC-694] 笔试：手写 AI 链路追踪器
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-694：笔试：手写 AI 链路追踪器

**答**：实现 `traceAIChain(events, opts)`。events: `{ traceId:string, stage:'request'|'gateway'|'model'|'response'|'accept'|'commit', ts:number, tokens?:number, error?:boolean }[]`；opts: `{ requiredStages?:string[], maxLatencyMs?:number }`（默认 required=['request','gateway','model','response'], maxLatency=30000）。规则：1) 按 traceId 分组；2) 每组按 ts 排序，计算 totalMs = last.ts − first.ts；3) 检查 requiredStages 是否齐全，缺失记 'incomplete-chain'；4) totalMs > maxLatencyMs → 'slow-chain'；5) 任 event.error → 'has-error'；6) 阶段顺序合法性：gateway 必须在 model 之前、model 在 response 之前，违反记 'out-of-order'；7) 返回 `Array<{ traceId, stages:string[], totalMs, tokens:number, flags:string[], healthy:boolean }>`。边界：events 空返回 []。

```javascript
function traceAIChain(events = [], opts = {}) {
  const { requiredStages = ['request', 'gateway', 'model', 'response'], maxLatencyMs = 30000 } = opts;
  const byTrace = new Map();
  for (const e of events) {
    if (!byTrace.has(e.traceId)) byTrace.set(e.traceId, []);
    byTrace.get(e.traceId).push(e);
  }
  const order = { request: 0, gateway: 1, model: 2, response: 3, accept: 4, commit: 5 };
  return [...byTrace.entries()].map(([traceId, arr]) => {
    arr.sort((a, b) => a.ts - b.ts);
    const stages = [...new Set(arr.map(e => e.stage))];
    const totalMs = arr.length ? arr[arr.length - 1].ts - arr[0].ts : 0;
    const tokens = arr.reduce((s, e) => s + (e.tokens || 0), 0);
    const flags = [];
    if (requiredStages.some(s => !stages.includes(s))) flags.push('incomplete-chain');
    if (totalMs > maxLatencyMs) flags.push('slow-chain');
    if (arr.some(e => e.error)) flags.push('has-error');
    // 顺序合法性：按 ts 排序后阶段序号应单调不减
    const idxs = arr.map(e => order[e.stage] ?? 99);
    if (idxs.some((v, i) => i > 0 && v < idxs[i - 1])) flags.push('out-of-order');
    return { traceId, stages, totalMs, tokens, flags, healthy: flags.length === 0 };
  });
}

// 自测
const base = [
  { traceId: 't1', stage: 'request', ts: 0 },
  { traceId: 't1', stage: 'gateway', ts: 100, tokens: 10 },
  { traceId: 't1', stage: 'model', ts: 200, tokens: 500 },
  { traceId: 't1', stage: 'response', ts: 300 },
  { traceId: 't2', stage: 'request', ts: 0 },
  { traceId: 't2', stage: 'model', ts: 50, error: true }, // 缺 gateway，乱序，有错
];
const r = traceAIChain(base);
console.log(r[0].healthy === true && r[0].tokens === 510);
console.log(r[1].flags.includes('incomplete-chain') && r[1].flags.includes('has-error'));
console.log(r[1].flags.includes('out-of-order'));
console.log(traceAIChain([]).length === 0);
```

**评分点**：
- 按 traceId 分组并按 ts 排序
- requiredStages 完整性、慢链路、错误三类 flag
- 阶段顺序合法性检测（序号单调不减）
- tokens 累加、healthy 综合
- 能说清「结果侧数据（采纳/存活/缺陷）最难采集但最有价值，请求侧只告诉你用了多少」属于加分
