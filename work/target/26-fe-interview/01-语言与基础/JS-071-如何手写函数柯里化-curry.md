---
title: [JS-071] 如何手写函数柯里化 curry？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-071：如何手写函数柯里化 curry？

**答**：
- 柯里化：把 `f(a, b, c)` 转为 `f(a)(b)(c)` 任意组合，参数收集满 `fn.length` 才执行。
- 实现要点：收集参数，数量足够调用原函数，否则返回新的收集函数。
- 展开 rest 参数后 `fn.length` 需注意默认参数不计入。
- 应用：参数复用、延迟执行、配合偏函数简化调用。

```javascript
function curry(fn) {
  return function collect(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return (...more) => collect(...args, ...more); // 继续收集
  };
}

function add(a, b, c) { return a + b + c; }
const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3)); // 6
console.log(curriedAdd(1, 2)(3)); // 6
console.log(curriedAdd(1)(2, 3)); // 6

// 参数复用
const log = curry((level, tag, msg) => `[${level}][${tag}] ${msg}`);
const errorLog = log('ERROR');
const apiError = errorLog('api');
apiError('timeout');  // [ERROR][api] timeout

// 支持 占位 的进阶版可用递归比较 args.length 与 fn.length
console.log(add.length, ((a, b = 1) => {}).length); // 3 1
```
