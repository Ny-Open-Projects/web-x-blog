---
title: [WCN-730] 笔试：手写 signal 的 batch 事务（批量更新合并通知）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-730：笔试：手写 signal 的 batch 事务（批量更新合并通知）

**答**：
- 需求：实现 `batch(fn)`，在 fn 内对多个 signal 的写入只触发一次订阅通知（fn 结束后统一 flush）；嵌套 batch 只有最外层结束才 flush；写入期间读取到的是最新值。
- 要点：用全局 depth 计数 + 待通知集合（Set 去重）；depth>0 时收集 dirty 依赖，depth 归零时统一通知；边界：fn 抛错也要 flush 并复位 depth。

```javascript
let depth = 0;
const pending = new Set();
function notifyAll() { for (const sub of [...pending]) sub(); pending.clear(); }
function makeSignal(initial) {
  let value = initial;
  const subs = new Set();
  return {
    get value() { return value; },
    set value(v) {
      value = v;
      if (depth > 0) subs.forEach((s) => pending.add(s));
      else subs.forEach((s) => s());
    },
    subscribe(fn) { subs.add(fn); },
  };
}
function batch(fn) {
  depth++;
  try { fn(); }
  finally {
    depth--;
    if (depth === 0) notifyAll();             // 仅最外层 flush
  }
}
const a = makeSignal(1), b = makeSignal(2);
let runs = 0;
a.subscribe(() => runs++); b.subscribe(() => runs++);
batch(() => { a.value = 10; b.value = 20; });
console.log('通知次数:', runs);   // 2（每个订阅各一次，而非多次）
```

**评分点**：
- depth 计数支持嵌套 batch，仅最外层 flush。
- pending 用 Set 去重，同一订阅只通知一次。
- finally 保证抛错时也 flush 并复位 depth（健壮性）。
- 写入期间读到最新值，语义正确。
