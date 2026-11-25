---
title: [WCN-731] 如何为 Signals 应用实现时间旅行调试与状态快照？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-731：如何为 Signals 应用实现时间旅行调试与状态快照？

**答**：
- 结论：每次 signal 写入记录一条带时间戳/调用栈的「变更日志」，维护从初始态到当前态的快照链；调试器可回放任意时间点并对比差异。
- 为控制内存，采用「增量快照 + 间隔全量快照」；生产环境关闭或采样；提供 jumpTo(index) 临时应用历史值而不污染真实状态。
- 追问钩子：时间旅行时 effect 会不会重复执行产生副作用（如重复发请求）？考察「回放只恢复状态、不触发副作用」的设计。

```javascript
const log = [], snapshots = [];
function record(key, value, stack) {
  log.push({ t: Date.now(), key, value, stack });
  if (log.length % 100 === 0) snapshots.push({ i: log.length, state: clone(current) });
}
function jumpTo(i) {
  const target = nearestSnapshot(i);        // 找最近全量快照
  let state = { ...target.state };
  for (let k = target.i; k < i; k++) {
    const e = log[k]; state[e.key] = e.value; // 仅恢复状态，不触发 effect
  }
  return state;
}
console.log('时间旅行 = 全量快照 + 增量日志回放');
```
