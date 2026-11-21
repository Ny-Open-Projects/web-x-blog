---
title: [JS-264] 笔试：手写简易 co（Promise 驱动生成器）
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 生成器]
type: 笔试题
---

## JS-264：笔试：手写简易 co

**题目**：实现 `co(genFn)`：自动驱动生成器，yield 出的值若是 Promise 则等结果传回；生成器 throw 传出错误则 reject；返回 Promise。

**答**：
```javascript
function co(genFn) {
  return new Promise((resolve, reject) => {
    const gen = genFn();
    const step = (nextOrThrow, arg) => {
      let res;
      try {
        res = nextOrThrow === 'next' ? gen.next(arg) : gen.throw(arg);
      } catch (e) { return reject(e); }          // 同步错误
      if (res.done) return resolve(res.value);
      Promise.resolve(res.value).then(
        (v) => step('next', v),                   // 结果传回 next
        (e) => step('throw', e)                   // 异常注入生成器（可被其 try/catch）
      );
    };
    step('next');
  });
}
// 验证
co(function* () {
  try {
    const a = yield Promise.resolve(1);
    const b = yield Promise.reject(new Error('boom')); // 生成器可 catch
    return a + 2;
  } catch (e) {
    return 'caught:' + e.message;
  }
}).then(console.log); // 'caught:boom'
```

**评分点**：
- 递归 step + Promise.then 链接生成器与异步——核心 20 行
- 错误两条路径：同步 catch → reject；异步错误用 gen.throw 注入（生成器还能自救）
- Promise.resolve 包装（yield 出非 Promise 值也能跑）
- done 时 resolve 最终返回值
