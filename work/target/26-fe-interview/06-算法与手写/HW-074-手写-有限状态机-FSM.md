---
title: [HW-074] 手写有限状态机（FSM）——声明式转移表、非法转移报错、进入/离开钩子
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-074：手写有限状态机（FSM）——声明式转移表、非法转移报错、进入/离开钩子
**答**：FSM 三要素：states、transitions（{from: {event: to}}）、当前态。要点：非法 event 在当前态下要么报错要么忽略（可配置）；entry/exit 钩子在转移时按序触发（exit 旧 → transition → entry 新）；支持带 payload 的事件与转移条件（guard）。

```javascript
class FSM {
  constructor({ initial, states, transitions, onError = (e) => { throw e; } }) {
    this.state = initial; this.def = transitions; this.states = states; this.onError = onError;
  }
  can(event) { return !!this.def[this.state]?.[event]; }
  async dispatch(event, payload) {
    const t = this.def[this.state]?.[event];
    if (!t) return this.onError(new Error(`非法转移: ${this.state} --${event}-->`));
    const target = typeof t === 'string' ? t : t.to;
    const guard = typeof t === 'object' ? t.guard : null;
    if (guard && !(await guard(payload, this.state))) return false;      // 条件不满足保持原态
    const from = this.state;
    await this.states[from]?.exit?.(payload);                             // 离开旧态
    this.state = target;
    await this.states[target]?.enter?.(payload, from);                    // 进入新态
    return true;
  }
}
// 用法：支付单状态机 idle -> pending -> paid/refunded
const payFSM = new FSM({
  initial: 'idle',
  states: {
    idle:    {},
    pending: { enter: (p) => startPolling(p.orderId), exit: () => stopPolling() },
    paid:    { enter: () => notifySuccess() },
    refunded:{ enter: () => notifyRefund() },
  },
  transitions: {
    idle:    { pay: 'pending', cancel: { to: 'idle', guard: () => false } },
    pending: { confirm: { to: 'paid', guard: (p) => p.status === 'SUCCESS' },
               fail: 'idle' },
    paid:    { refund: 'refunded' },
  },
});
await payFSM.dispatch('pay', { orderId: 'A1' });   // idle -> pending（进入钩子开轮询）
await payFSM.dispatch('confirm', { status: 'SUCCESS' }); // pending -> paid（轮询被 exit 停止）
payFSM.dispatch('refund');
```

**评分点**：
- 转移表数据驱动（不是 if-else 硬编码），字符串与对象两种目标写法。
- exit → entry 钩子顺序正确（先离开后进入），异步钩子 await。
- 非法转移走 onError 可配置（不静默）。
- guard 条件转移失败保持原态（不是抛错）。
