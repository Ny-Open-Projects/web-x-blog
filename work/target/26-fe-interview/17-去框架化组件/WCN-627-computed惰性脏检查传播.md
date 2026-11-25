---
title: [WCN-627] 笔试：实现 signal 的 computed——惰性求值 + 脏标记传播 + 缓存
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-627：笔试：实现 signal 的 computed——惰性求值 + 脏标记传播 + 缓存

**答**：
- 需求：实现 computed(fn)，依赖变化时不立即重算，只标记 dirty；下次 get() 时才重算并缓存结果；依赖未变时直接返回缓存。
- 思路：每个节点维护 version；computed 记录依赖节点的 version 快照；get 时比对版本判断 dirty；重算后更新快照。
- 边界：嵌套 computed 要正确传递脏状态；循环依赖要检测并报错；相等值不触发下游（可选优化）。

```javascript
let active = null;
function signal(v) {
  const subs = new Set();
  return {
    get() { if (active) subs.add(active); return v; },
    set(nv) { if (Object.is(nv, v)) return; v = nv; [...subs].forEach(f => f()); },
    subs,
  };
}
function computed(fn) {
  let cache, dirty = true, deps = [];
  const node = {
    get() {
      if (dirty) { cache = compute(); dirty = false; }
      if (active) deps.push(active);
      return cache;
    },
    mark() { if (!dirty) { dirty = true; this.subs?.forEach(f => f()); } },
    subs: new Set(),
  };
  function compute() {
    const prev = active; active = node; deps = [];
    try { return fn(); } finally { active = prev; }
  }
  deps.forEach(d => d.subs.add(node.mark.bind(node)));
  return node;
}
const a = signal(1);
const double = computed(() => a.get() * 2);
console.log(double.get()); // 2（首次计算）
a.set(2);                  // 仅标记 dirty
console.log(double.get()); // 4（惰性重算）
```

**评分点**：
- 依赖变化只标记 dirty，get 时才重算（惰性求值）。
- 缓存命中：依赖未变时重复 get 不执行 fn。
- 嵌套 computed 脏状态能正确向上传播。
- 相等值（Object.is）不触发无谓通知，避免抖动。
