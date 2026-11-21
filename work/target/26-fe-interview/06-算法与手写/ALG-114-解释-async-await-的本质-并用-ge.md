---
title: [ALG-114] 解释 async/await 的本质，并用 generator + Promise 手写一个等价的执行器（co/spawn）？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-114：解释 async/await 的本质，并用 generator + Promise 手写一个等价的执行器（co/spawn）？
**答**：async 函数 = 自动执行的 generator + Promise 语法糖。手写执行器四步：① 实例化 generator；② 递归调用 `gen.next()` 驱动；③ 把 yield 的值 `Promise.resolve` 包装后 then——成功走 `next(v)` 把结果还给 await 表达式，失败走 `throw(e)` 让 generator 内 try/catch 捕获；④ done 为 true 时以最后值 resolve 整体 Promise。

```javascript
function spawn(genFn) {
  return new Promise((resolve, reject) => {
    const gen = genFn();
    const step = (nextFn, arg) => {
      let res;
      try { res = nextFn.call(gen, arg); }        // next 或 throw 注入
      catch (e) { return reject(e); }             // generator 内抛出的错误
      const { value, done } = res;
      if (done) return resolve(value);
      // await 后是普通值也包装成 Promise，统一处理
      Promise.resolve(value).then(
        v => step(gen.next, v),                   // 成功 => 结果还给 await
        e => step(gen.throw, e)                   // 失败 => 在 yield 处抛出
      );
    };
    step(gen.next);
  });
}
// function* main() { const r = yield fetchUser(); yield saveLog(r); }
// spawn(main) 等价于 async function main
```
