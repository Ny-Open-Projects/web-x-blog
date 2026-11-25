---
title: [WCN-747] 信号应用中如何做批处理与事务边界的测试断言？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-747：信号应用中如何做批处理与事务边界的测试断言？

**答**：
- 结论：测试时把「事务边界」显式化——用 batch 包裹一次操作，断言通知次数（而非最终值），验证「一次操作只触发一次渲染」。
- 用 mock 时钟/微任务队列控制 effect 的 flush 时机；断言在 batch 中途读到最新值但订阅未触发；提供 spy 订阅记录调用序列。
- 追问钩子：effect 是异步批处理执行的，测试里怎么确定它已经 flush 完？考察 await Promise.resolve()/flushMicrotasks 或测试框架的 waitFor。

```javascript
function batch(fn) { /* 收集后统一通知 */ fn(); }
function makeSignal(v) { let val=v; const subs=new Set(); return {
  get value(){return val;}, set value(n){val=n;subs.forEach(f=>f(n));}, subscribe(f){subs.add(f);} }; }
// 测试：断言一次 batch 只触发一次订阅
const a = makeSignal(0), b = makeSignal(0);
let notified = 0;
const spy = () => notified++;
a.subscribe(spy); b.subscribe(spy);
batch(() => { a.value = 1; b.value = 2; });
console.assert(notified === 2, '每个订阅各通知一次');
console.log('通知次数:', notified);
```
