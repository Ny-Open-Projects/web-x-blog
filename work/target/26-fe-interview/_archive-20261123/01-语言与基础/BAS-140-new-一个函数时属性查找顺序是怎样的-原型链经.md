---
title: [BAS-140] new 一个函数时属性查找顺序是怎样的？（原型链经典输出题）
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-140：new 一个函数时属性查找顺序是怎样的？（原型链经典输出题）
**答**：
- new 做四件事：创建空对象 → 链到构造函数的 prototype → 以 this 执行构造函数 → 无显式返回对象时返回新对象。
- 属性查找先看自有属性，找不到沿 `__proto__` 逐级上溯到 Object.prototype，再没有就是 undefined。
- constructor 属性本身定义在构造函数的 prototype 上。

```javascript
function Foo() { this.a = 1; }
Foo.prototype.a = 2;
Foo.prototype.b = 3;
const f = new Foo();
console.log(f.a);                   // 1 —— 自有属性优先于原型上的同名属性
console.log(f.b);                   // 3 —— f 自身没有，沿 __proto__ 到 Foo.prototype 找到
console.log(f.c);                   // undefined —— 一路找到 Object.prototype 仍没有
console.log(f.constructor === Foo); // true —— constructor 就挂在 Foo.prototype 上
```

## 十六、异步与事件循环补充
