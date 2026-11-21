---
title: [JS-020] call、apply、bind 有什么区别？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-020：call、apply、bind 有什么区别？

**答**：
- 三者都能显式指定 this；call 逐个传参、apply 传参数数组。
- bind 返回绑定了 this 的新函数，可预设参数（偏函数），不立即执行。
- bind 的绑定是永久的，再次 call/apply 无法覆盖（new 除外）。
- 性能上直接 call 优于创建中间 bind 函数，但可读性优先。

```javascript
function greet(greeting, punctuation) {
  return `${greeting}, ${this.name}${punctuation}`;
}
const person = { name: 'Tom' };

console.log(greet.call(person, 'Hi', '!'));      // "Hi, Tom!"
console.log(greet.apply(person, ['Hey', '?']));  // "Hey, ?"

const boundGreet = greet.bind(person, 'Yo');
console.log(boundGreet('.'));                    // "Yo, Tom."

// 经典应用：类数组转数组
function fn() {
  const args = Array.prototype.slice.call(arguments); // 老写法
  const args2 = Array.from(arguments);                // 现代写法
  return [args.length, args2.length];
}
console.log(fn(1, 2, 3)); // [3, 3]
```
