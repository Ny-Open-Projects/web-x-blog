---
title: [WCN-873] 笔试：手写编译平台的「插件钩子系统」（tapable 风格）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-873：笔试：手写编译平台的「插件钩子系统」（tapable 风格）

**题目**：实现三种钩子：① `SyncHook`——同步串行调用所有 tap 的回调；② `SyncWaterfallHook`——把上一个回调的返回值传给下一个（初始值由 call 传入）；③ `AsyncSeriesHook`——异步串行执行（回调返回 Promise，等待完成后再执行下一个）。每个 Hook 提供 `tap(name, fn)` 注册、`call(...args)`（AsyncSeries 返回 Promise）。要求：① tap 可命名，重复 tap 同名允许（都执行）；② 提供 `tapOnce(name, fn)` 只执行一次；③ 错误向外抛出/拒绝，中断后续；④ AsyncSeries 中若某 tap 抛错，Promise reject 且不执行后续。边界：无 tap 时 call 返回初始值（Waterfall）或 undefined（Sync）；tap 的 this 指向一个含 `name` 的上下文。

**答**：

```javascript
class BaseHook {
  constructor(args = []) { this.taps = []; this.args = args; }
  tap(name, fn) { this.taps.push({ name, fn, type: 'tap' }); return this; }
  tapOnce(name, fn) { this.taps.push({ name, fn, type: 'once', done: false }); return this; }
  _ctx(t) { return { name: t.name }; }
}
class SyncHook extends BaseHook {
  call(...args) {
    for (const t of this.taps) {
      if (t.type === 'once' && t.done) continue;
      t.fn.call(this._ctx(t), ...args);
      if (t.type === 'once') t.done = true;
    }
  }
}
class SyncWaterfallHook extends BaseHook {
  call(initial, ...args) {
    let value = initial;
    for (const t of this.taps) {
      if (t.type === 'once' && t.done) continue;
      value = t.fn.call(this._ctx(t), value, ...args);
      if (t.type === 'once') t.done = true;
    }
    return value;
  }
}
class AsyncSeriesHook extends BaseHook {
  async call(...args) {
    for (const t of this.taps) {
      if (t.type === 'once' && t.done) continue;
      await t.fn.call(this._ctx(t), ...args);   // 抛错自动 reject 并中断
      if (t.type === 'once') t.done = true;
    }
  }
}

const wf = new SyncWaterfallHook();
wf.tap('add1', v => v + 1).tapOnce('add10', v => v + 10);
console.log(wf.call(0)); // 11
const async = new AsyncSeriesHook();
async.tap('a', async () => console.log('a')).tap('b', async () => console.log('b'));
async.call().then(() => console.log('done')); // a, b, done（串行）
```

**评分点**：
- 三种钩子语义正确（Sync 串行、Waterfall 传递返回值、AsyncSeries 异步串行）。
- tapOnce 只执行一次且状态管理正确。
- 错误传播：同步抛出中断、异步 reject 中断后续（符合 tapable 契约）。
- this 上下文含 name、无 tap 返回初始值（边界与 API 细节）。
