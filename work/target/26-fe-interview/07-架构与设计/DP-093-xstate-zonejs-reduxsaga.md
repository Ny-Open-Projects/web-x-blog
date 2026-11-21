---
title: [DP-093] xstate、zone.js、redux-saga 里各有什么模式？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-093：xstate、zone.js、redux-saga 里各有什么模式？
**答**：
- **xstate**：状态模式 + 策略（转移表）+ 备忘录（context 快照可序列化）+ 解释器（状态图即文法）。
- **zone.js**：代理/装饰器——monkey-patch 所有异步 API（setTimeout/Promise/addEventListener），把"异步上下文"透明织入（Angular 变更检测的触发源）。
- **redux-saga**：解释器模式——saga 用 Generator 产出 effect 描述符（纯数据），引擎负责"解释执行"，因此可单测。
- 共同点：都在"不改业务代码"的前提下附加控制逻辑（AOP 思想）。

```javascript
// 1. zone.js 思想：代理所有异步 API，织入上下文追踪
const originalSetTimeout = globalThis.setTimeout;
globalThis.setTimeout = function patched(fn, delay, ...args) {   // 代理：控制访问
  const zone = Zone.current;                                      // 捕获当前 Zone 上下文
  return originalSetTimeout(function zoned(...a) {
    zone.run(() => fn(...a));                                     // 回调仍在原 Zone 内执行
  }, delay, ...args);
};
class Zone {
  static #current = new Zone('root');
  static get current() { return this.#current; }
  #tasks = 0;
  constructor(name, onStable) { this.name = name; this.onStable = onStable; }
  run(fn) {                                                        // 模板方法：进入 -> 执行 -> 检查
    const prev = Zone.#current;
    Zone.#current = this;
    this.#tasks++;
    try { return fn(); } finally {
      Zone.#current = prev;
      if (--this.#tasks === 0) this.onStable?.(); // 所有异步任务完成 -> 触发变更检测
    }
  }
}
// Angular 的 NgZone：zone.run 内所有异步结束 => onMicrotaskEmpty => CD
const ngZone = new Zone('ngZone', () => console.log('异步全部完成，触发变更检测'));
ngZone.run(() => {
  setTimeout(() => console.log('异步回调'));
  setTimeout(() => console.log('另一个异步回调'));
});
// 异步回调 / 另一个异步回调 / 异步全部完成，触发变更检测

// 2. redux-saga 的解释器模式：effect 是纯描述，引擎解释执行
const CALL = 'CALL', PUT = 'PUT';
const call = (fn, ...args) => ({ [CALL]: true, fn, args });   // 描述符：不执行
const put = (action) => ({ [PUT]: true, action });
function* fetchUserSaga(id) {
  const user = yield call((x) => Promise.resolve({ id: x, name: 'Tom' }), id); // 描述"将调用"
  yield put({ type: 'USER_OK', user });                        // 描述"将派发"
}
// 引擎：迭代器逐条解释 effect（可替换任意实现 -> 单测时传入假 fn）
function runSaga(genFn, ...args) {
  const it = genFn(...args);
  (function next(input) {
    const { value, done } = it.next(input);
    if (done) return;
    if (value[CALL]) value.fn(...value.args).then(next);      // 解释 CALL
    else if (value[PUT]) { console.log('dispatch', value.action.type); next(); } // 解释 PUT
  })();
}
runSaga(fetchUserSaga, 1); // dispatch USER_OK —— 描述与执行分离，测试只需断言描述符
```
