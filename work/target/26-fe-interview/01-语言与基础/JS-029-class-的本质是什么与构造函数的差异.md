---
title: [JS-029] class 的本质是什么？与构造函数的差异？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-029：class 的本质是什么？与构造函数的差异？

**答**：
- class 本质仍是基于原型的语法糖：实例方法挂在 prototype 上，静态方法挂在类本身。
- 差异：class 内部默认严格模式；声明不提升（TDZ）；必须用 new 调用；方法不可枚举。
- constructor 在 new 时自动执行；类里所有方法默认绑定实例行为与普通原型方法一致。
- `typeof class` 仍是 `"function"`。

```javascript
class Animal {
  constructor(name) {
    this.name = name;          // 实例属性
  }
  speak() {                    // 挂在 Animal.prototype
    return `${this.name} makes a noise`;
  }
  static create(name) {        // 挂在 Animal 本身
    return new Animal(name);
  }
}

console.log(typeof Animal);                          // function
console.log(Animal.prototype.speak);                 // 函数
console.log(Object.keys(Animal.prototype));          // []，方法不可枚举
console.log(Animal.create('Cat').speak());           // Cat makes a noise

// 等价的 ES5 写法核心
// function Animal(name) { this.name = name }
// Animal.prototype.speak = function () {...}
```
