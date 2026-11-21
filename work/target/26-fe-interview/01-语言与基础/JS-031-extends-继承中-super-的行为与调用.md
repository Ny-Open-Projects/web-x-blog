---
title: [JS-031] extends 继承中 super 的行为与调用顺序？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-031：extends 继承中 super 的行为与调用顺序？

**答**：
- 子类 constructor 必须先 `super(...)` 才能使用 this，否则 ReferenceError。
- super 调用父构造函数时，this 被隐式创建并绑定，随后父类在其上追加属性。
- 方法里的 `super.method()` 沿原型链找父类方法，且 this 仍是当前实例。
- `Object.getPrototypeOf(ChildClass) === ParentClass`，静态成员也会被继承。

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() { return `${this.name} makes a noise`; }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);              // 必须在 this 之前
    this.breed = breed;
  }
  speak() {
    return `${super.speak()} and woofs`; // this 仍是 Dog 实例
  }
  static defaultName() { return 'Dog'; }
  static create() { return new this(this.defaultName()); } // this 指向 Dog
}

const d = new Dog('旺财', '柴犬');
console.log(d.speak()); // 旺财 makes a noise and woofs
console.log(Object.getPrototypeOf(Dog) === Animal); // true
```
