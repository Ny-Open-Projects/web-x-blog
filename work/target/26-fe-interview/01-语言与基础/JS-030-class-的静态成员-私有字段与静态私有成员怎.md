---
title: [JS-030] class 的静态成员、私有字段与静态私有成员怎么用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-030：class 的静态成员、私有字段与静态私有成员怎么用？

**答**：
- `static` 方法和属性属于类本身，通过 `Class.xxx` 访问，实例不可访问。
- 私有字段 `#field` 是语言级真私有，类外部无法访问，比 `_field` 约定强。
- `#field in obj` 可安全探测私有字段是否存在；私有方法与静态私有也支持。
- 静态块 `static {}` 可在类定义期做复杂初始化。

```javascript
class Counter {
  static instanceCount = 0;      // 静态属性
  #count = 0;                    // 私有字段
  static #secret = 'hidden';     // 静态私有

  increment() { this.#count += 1; }
  get value() { return this.#count; }

  static fromJSON(obj) {
    const c = new Counter();
    c.#count = obj.count ?? 0;
    return c;
  }
  static hasCounter(obj) { return #count in obj; }
}

const c = new Counter();
c.increment();
console.log(c.value);           // 1
// console.log(c.#count);       // SyntaxError，类外访问私有字段
console.log(Counter.instanceCount); // 0
```
