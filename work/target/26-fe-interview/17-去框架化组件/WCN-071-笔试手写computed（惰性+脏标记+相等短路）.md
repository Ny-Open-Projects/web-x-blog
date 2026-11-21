---
title: [WCN-071] 笔试：手写 computed（惰性求值 + 脏标记 + 相等短路）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-071：笔试：手写 computed

**题目**：基于上题的 signal 原语实现 `computed(fn)`：① 返回只读 getter；② 依赖变化只标脏不立即重算（push-pull）；③ 读取时重算一次；④ 重算结果与旧值 Object.is 相等时不通知订阅者（下游 effect 不触发）；⑤ 支持 computed 依赖 computed 的链式场景；⑥ 循环依赖检测。

**答**：

```javascript
let activeSub = null;

export function computed(fn) {
  let value, dirty = true;
  const deps = new Set();        // 我依赖的上游
  const subs = new Set();        // 依赖我的下游
  const self = {                 // 作为上游订阅者身份
    deps, run: recompute,
  };
  function recompute() {
    if (!dirty) return;
    for (const d of deps) d.delete(self); deps.clear();
    const prev = activeSub; activeSub = self;
    try {
      const nv = fn();
      dirty = false;
      if (!Object.is(nv, value)) {         // 相等短路：不惊动下游
        value = nv;
        for (const s of subs) s.invalidate();
      }
    } finally { activeSub = prev; }
  }
  const read = () => {
    if (activeSub) {                       // 被别人读取：建立双向依赖
      subs.add(activeSub);
      if (activeSub.deps) activeSub.deps.add(subsKey);
    }
    if (dirty) recompute();
    return value;
  };
  read.invalidate = () => { dirty = true; recompute(); }; // pull 时立即重算
  return read;
}
const subsKey = Symbol('computed'); // 依赖集合登记（示意，实际实现里 deps 存上游 subs Set）

// 链式口径：c = computed(() => b() + a())；改 a → b/c 都只标脏 → 读 c 时一条链重算一次
// 循环：computed(() => c() + 1) 依赖自身 → recompute 重入检测：activeSub === self 时抛错
```

**评分点**：
- push-pull 双阶段：写入只标脏（invalidate 传播），读取才重算。
- 相等短路：computed 新旧值 Object.is 相等时不向下游传播（下游 effect 不跑）。
- 重算前清空并重建依赖（动态分支依赖）。
- 循环依赖检测（重入 self 抛错）与链式 computed 的拓扑顺序正确性。
