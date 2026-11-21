---
title: [DP-021] 什么是原型模式？`Object.create` 在其中扮演什么角色？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-021：什么是原型模式？`Object.create` 在其中扮演什么角色？
**答**：
- 原型模式：以一个已有对象为模板克隆出新对象，新对象通过原型链共享模板的方法。
- `Object.create(proto)` 直接指定新对象的原型——比"构造函数 + prototype"更直接地表达"从模板派生"。
- 适用：对象创建昂贵（需要大量配置/初始化），或希望多个对象共享同一套行为定义。
- 注意：`Object.create` 是浅克隆——引用类型的属性会被所有派生对象共享，见下一题的坑。

```javascript
// 原型对象：定义共享行为
const chartPrototype = {
  type: 'base',
  colors: ['red', 'blue'],           // 引用属性：浅克隆风险点
  render() { console.log(`渲染 ${this.type}，主题色 ${this.colors[0]}`); },
  clone(overrides) {                 // 原型模式的标准克隆手法
    return Object.assign(Object.create(Object.getPrototypeOf(this)), this, overrides);
  },
};
// 从原型派生两个具体图表
const line = chartPrototype.clone({ type: 'line' });
const bar = chartPrototype.clone({ type: 'bar' });
line.render();  // 渲染 line，主题色 red
bar.render();   // 渲染 bar，主题色 red

// Object.create 直接以某对象为原型
const base = { greet() { return `hi ${this.name}`; } };
const ins = Object.create(base); // ins.__proto__ === base，方法共享不复制
ins.name = 'Tom';
console.log(ins.greet()); // hi Tom

// 验证"方法共享"：改原型方法，所有派生对象同步生效
chartPrototype.render = function () { console.log(`新渲染逻辑 ${this.type}`); };
line.render(); // 新渲染逻辑 line —— 原型模式的内存优势
```
