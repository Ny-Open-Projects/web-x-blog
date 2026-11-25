---
title: [WCN-548] 笔试：实现 effect 触发原因追踪器（记录触发链：哪个写 → 哪个 computed → 哪个 effect）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-548：笔试：实现 effect 触发原因追踪器（记录触发链：哪个写 → 哪个 computed → 哪个 effect）。

**答**：
- 结论：包装 signal 的 set 与 computed 的标脏、effect 的执行，串成一条因果链并记录。
- 写时生成 traceId，标脏与执行携带同一 traceId，最后按 traceId 聚合出完整链。
- 环形缓冲限制内存，支持按 effect 名查询最近若干条链。
- 追问：异步 flush 跨微任务如何保持 traceId？（答：用 AsyncLocalStorage 或显式透传上下文）

```javascript
let traceSeq = 0; const TRACES = new Map();
function beginTrace(src) { const id = ++traceSeq; TRACES.set(id, { src, at: performance.now(), steps: [] }); return id; }
function step(id, kind, name) { TRACES.get(id)?.steps.push({ kind, name, at: performance.now() }); }
function wrapSet(sig, name) {
  const orig = sig.set;
  sig.set = v => { const id = beginTrace('write'); step(id, 'set', name); orig(v); step(id, 'done', name); return id; };
}
function chain(id) { return TRACES.get(id)?.steps || []; }
function prune(n = 100) { while (TRACES.size > n) TRACES.delete(TRACES.keys().next().value); }
```

**评分点**：
- traceId 串联因果链
- 写/标脏/执行全记录
- 环形缓冲限内存
- 按 effect 查询链路
