---
title: [AGT-640] 手写 traceHeaders：traceparent 生成、跨请求复用、错误上报关联、隐私保护？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-640：手写 traceHeaders：traceparent 生成、跨请求复用、错误上报关联、隐私保护

**需求与边界**：
- 实现 traceHeaders(turn) 与 reportError(err)。
- 边界要求：① traceparent 格式合法（00-32hex-16hex-01）；② 同一 turn 内所有请求复用同一 traceId（spanId 各异）；③ 错误上报自动带当前 turn 上下文（无 turn 时标记 orphan）；④ userId 只传哈希不传明文。

**答**：
```javascript
const hex = (n) => [...crypto.getRandomValues(new Uint8Array(n))]
  .map(b => b.toString(16).padStart(2, '0')).join('');
function newTraceParent() {
  return { traceId: hex(16), spanId: hex(8) };   // 32/16 hex
}
function traceHeaders(turn) {
  if (!turn.trace) turn.trace = newTraceParent(); // turn 内复用
  const { traceId } = turn.trace;
  const spanId = hex(8);                          // 每请求新 span
  return {
    traceparent: `00-${traceId}-${spanId}-01`,
    'x-user-hash': sha256(turn.userId).slice(0, 16),  // 只传哈希
    'x-turn-id': turn.id,
  };
}
function reportError(err) {
  const turn = currentTurn();
  return api.report({ msg: String(err), stack: err?.stack,
    traceId: turn?.trace?.traceId ?? null,
    orphan: !turn, at: Date.now() });             // 无turn标orphan
}
```

**评分点**:
- traceparent 格式合法且 turn 内 traceId 复用、spanId 每请求独立。
- 错误上报自动关联当前 turn，无 turn 标 orphan（可反查）。
- 用户标识哈希化（隐私最小化）。

