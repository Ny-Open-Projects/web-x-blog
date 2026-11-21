---
title: [JS-025] new 操作符做了什么？如何手写模拟？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-025：new 操作符做了什么？如何手写模拟？

**答**：
- 四步：创建空对象、把对象的原型指向构造函数的 prototype、以该对象为 this 执行构造函数、决定返回值。
- 返回值规则：构造函数显式返回对象（含函数）时用它，否则返回新对象。
- `instanceof` 之所以成立，是因为第二步的原型指向。
- 手写实现可以完整还原这套流程。

```javascript
function myNew(Ctor, ...args) {
  const obj = Object.create(Ctor.prototype); // 1+2 步
  const result = Ctor.apply(obj, args);      // 3 步
  return (result !== null && (typeof result === 'object' || typeof result === 'function'))
    ? result
    : obj;                                   // 4 步
}

function Dog(name) {
  this.name = name;
  // return { fake: true }; // 若返回对象，new 的结果就是它
}
Dog.prototype.bark = () => 'woof';

const d = myNew(Dog, '旺财');
console.log(d.name);            // 旺财
console.log(d instanceof Dog);  // true
console.log(d.bark());          // woof
```

## 四、原型、继承与 class
