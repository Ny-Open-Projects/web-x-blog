---
title: [JS-142] 闭包计数与 IIFE 循环输出题？var、let、IIFE 三种写法输出有什么区别？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-142：闭包计数与 IIFE 循环输出题？var、let、IIFE 三种写法输出有什么区别？

**答**：
- var 声明的 i 属于唯一的函数作用域，异步回调执行时循环已结束，读到的是最终值。
- IIFE 通过参数把每轮的值拷贝进独立的闭包作用域，是 ES5 时代的标准解法。
- let 让循环体每轮创建新的词法环境，效果等价于 IIFE，且是规范内置行为。
- 闭包计数器：外部拿不到 count 变量，只能通过暴露的方法读写，这就是闭包封装私有状态。

```javascript
// 1. var + 异步：所有回调共享同一个 i
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log('A', i));   // A 3 ｜ A 3 ｜ A 3 —— 回调执行时 i 已是 3
}
// 2. IIFE：每轮用参数 k 保存当时的值
for (var j = 0; j < 3; j++) {
  (function (k) {
    setTimeout(() => console.log('B', k)); // B 0 ｜ B 1 ｜ B 2
  })(j);
}
// 3. let：每轮迭代创建新的词法环境
for (let m = 0; m < 3; m++) {
  setTimeout(() => console.log('C', m));   // C 0 ｜ C 1 ｜ C 2
}
// 4. 闭包计数器：封装私有状态
function createCounter(start = 0, step = 1) {
  let count = start;                       // 外部无法直接访问
  return {
    inc: () => (count += step),
    dec: () => (count -= step),
    get: () => count,
  };
}
const c = createCounter(10, 5);
c.inc(); c.inc(); c.dec();
console.log(c.get());  // 20
```
