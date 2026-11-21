---
title: [JS-072] 如何手写 instanceof？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-072：如何手写 instanceof？

**答**：
- 原理：沿右侧构造函数的 prototype 在左侧对象的原型链上逐级查找。
- 找到相等返回 true，走到 null（原型链尽头）返回 false。
- 注意：基本类型直接返回 false；`Object.getPrototypeOf` 优于已废弃的 `__proto__`。
- 结合 JS-025 可知 new 的第 2 步正是 instanceof 成立的前提。

```javascript
function myInstanceof(left, right) {
  if (left === null || (typeof left !== 'object' && typeof left !== 'function')) {
    return false; // 基本类型必然不在原型链上
  }
  let proto = Object.getPrototypeOf(left);
  const target = right.prototype;
  while (proto !== null) {
    if (proto === target) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}

function Animal() {}
function Dog() {}
Dog.prototype = Object.create(Animal.prototype); // 模拟继承

const d = new Dog();
console.log(myInstanceof(d, Dog));    // true
console.log(myInstanceof(d, Animal)); // true，沿链向上
console.log(myInstanceof(d, Array));  // false
console.log(myInstanceof('str', String)); // false，基本类型
console.log(myInstanceof(new String('s'), String)); // true
```

## 十一、内存、严格模式与其他专题
