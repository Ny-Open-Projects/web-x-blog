---
title: [JS-021] 箭头函数的 this 与普通函数有什么不同？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-021：箭头函数的 this 与普通函数有什么不同？

**答**：
- 箭头函数没有自己的 this/arguments/super，this 沿词法作用域捕获定义处外层的 this。
- 不能用 call/apply/bind 改变箭头函数的 this，这些调用只影响参数。
- 不能作为构造函数（无 [[Construct]]），没有 prototype。
- 因此不适合作对象方法（this 不指向对象）和原型方法，适合回调保 this。

```javascript
const timer = {
  seconds: 0,
  start() {
    // start 是普通方法，this 是 timer
    setInterval(() => {
      this.seconds++; // 箭头函数捕获 start 的 this
    }, 1000);
  },
  wrongStart() {
    setInterval(function () {
      // this 是 window，报 NaN 递增
      console.log(this.seconds); // undefined
    }, 1000);
  },
};

// 对象字面量中的箭头函数
const obj = {
  name: 'obj',
  say: () => console.log(this.name), // this 是外层（模块/window），undefined
};

// 不能 new
const A = () => {};
// new A(); // TypeError: A is not a constructor
```
