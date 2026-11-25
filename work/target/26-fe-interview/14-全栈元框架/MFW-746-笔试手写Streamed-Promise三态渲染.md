---
title: [MFW-746] 笔试：手写 Streamed Promise 三态渲染
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-746：笔试：手写流式 Promise 三态

**答**：实现 `createStreamedValue(promise)`。返回 `{ state: 'pending'|'resolved'|'rejected', value?, error?, subscribe(cb) }`。规则：1) 初始 pending；2) promise resolve → state='resolved'，value 更新，通知 subscriber；3) promise reject → state='rejected'，error 更新；4) subscribe(cb)：注册回调（状态变化时调用 cb(state)——返回 unsubscribe）；5) 多次 subscribe 全通知（多消费者——每个 cb 收到状态变化）；6) promise 的值不可变（resolve 后 value 固定）。边界：promise 已 resolve（立即 resolved）；同步 resolve（微任务内 resolve——仍经历 pending）；多次 resolve（Promise 语义——只有第一次生效）。

```javascript
function createStreamedValue(promise) {
  let state = 'pending';
  let value, error;
  const subscribers = new Set();
  function update(newState, data) {
    state = newState;
    if (newState === 'resolved') value = data;
    if (newState === 'rejected') error = data;
    subscribers.forEach(cb => cb({ state, value, error }));
  }
  promise.then(
    (v) => update('resolved', v),
    (e) => update('rejected', e?.message ?? String(e)),
  );
  return {
    get state() { return state; },
    get value() { return value; },
    get error() { return error; },
    subscribe(cb) {
      subscribers.add(cb);
      // 立即通知当前状态（新订阅者）
      cb({ state, value, error });
      return () => subscribers.delete(cb);
    },
  };
}

// 自测
// resolve
let sv = createStreamedValue(Promise.resolve({ id: 1, name: 'test' }));
console.log(sv.state === 'pending');                     // 同步调用时 pending
await sleep(5);
console.log(sv.state === 'resolved' && sv.value.name === 'test');

// reject
sv = createStreamedValue(Promise.reject(new Error('fail')));
await sleep(5);
console.log(sv.state === 'rejected' && sv.error === 'fail');

// subscribe 多消费者
const events = [];
sv = createStreamedValue(Promise.resolve('v1'));
const unsub1 = sv.subscribe(s => events.push({ sub: 1, state: s.state }));
const unsub2 = sv.subscribe(s => events.push({ sub: 2, state: s.state }));
await sleep(5);
console.log(events.filter(e => e.sub === 1).map(e => e.state).join(','));
// pending,resolved（新订阅者先收到当前状态 + 变更通知）
console.log(events.filter(e => e.sub === 2).length >= 2);

// unsubscribe
unsub1();
sv = createStreamedValue(Promise.resolve('v2'));
await sleep(5);
// unsub1 不再收到通知（events 无新 sub:1 条目——上面 sv 是新实例）
// 同步 resolve（微任务）
sv = createStreamedValue(Promise.resolve('sync'));
console.log(sv.state === 'pending');                     // 同步代码仍在 pending
await sleep(0);                                          // 微任务
console.log(sv.state === 'resolved');
```

**评分点**：
- 三态状态机（pending/resolved/rejected）；subscribe 的立即通知（新订阅者收当前状态）+ 变更通知
- 多消费者（Set 全通知）；unsubscribe 清理
- 边界（同步 resolve 的微任务语义/reject 的 message 提取/不可变性）
- 能说清「流式 Promise 的三态 = SvelteKit 的 {#await} 块——pending/resolved/rejected 的声明式消费」属于加分
