---
title: [JS-023] 手写实现 Function.prototype.apply？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-023：手写实现 Function.prototype.apply？

**答**：
- 与 call 唯一区别：第二个参数是数组或类数组，调用时展开。
- 参数需兼容 null/undefined（等价于不传参）。
- 类数组参数可用展开运算符展开，兼容老环境时用 for 循环。
- 同样要考虑 Symbol 键防冲突、返回值透传。

```javascript
Function.prototype.myApply = function (context, args) {
  context = context ?? globalThis;
  context = Object(context);
  const key = Symbol('fn');
  context[key] = this;
  let result;
  if (args == null) {
    result = context[key]();
  } else {
    result = context[key](...args); // 类数组也可展开（可迭代）
  }
  delete context[key];
  return result;
};

function sum(a, b, c) { return a + b + c + this.base; }
console.log(sum.myApply({ base: 100 }, [1, 2, 3])); // 106
console.log(sum.myApply({ base: 100 }, null));      // NaN，缺参相加
```
