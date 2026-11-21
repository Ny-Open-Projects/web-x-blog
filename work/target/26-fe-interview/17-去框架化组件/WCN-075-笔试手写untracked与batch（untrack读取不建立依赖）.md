---
title: [WCN-075] 笔试：手写 untrack 与 batch（逃逸追踪 + 显式事务合并）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-075：笔试：手写 untrack 与 batch

**题目**：实现两个调度原语：① `untrack(fn)` — fn 内读 signal 不建立依赖；② `batch(fn)` — fn 内所有 signal 写入合并到一次微任务刷新，fn 结束前 effect 不执行；③ 支持嵌套 batch（内层不提前 flush）；④ batch 内 effect 若被显式调用（直接 run）应读到一致快照；⑤ 用测试口径验证：batch 内三次写 → effect 一次；untrack 内读取 → 依赖数不增。

**答**：

```javascript
let activeSub = null;
let batchDepth = 0;
const pendingSubs = new Set();

export function untrack(fn) {
  const prev = activeSub;
  activeSub = null;                 // 关闭追踪：getter 看到 null 就不登记
  try { return fn(); } finally { activeSub = prev; }
}

export function batch(fn) {
  batchDepth++;
  try { return fn(); }
  finally {
    batchDepth--;
    if (batchDepth === 0) {
      const list = [...pendingSubs]; pendingSubs.clear();
      list.forEach((s) => s.run()); // 嵌套结束时由最外层统一 flush
    }
  }
}

// 与 createSignal 的集成（改造 write）：
// function write(nv) { if (Object.is(nv, v)) return; v = nv;
//   if (batchDepth > 0) subs.forEach((s) => pendingSubs.add(s));
//   else subs.forEach((s) => scheduleRun(s)); }
//
// 注意一致快照：batch 内直接 s.run() 时 fn 读到的是已写入的最新值——
// 若需要"事务快照"，用 pendingSubs 里 effect 的 deferral 语义即可（默认推迟到 batch 末尾）。

// 测试口径：
// batch(() => { setA(1); setB(2); batch(() => setC(3)); });
// → effect([a,b,c]) 只执行 1 次，且读到 {1,2,3}
// const [x, setX] = createSignal(1);
// effect(() => { const n = untrack(() => Math.random()); return x(); });
// → untrack 内读取不影响依赖
```

**评分点**：
- untrack 通过置空 activeSub 实现，finally 恢复（重入安全）。
- batchDepth 计数支持嵌套，最外层才 flush（早 flush 是常见 bug）。
- pendingSubs 用 Set 去重；flush 顺序应尽量拓扑（注册序简化可接受，需说明）。
- 与 write 集成的条件分支写对（batch 内进 pendingSubs，否则走微任务调度）。
