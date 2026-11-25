---
title: [WCN-849] 笔试：手写 CRDT + Signal 的协同计数器（G-Counter 收敛）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-849：笔试：手写 CRDT + Signal 的协同计数器（G-Counter 收敛）

**题目**：实现一个「增长型计数器 G-Counter」CRDT，并用 signal 暴露当前值。G-Counter 原理：每个副本维护 `{ replicaId: count }`，本地 increment 只增自己的计数；merge 两个状态时对每个 replicaId 取最大值（max）；当前值 = 各 replica 计数之和。要求：① `createGCounter(id, signalFactory)` 返回 `{ increment(n=1), merge(otherState), getState(), value(signal) }`；② increment 后 value signal 自动更新；③ merge 用逐键 max 保证幂等、交换律、结合律（并发最终收敛）；④ 提供 `compare(a,b)` 判断两状态因果序。边界：n 必须为非负整数；merge 外部状态时忽略非法值；信号用 Object.is 去重避免无效通知。

**答**：

```javascript
function createGCounter(id, signalFactory) {
  let state = { [id]: 0 };
  const valueSig = signalFactory(0);
  function emit() { valueSig.set(Object.values(state).reduce((a, b) => a + b, 0)); }
  return {
    increment(n = 1) {
      if (!Number.isInteger(n) || n < 0) return;           // 边界：非负整数
      state = { ...state, [id]: (state[id] || 0) + n };
      emit();
    },
    merge(other = {}) {
      const next = { ...state };
      for (const [k, v] of Object.entries(other)) {
        if (!Number.isFinite(v) || v < 0) continue;         // 忽略非法值
        next[k] = Math.max(next[k] || 0, v);                // 逐键 max
      }
      state = next; emit();
    },
    getState: () => ({ ...state }),
    value: valueSig,
  };
}
// 判断因果序：a <= b 当且仅当所有键 a[k] <= b[k]
function compare(a, b) {
  const keys = new Set([...Object.keys(a), ...Object.keys(b)]);
  const le = [...keys].every(k => (a[k] || 0) <= (b[k] || 0));
  const ge = [...keys].every(k => (a[k] || 0) >= (b[k] || 0));
  return le && ge ? 'equal' : le ? 'before' : ge ? 'after' : 'concurrent';
}
const sig = (init) => { let v = init; const s = { get: () => v, set(n) { if (Object.is(v,n)) return; v = n; } }; return s; };
const A = createGCounter('A', sig), B = createGCounter('B', sig);
A.increment(3); B.increment(2);
A.merge(B.getState()); B.merge(A.getState());
console.log(A.value.get(), B.value.get()); // 5 5，收敛一致（幂等/交换/结合）
console.log(compare(A.getState(), B.getState())); // equal
```

**评分点**：
- merge 用逐键 max，满足 CRDT 三律（幂等、交换、结合），保证最终收敛（核心）。
- increment 只改本地副本、value 由求和派生，符合 G-Counter 定义（正确性）。
- 边界处理：非负整数校验、merge 忽略非法值、Object.is 去重（健壮性/性能）。
- compare 正确判定因果/并发序，支撑「是否需要合并」的判断（深度）。
