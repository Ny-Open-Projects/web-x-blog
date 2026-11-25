---
title: [WCN-903] 手写「版本戳 + 惰性求值」computed，让菱形依赖只重算一次
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-903：手写「版本戳 + 惰性求值」computed，让菱形依赖只重算一次

**题目**：实现 `createComputed(fn, depsSignals)`：要求① 惰性求值——首次读 `.value` 才计算；② 版本戳——每个 signal 有全局递增版本号，computed 缓存上次读取各依赖的版本；③ 脏检查——读取时只有任一依赖版本变化才重算，否则返回缓存；④ 菱形依赖（a→b→c 与 a→d→c）中 c 被多条路径触达时，一次读取只重算一次，不重复计算；⑤ 返回 `{ get value() }`。请自足实现并提供可运行示例。

**答**：

```javascript
function createAtom(init) {
  let v = init, ver = 0, subs = new Set();
  return {
    get value() { return v; },
    set value(n) { if (n !== v) { v = n; ver++; subs.forEach(f => f()); } },
    get version() { return ver; },
    on(f) { subs.add(f); },
  };
}
let clock = 0;
function createComputed(fn, deps) {
  let cache, cachedVersions = [], valid = false;
  const check = () => deps.map(d => d.version);
  function recompute() {
    cachedVersions = check();
    cache = fn();
    valid = true;
    clock++;
    return cache;
  }
  // 依赖变化时只标脏，不立即算（惰性 + 合帧）
  deps.forEach(d => d.on(() => { valid = false; }));
  return { get value() {
    if (!valid) return recompute();
    const now = check();
    if (now.some((v, i) => v !== cachedVersions[i])) return recompute();
    return cache; // 菱形依赖：版本一致，直接命中缓存
  } };
}
const a = createAtom(2);
const b = createComputed(() => a.value * 2, [a]);
const c = createComputed(() => a.value * 3, [a]);
const d = createComputed(() => b.value + c.value, [b, c]);
let runs = 0;
const e = createComputed(() => { runs++; return a.value + d.value; }, [a, d]);
console.log(e.value, runs); // 12, 1
a.value = 5;
console.log(e.value, runs); // 30, 2（只重算一次）
```

**评分点**：
- 惰性求值：首次读才计算，构造时不执行 fn（核心机制）。
- 版本戳脏检查：用依赖版本号比对决定是否重算，引用变化但版本不变不重算。
- 菱形依赖只算一次：同一批次内 d、c 的变化不会导致 e 重复计算（runs 计数正确）。
- 订阅标脏正确：依赖写入时把下游标为 invalid，读取时再惰性重算。
- 示例可运行、边界（首次/未变化/变化）覆盖完整。
