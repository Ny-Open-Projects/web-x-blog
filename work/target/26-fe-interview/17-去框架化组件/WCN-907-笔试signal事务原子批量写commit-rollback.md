---
title: [WCN-907] 手写 signal 的「事务 / 原子批量写」：一批写要么全可见要么全不可见
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-907：手写 signal 的「事务 / 原子批量写」：一批写要么全可见要么全不可见

**题目**：实现 `createTransaction(signals)`，返回 `{ read(name), write(name, val), commit(), rollback() }`。要求：① 事务期间所有 write 先写入暂存区，其他订阅者读到的仍是旧值（全不可见）；② 事务内部 read 能看到自己的未提交写（读己可见）；③ commit 时把所有暂存写一次性原子提交，并只触发一次订阅通知；④ rollback 丢弃暂存写，状态完全不变；⑤ 提供 `run(fn)`  sugar：fn 抛错自动 rollback，成功自动 commit。请自足实现并给出「转账」可运行示例（转出与转入必须原子）。

**答**：

```javascript
function createTransaction(signals) {
  const state = { ...signals };            // 真实状态
  let staged = null, subs = [];
  function read(name) {
    return staged && name in staged ? staged[name] : state[name];
  }
  function write(name, val) {
    if (!staged) staged = {};
    staged[name] = val;                     // 先暂存，不对外可见
  }
  function commit() {
    if (!staged) return;
    Object.assign(state, staged);
    staged = null;
    subs.forEach(f => f());                 // 一次通知
  }
  function rollback() { staged = null; }
  function run(fn) {
    try { fn(); commit(); }
    catch (e) { rollback(); throw e; }
  }
  return { read, write, commit, rollback, run,
           subscribe(f) { subs.push(f); },
           snapshot: () => ({ ...state }) };
}
const acc = createTransaction({ alice: 100, bob: 100 });
acc.subscribe(() => console.log('外部看到:', acc.snapshot()));
acc.run(() => {
  acc.write('alice', acc.read('alice') - 30);
  acc.write('bob', acc.read('bob') + 30);
  console.log('事务内读己可见:', acc.read('alice'), acc.read('bob')); // 70,130
}); // 外部只打印一次: { alice:70, bob:130 }
try { acc.run(() => { acc.write('alice', 0); throw new Error('fail'); }); } catch {}
console.log(acc.snapshot()); // alice 仍 70，回滚成功
```

**评分点**：
- 写暂存与读己可见：暂存区实现写不对外可见、事务内 read 能读到未提交值。
- 原子提交与单次通知：commit 一次性 Object.assign，订阅者只被通知一次。
- rollback 完整丢弃暂存写，状态不被污染（转账失败示例正确）。
- run sugar 的异常安全：fn 抛错自动 rollback 且重新抛出，成功自动 commit。
- 示例覆盖正常提交与失败回滚两条路径，可运行。
