---
title: [JS-143] 原型链继承输出题？构造函数返回对象时 new 的结果有什么变化？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-143：原型链继承输出题？构造函数返回对象时 new 的结果有什么变化？

**答**：
- `new` 的返回值规则：构造函数显式返回一个对象时，new 的结果就是那个对象，`this` 上挂的属性全部丢弃。
- 返回原始值（数字/字符串等）时被忽略，正常返回 `this`。
- 原型链继承：`Object.create(Parent.prototype)` 让 Child 的原型链指向 Parent.prototype，方法得以复用。
- `Parent.call(this)` 借用构造函数，把 Parent 的实例属性复制到 Child 实例上。
- 重设原型后 `constructor` 丢失，必须手动修复，否则实例.constructor 指向 Parent。

```javascript
function Normal() { this.x = 1; }
function ReturnObj() { this.y = 2; return { z: 3 }; }   // 返回对象：new 的结果是它
function ReturnPrim() { this.w = 4; return 42; }        // 返回原始值：被忽略

console.log(new Normal().x);            // 1
const r = new ReturnObj();
console.log(r.y, r.z);                  // undefined 3 —— this.y 被整个丢弃
console.log(new ReturnPrim().w);        // 4 —— 原始返回值无效，正常返回 this

function Parent() { this.tag = 'P'; }
Parent.prototype.hello = function () { return 'hello-' + this.tag; };
function Child() {
  Parent.call(this);                    // 借用构造函数：继承实例属性
  this.tag = 'C';
}
Child.prototype = Object.create(Parent.prototype); // 原型链继承方法
Child.prototype.constructor = Child;    // 修复 constructor

const c = new Child();
console.log(c.hello());                 // hello-C
console.log(c instanceof Child);        // true
console.log(c instanceof Parent);       // true —— 原型链上有 Parent.prototype
console.log(c.constructor === Child);   // true（已手动修复）
console.log(Child.prototype.__proto__ === Parent.prototype); // true —— 链条关系
```
