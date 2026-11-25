---
title: [HW-062] 手写 deferred / Promise.withResolvers——在外部作用域控制 Promise 结算
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-062：手写 deferred / Promise.withResolvers——在外部作用域控制 Promise 结算

**答**：deferred 把 Promise 的 resolve/reject "提"到构造器外面，是任务队列、事件等待、回调转 Promise 的基础设施。ES2024 已有原生 `Promise.withResolvers()`，手写即兼容版。边界：resolve/reject 可多次调用但只有第一次生效（天然）；别把 deferred 当"可取消"用（那是 HW-061）。

```javascript
function deferred() {
  let resolve, reject;
  const promise = new Promise((res, rej) => { resolve = res; reject = rej; });
  return { promise, resolve, reject };
}
if (!Promise.withResolvers) {
  Promise.withResolvers = deferred;    // 补齐原生（ES2024 之前的环境）
}

// 典型场景 1：回调 API 转 Promise，且需要在回调里结算
function waitForMessage(ws) {
  const d = deferred();
  ws.onmessage = (e) => d.resolve(JSON.parse(e.data));
  ws.onerror = () => d.reject(new Error('ws error'));
  return d.promise;
}
// 典型场景 2：等待外部信号再放行（门闩）
const gate = deferred();
async function worker(i) { await gate.promise; return doJob(i); }
const jobs = [1, 2, 3].map(worker);
gate.resolve();        // 一声令下全部放行
```

**评分点**：
- 结构正确：resolve/reject 从 executor 作用域提升出来。
- 能说出两个以上真实用途（回调转 Promise、门闩/信号、任务协调）。
- 知道 ES2024 原生 withResolvers 并给出 polyfill 写法。
- 多次 resolve 只第一次生效的语义理解。

## 变体与延伸（补充）

**变体与延伸**：

1. resolve 之后再调 reject 会怎样 → 状态已 settled，后续调用一律静默忽略且不抛错，这正是「只第一次生效」的语义，重复调用也不改变已定状态
2. 如何避免 Promise 永不结算造成泄漏 → 用 Promise.race 加超时兜底，或在 finally 里清理挂起的 waiter，否则等待方永久占住闭包引用，超时后要主动 reject 释放
3. 与直接 new Promise 的实质差别 → 解构出 resolve/reject 后可传出作用域，调用方不必交出整个 executor，回调转 Promise 与任务协调共用一套 API，这是它存在的实际价值
