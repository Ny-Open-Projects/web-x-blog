---
title: [940] 笔试手写：实现带条件跳转与最大轮次的状态机工作流
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 状态机]
type: 笔试题
---

## 940：笔试手写：实现带条件跳转与最大轮次的状态机工作流

**需求**：实现 runMachine(def, ctx)。def = { states: { [name]: { on: (ctx) => nextName | null, max: 轮次上限 } }, init, done }。on 返回 null 表示进入终态。防死循环：任意 state 连续执行超过其 max 抛错（携带 state 名与轮次）。

```js
async function runMachine(def, ctx) {
  let cur = def.init, total = 0;
  const counters = {};
  while (cur !== def.done) {
    const st = def.states[cur];
    if (!st) throw new Error('unknown state: ' + cur);
    counters[cur] = (counters[cur] || 0) + 1;
    if (counters[cur] > (st.max || Infinity)) {
      throw new Error('loop at ' + cur + ' x' + counters[cur]);
    }
    if (++total > 1000) throw new Error('global runaway');  // 全局保险丝
    cur = await st.on(ctx) ?? def.done;                      // null -> 终态
  }
  return ctx;
}
const def = {
  init: 'plan', done: 'end',
  states: {
    plan:  { max: 3, on: c => (c.plan ? 'execute' : 'plan') },
    execute: { max: 5, on: c => (c.testsPass ? 'review' : 'execute') },
    review: { max: 2, on: c => (c.approved ? null : 'execute') }, // 驳回回执行
  },
};
```

**评分点**：
- 每状态轮次计数 + 上限抛错（错误信息带 state 名，可定位）
- 全局保险丝（total 上限）防止「每个 state 都没超限但组合成超长循环」
- on 返回 null 的终态语义处理正确
- 能讨论真实用途：Agent 工作流的显式状态机比自由对话循环可控，驳回回环（review -> execute）是典型模式

