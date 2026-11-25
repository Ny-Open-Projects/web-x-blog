---
title: [WCN-410] 笔试：实现信号的时间旅行（记录/回放）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-410：笔试：实现信号的时间旅行（记录/回放）。
**题目**：包装信号写：记录 `{sigId, from, to, batchId}` 日志。`snapshot()` 全量快照；`restore(snap)` 重置全部信号。

```javascript
const log = [];
function tracedSet(sig, nv) {
  log.push({ id: sig.id, from: sig._v, to: nv });
  sig.set(nv);
}
function snapshot(registry) {
  return new Map(registry.map(s => [s.id, s._v]));
}
function restore(registry, snap) {
  for (const s of registry) if (snap.has(s.id)) s.set(snap.get(s.id));  // 触发重放
}

```

**评分点**：
- 写拦截（proxy 或库内 set 包装）记录日志。
- 快照：全部信号当前值（id → value）。
- restore：逆序回放或直接 set 快照值（简单版）。
- 副作用标注：日志里 effect 执行不可逆——只对信号状态保真（说明局限）。
