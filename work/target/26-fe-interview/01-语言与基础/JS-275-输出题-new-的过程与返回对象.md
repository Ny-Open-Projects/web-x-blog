---
title: [JS-275] 输出题：new 的过程与返回对象
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 原型链]
type: 笔试题
---

## JS-275：输出题：new 的过程与返回对象

**题目**：描述 new 的四步过程；构造函数返回对象/原始值时实例分别是什么。

**答**：
```javascript
function A() { this.x = 1; }
const a = new A();
// 四步：① 创建空对象，原型指向 A.prototype
//       ② 以该对象为 this 执行构造函数
//       ③ 若构造函数返回对象 → 用返回对象；返回原始值/无返回 → 用步骤①对象
console.log(a.x);                    // 1
a.__proto__ === A.prototype;         // true

function B() { this.x = 1; return { y: 2 }; }
new B().x;  // undefined —— 返回对象完全替代实例
new B().y;  // 2

function C() { this.x = 1; return 42; }  // 返回原始值被忽略
new C().x;  // 1

// 箭头函数不能 new（无 [[Construct]]、无 this）
// const F = () => {}; new F(); // ❌ TypeError
```

**评分点**：
- 四步流程完整（原型绑定是必答点）
- 「返回对象覆盖实例、原始值被忽略」的规则——本题核心判分点
- 箭头函数不可 new 的原因（无 this/无 Construct 内部方法）
- new.target 可判断是否被 new 调用（加分）
