---
title: [HW-006] 手写 async 执行器（Generator 自动执行）
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-006：手写 async 执行器（Generator 自动执行）

**答**：
- 评分点：`gen.next(value)` 的返回值 `{ value, done }`，value 要用 `Promise.resolve()` 包装成 thenable 再消费；递归驱动：未 done 就继续 `next`，把上一段 yield 的结果作为下一次 next 的入参回传（这就是 `const a = yield x` 能拿到值的原因）；done 为 true 时 resolve 最终值；用 `gen.throw(e)` 把 Promise 的失败注入回 generator 内部，让 try/catch 能捕获；执行器整体返回一个 Promise。

```javascript
// ===== 5 分钟速写版 =====
function asyncTo(genFn) {
  return new Promise((resolve, reject) => {
    const gen = genFn();
    const step = (nextFn, val) => {
      let result;
      try { result = nextFn(val); }
      catch (e) { return reject(e); }
      if (result.done) return resolve(result.value);
      Promise.resolve(result.value).then(
        v => step(gen.next.bind(gen), v),          // 成功 → 注入下一轮
        e => step(gen.throw.bind(gen), e)          // 失败 → throw 进 generator
      );
    };
    step(gen.next.bind(gen), undefined);
  });
}
// 用法：asyncTo(function* () { const a = yield fetchA(); const b = yield fetchB(a); return b; })

// ===== 标准完整版（含边界处理）=====
function asyncToPro(genFn, ...args) {
  return new Promise((resolve, reject) => {
    let gen;
    try { gen = genFn(...args); }        // 支持向 generator 传参
    catch (e) { return reject(e); }
    if (!gen || typeof gen.next !== 'function') {
      return reject(new TypeError('genFn must return a generator'));
    }
    const onFulfilled = val => { drain('next', val); };
    const onRejected = err => { drain('throw', err); };
    function drain(method, val) {
      let result;
      try { result = gen[method](val); }
      catch (e) { return reject(e); }    // generator 内部未捕获的异常 → 整体 reject
      if (result.done) {
        // 最终返回值若是 Promise，继续跟随其落定
        return Promise.resolve(result.value).then(resolve, reject);
      }
      Promise.resolve(result.value).then(onFulfilled, onRejected);
    }
    drain('next', undefined);
  });
}
// 面试追问点：
// 1. 为什么 next(v) 能让 const a = yield x 拿到 v —— next 的参数会作为上一处 yield 表达式的求值结果
// 2. 与真 async/await 差异 —— await 由引擎在微任务层面实现，且语法上不需要手写驱动器
```

---
