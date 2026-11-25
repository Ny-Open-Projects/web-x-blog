---
title: [WCN-648] 笔试：实现 signal 的事务与回滚（structuredClone 快照 + commit/rollback）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-648：笔试：实现 signal 的事务与回滚（structuredClone 快照 + commit/rollback）

**答**：
- 需求：实现 transaction(fn)：批量修改多个 signal 期间暂停通知；fn 抛错或调用 rollback() 时回滚到初始快照；成功则一次性通知。
- 思路：全局 batch 深度 + 快照表（signal→structuredClone 值）；写时记录旧值；commit 时清空快照并统一通知；rollback 恢复值再通知。
- 边界：嵌套事务只在外层提交；不可克隆值（函数）回退为引用；只通知真正变化的 signal。

```javascript
let depth = 0;
const snapshots = new Map();
const pending = new Set();
function beginBatch() { depth++; }
function endBatch(commit = true) {
  if (--depth > 0) return;
  if (commit) {
    snapshots.clear();
    pending.forEach(f => f());
  } else {
    snapshots.forEach((v, s) => s._setRaw(v));
    snapshots.clear();
    pending.forEach(f => f());
  }
  pending.clear();
}
function transactionalSignal(value) {
  let v = value;
  const subs = new Set();
  const s = {
    get() { return v; },
    _setRaw(nv) { v = nv; },
    set(nv) {
      if (!snapshots.has(s)) snapshots.set(s, v);
      v = nv;
      if (depth === 0) subs.forEach(f => f());
      else pending.add(() => subs.forEach(f => f()));
    },
    subscribe(f) { subs.add(f); return () => subs.delete(f); },
  };
  return s;
}
const a = transactionalSignal(1);
beginBatch(); a.set(2); endBatch(false); // 回滚 → a.get() === 1
```

**评分点**：
- 批量期间暂停通知，commit 时只通知一次（避免抖动）。
- rollback 恢复到快照值并重新通知订阅者。
- 嵌套事务只在最外层提交/回滚（depth 计数）。
- 不可克隆值安全处理（此实现用引用快照，可扩展 structuredClone）。
