---
title: [WCN-077] 笔试：手写一个有限状态机 Signal（FSM：状态转移约束 + 副作用钩子）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-077：笔试：手写一个有限状态机 Signal

**题目**：实现 `createFSM({ initial, states, transitions })`：① states 定义合法状态及进入/离开钩子（enter/exit）；② transitions 是 `{ from, event, to }` 列表；③ `send(event)` 只允许合法转移，非法转移 warn 并保持原状态；④ 当前状态是 signal，可被 effect/computed 追踪；⑤ exit/enter 钩子同步执行且在状态 signal 更新前后顺序正确（exit 旧 → 更新 → enter 新）；⑥ 事件队列：重入 send 在转移进行中时排队。

**答**：

```javascript
import { createSignal, batch, untrack } from './mini.js';

export function createFSM(def) {
  const [state, setState] = createSignal(def.initial);
  const ruleMap = new Map();
  for (const t of def.transitions) ruleMap.set(`${t.from}|${t.event}`, t.to);

  let busy = false;
  const q = [];

  function send(event, payload) {
    const cur = untrack(state);
    const to = ruleMap.get(`${cur}|${event}`);
    if (!to) { console.warn(`非法转移: ${cur} --${event}-->`); return false; }
    if (busy) { q.push([event, payload]); return true; }  // 重入排队
    busy = true;
    def.states?.[cur]?.exit?.(payload);
    setState(to);                                           // 更新 signal
    def.states?.[to]?.enter?.(payload);
    busy = false;
    while (q.length) { const [e, p] = q.shift(); send(e, p); } // 逐个消费队列
    return true;
  }

  return { state, send,
    matches(...names) { return computed ? undefined : names.includes(state()); } };
}
// 简化 matches：effect(() => { if (fsm.state() === 'loading') ... })

// 口径（订单状态机）：
// const fsm = createFSM({
//   initial: 'created',
//   transitions: [
//     { from: 'created', event: 'PAY', to: 'paid' },
//     { from: 'paid', event: 'SHIP', to: 'shipped' },
//     { from: 'paid', event: 'CANCEL', to: 'cancelled' },
//   ],
//   states: { paid: { enter: () => notifyFinance() } },
// });
// fsm.send('PAY'); fsm.send('SHIP');     // ok
// fsm.send('PAY');                        // 非法：cancelled 不能再支付
```

**评分点**：
- 转移表用 Map 索引 O(1) 查找；非法转移 warn 不抛（宽松降级）或可配置 strict。
- 钩子顺序：exit → setState（signal 更新）→ enter（订阅者可见顺序正确）。
- 重入排队（busy 标志 + 队列），转移原子性。
- 状态是 signal，可无缝接入响应式链。
