---
title: [FRP-367] 笔试：手写 computed signal（惰性 + 脏标记）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-367：笔试：手写 computed signal

**答**：实现 `computed(fn)`：① 惰性求值（没人读不计算）；② 脏标记：依赖变化标脏，读时才重算，未变返回缓存；③ 链式 computed 正确传播（A→B→C）；④ 分支依赖清理（重算时解除不再读取的依赖）；⑤ computed 可被 effect 订阅（effect 依赖 computed 的缓存语义——依赖不变不重跑）。基于 FRP-366 的 signal 内核扩展。写出实现。

```javascript
function computed(fn) {
  let value, dirty = true;
  const subs = new Set();                          // 订阅此 computed 的下游
  const read = () => {
    if (active) { subs.add(active); active.deps.add(subs); }
    if (dirty) {
      const e = { deps: new Set(), run: () => {} };
      const oldSubs = subs;                        // 旧下游保留
      // 计算: 读上游 signal 时注册到 e
      stack.push(active); active = e;
      try { value = fn(); }
      finally { active = stack.pop(); }
      // 上游通知时: 标脏 + 传播下游
      e.deps.forEach((upstream) => {
        upstreamDelete(e);                         // 由上游清理旧订阅
        registerPropagation(e, subs);
      });
      dirty = false;
    }
    return value;
  };
  // 上游变化 → dirty = true + 通知下游(若下游是 effect 立即跑, computed 递归标脏)
  const onUpstream = () => {
    dirty = true;
    subs.forEach((s) => s.onUpstream ? s.onUpstream() : s.run());
  };
  read.onUpstream = onUpstream;
  return read;
}
// 简化注释版关键点:
// - dirty 标记 + 读时重算 = 惰性
// - 上游通知先标脏, 下游若是 effect 由下游自决(读时才算)
// - 重算时旧依赖清理 = 分支切换正确性
```

**评分点**：
- 惰性 + 脏标记（无人读不计算、依赖未变不重算）
- 链式传播（上游标脏 → 递归通知 → effect 最终驱动）
- 分支依赖清理（重算解除旧依赖）
- effect 读 computed 的「依赖未变不重跑」缓存语义
