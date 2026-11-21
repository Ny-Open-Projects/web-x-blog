---
title: [JS-137] 如何手写 new 与 Object.create 的完整版？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-137：如何手写 new 与 Object.create 的完整版？

**答**：
- new 四步：以 `Constructor.prototype` 为原型建对象 → 以新对象为 this 执行构造函数 → 若构造函数返回引用类型则以它为准 → 否则返回新对象。
- “返回对象生效”这个规则常被忽略：返回原始值会被忽略，返回对象会覆盖默认实例。
- Object.create 完整版要支持第二参数（属性描述符），并对 proto 做类型校验。
- 验证手段：instanceof、getPrototypeOf、描述符检查。

```javascript
function myNew(Constructor, ...args) {
  // 1. 创建以构造函数 prototype 为原型的空对象
  const obj = Object.create(Constructor.prototype);
  // 2. 执行构造函数，this 绑定新对象
  const result = Constructor.apply(obj, args);
  // 3. 构造函数显式返回引用类型时，以返回值为准；返回原始值被忽略
  return result instanceof Object ? result : obj;
}

function Person(name) { this.name = name; }
function Overrider() { return { overridden: true }; } // 返回对象
function PrimitiveReturn() { return 42; }             // 返回原始值被忽略

console.log(myNew(Person, 'tom').name);              // tom
console.log(myNew(Overrider()));                     // { overridden: true }
console.log(myNew(PrimitiveReturn()) instanceof PrimitiveReturn); // true
console.log(myNew(Person, 'a') instanceof Person);   // true

// Object.create 完整版：支持描述符
function myCreate(proto, props) {
  if (proto === null || (typeof proto !== 'object' && typeof proto !== 'function')) {
    throw new TypeError('Object prototype may only be an Object or null');
  }
  function F() {}        // 临时构造器桥接原型
  F.prototype = proto;
  const obj = new F();
  if (props !== undefined) Object.defineProperties(obj, props);
  return obj;
}

const base = { greet() { return `hi ${this.name}`; } };
const ins = myCreate(base, {
  name: { value: 'tom', enumerable: true },
});
console.log(ins.greet());                                  // hi tom
console.log(Object.getPrototypeOf(ins) === base);          // true
console.log(Object.keys(ins));                             // ['name']
```
