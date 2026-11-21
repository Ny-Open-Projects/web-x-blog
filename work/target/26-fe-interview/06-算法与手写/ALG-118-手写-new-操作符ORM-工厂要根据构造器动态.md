---
title: [ALG-118] 手写 new 操作符：ORM 工厂要根据构造器动态创建实例，且构造器可能显式 return 一个对象？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-118：手写 new 操作符：ORM 工厂要根据构造器动态创建实例，且构造器可能显式 return 一个对象？
**答**：new 做四件事：① 创建空对象，原型指向构造函数的 `prototype`；② 把 this 绑到新对象执行构造函数；③ 若构造函数显式返回对象/函数，则以返回值为准（否则丢弃返回值）；④ 返回新对象。手写时用 `Object.create(Ctor.prototype)` 一步完成原型挂载。时间 O(1)。

```javascript
function myNew(Ctor, ...args) {
  if (typeof Ctor !== 'function') throw new TypeError('not a constructor');
  const obj = Object.create(Ctor.prototype); // 1. 原型指向构造函数 prototype
  const ret = Ctor.apply(obj, args);         // 2. this 绑定新对象执行
  // 3. 显式返回对象或函数时以它为准，否则用新对象
  return (ret !== null && (typeof ret === 'object' || typeof ret === 'function'))
    ? ret
    : obj;
}
// function Model(data) { this.data = data; }
// myNew(Model, { id: 1 }) instanceof Model => true
// function Singleton() { return { shared: true }; } 显式返回对象会被采用
```
