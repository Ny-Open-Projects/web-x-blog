---
title: [JS-148] 手写 async/await 执行器？generator 如何被自动驱动？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-148：手写 async/await 执行器？generator 如何被自动驱动？

**答**：
- 本质：async 函数是「generator + 自动执行器」的语法糖，await 对应 yield。
- 执行器用递归 step 驱动：`gen.next(v)` 拿到 { value, done }，把 value 包成 Promise，resolve 后把结果传回 next。
- 错误处理：Promise reject 时调用 `gen.throw(e)`，让错误在 generator 内部被 try/catch 捕获。
- done 为 true 时 resolve 最终返回值，整个执行器返回一个 Promise——与真 async 函数行为一致。

```javascript
function run(genFn) {
  return (...args) =>
    new Promise((resolve, reject) => {
      const gen = genFn(...args);
      const step = (method, arg) => {
        let result;
        try { result = gen[method](arg); }        // next 或 throw
        catch (e) { return reject(e); }           // generator 外抛错
        const { value, done } = result;
        if (done) return resolve(value);          // 执行完毕 → 整体 resolve
        Promise.resolve(value).then(
          (v) => step('next', v),                 // await 成功 → 继续推进
          (e) => step('throw', e)                 // await 失败 → 在 generator 内抛出
        );
      };
      step('next');
    });
}

// 用法：generator 版 async/await
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const main = run(function* (uid) {
  try {
    const user = yield sleep(50).then(() => ({ id: uid, name: 'Alice' }));
    const posts = yield sleep(50).then(() => ['p1', 'p2']);
    return { user, posts };
  } catch (e) {
    return { error: e.message };                  // gen.throw 会落进这个 catch
  }
});
main(7).then((r) => console.log(JSON.stringify(r)));
// {"user":{"id":7,"name":"Alice"},"posts":["p1","p2"]}
```
