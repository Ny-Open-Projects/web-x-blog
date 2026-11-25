---
title: [RBL-045] 笔试：手写 tapable 风格的 SyncHook 与 AsyncSeriesHook
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-045：笔试：手写 tapable 风格的 SyncHook 与 AsyncSeriesHook
**答**：实现两个钩子类：1) SyncHook：tap 注册、call 同步串行调用；2) AsyncSeriesHook：tap/tapAsync/tapPromise 注册，promise() 串行执行异步回调（前一个完成才执行下一个）；3) 支持拦截子串不匹配的参数透传；4) call 传参给每个回调；5) tapAsync 回调以 (err) => 结尾，err 非 null 时中断后续。

```javascript
class SyncHook {
  constructor(args = []) { this._args = args; this.taps = []; }
  tap(name, fn) { this.taps.push({ name, fn }); }
  call(...args) {
    for (const { fn } of this.taps) fn(...args);
  }
}

class AsyncSeriesHook {
  constructor(args = []) { this._args = args; this.taps = []; }
  tap(name, fn) { this.taps.push({ type: 'sync', fn }); }
  tapAsync(name, fn) { this.taps.push({ type: 'async', fn }); }
  tapPromise(name, fn) { this.taps.push({ type: 'promise', fn }); }

  promise(...args) {
    // 递归链式：前一个完成才触发下一个（series 语义）
    const run = (i) => {
      if (i >= this.taps.length) return Promise.resolve();
      const t = this.taps[i];
      if (t.type === 'sync') { t.fn(...args); return run(i + 1); }
      if (t.type === 'promise') return t.fn(...args).then(() => run(i + 1));
      return new Promise((resolve, reject) =>
        t.fn(...args, (err) => err ? reject(err) : resolve())).then(() => run(i + 1));
    };
    return run(0);
  }
}

// 用法
const h = new AsyncSeriesHook(['compilation']);
h.tap('a', (c) => console.log('sync a'));
h.tapAsync('b', (c, cb) => setTimeout(() => { console.log('async b'); cb(); }, 10));
h.tapPromise('c', async (c) => console.log('promise c'));
h.promise({}); // 顺序：a → b → c
module.exports = { SyncHook, AsyncSeriesHook };
```
**评分点**：
- AsyncSeries 的「串行」正确：前一回调 cb() 之后才执行下一个（并行是 AsyncParallelHook）。
- tapAsync 回调 err 非空要中断后续（reject）。
- 三种 tap 类型都支持（tapable 契约）。
- SyncHook.call 顺序遍历（保序）。
- 能答出 tapable 按注册类型编译为不同执行函数、hook 名与参数个数约束（_args）。
