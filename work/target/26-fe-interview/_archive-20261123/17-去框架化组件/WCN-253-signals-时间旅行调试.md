---
title: [WCN-253] Signals 的「时间旅行」调试如何实现（快照/回放）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-253：Signals 的「时间旅行」调试如何实现（快照/回放）？
**答**：
- 记录每次写操作（signal, oldValue, newValue, batchId）成日志。
- 回放：重置全部信号到初始值 → 重放写序列 → 重建任意时刻状态。
- 快照优化：定期做全量快照，回放只重放快照后的增量。
- 挑战：副作用（effect 的 DOM 写/请求）不可逆——时间旅行只对「信号状态」保真，副作用侧标注。

```javascript
const log: Write[] = [];
function set(sig, v) { log.push({ sig, from: sig.value, to: v }); sig.value = v; }
function rewindTo(batchId) {
  replayFromSnapshot(batchId);          // 快照 + 增量重放
}
r
```
