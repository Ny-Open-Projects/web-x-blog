---
title: [JS-024] 手写实现 Function.prototype.bind？如何处理 new 调用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-024：手写实现 Function.prototype.bind？如何处理 new 调用？

**答**：
- 返回一个新函数，内部用 apply 绑定 this 并拼接预设参数。
- new 调用绑函数时 this 应指向新实例：判断 `this instanceof bound`，并用原型链串联（Object.create）。
- 返回函数要与原函数同名（可选）、保持 length 语义可忽略。
- bind 后的函数也有 prototype 供 new 使用，需手动挂接。

```javascript
Function.prototype.myBind = function (context, ...presetArgs) {
  const fn = this;
  function bound(...laterArgs) {
    // new 调用时 this 是新实例，忽略绑定的 context
    return fn.apply(this instanceof bound ? this : context,
                    [...presetArgs, ...laterArgs]);
  }
  // 维持原型链，让 new bound() 得到原函数的原型能力
  bound.prototype = Object.create(fn.prototype);
  return bound;
};

function Person(name, age) {
  this.name = name;
  this.age = age;
}
Person.prototype.hi = function () { return `hi ${this.name}`; };

const BoundPerson = Person.myBind(null, 'Tom');
const p = new BoundPerson(18);
console.log(p.name, p.age, p.hi()); // Tom 18 "hi Tom"
```
