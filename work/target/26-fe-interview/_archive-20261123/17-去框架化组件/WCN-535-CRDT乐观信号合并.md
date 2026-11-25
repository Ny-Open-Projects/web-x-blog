---
title: [WCN-535] Signals 在实时协同（CRDT / Yjs）场景：本地乐观信号与远端操作如何合并？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-535：Signals 在实时协同（CRDT / Yjs）场景：本地乐观信号与远端操作如何合并？

**答**：
- 结论：本地写先更新乐观 signal（即时反馈），远端操作通过 CRDT 合并后校正；冲突由 CRDT 的确定性规则解决。
- 用 Lamport 时钟 / 版本号标记每次本地写，远端合并时按因果序应用。
- 乐观态与确认态分离：UI 读乐观值，未确认操作带「pending」标记，ack 后清除。
- 追问：离线期间的操作如何恢复？（答：操作日志持久化，重连后按序补发，CRDT 天然幂等）

```javascript
function makeOptimistic(initial, applyRemote) {
  const local = signal(initial), pending = signal(0);
  const log = [];
  function commit(op) { log.push(op); pending.set(pending.get() + 1); return applyLocal(op); }
  function remote(op) {
    const next = applyRemote(local.get(), op); // CRDT merge，确定性
    local.set(next);
    // 若远端包含本地操作，移除对应 pending
  }
  function ack(opId) { pending.set(Math.max(0, pending.get() - 1)); }
  return { local, pending, commit, remote, ack, log };
}
```
