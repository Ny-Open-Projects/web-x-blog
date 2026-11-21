---
title: [JS-032] class 中的 getter/setter 与计算属性怎么用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-032：class 中的 getter/setter 与计算属性怎么用？

**答**：
- `get/set` 定义访问器属性，语法像属性、行为是函数，可做校验与派生值。
- 计算属性名 `[expr]` 允许用表达式/Symbol 定义方法或字段。
- 访问器只定义在 prototype 上，配合私有字段可暴露只读视图。
- 避免在 getter 内再次读取自身造成无限递归。

```javascript
class Temperature {
  #celsius = 0;
  constructor(c) { this.celsius = c; }

  get celsius() { return this.#celsius; }
  set celsius(v) {
    if (typeof v !== 'number' || Number.isNaN(v)) throw new TypeError('need number');
    this.#celsius = v;
  }
  get fahrenheit() { return this.#celsius * 1.8 + 32; } // 派生只读

  [Symbol.toPrimitive](hint) {                          // 计算属性名 + 协议
    return hint === 'string' ? `${this.#celsius}°C` : this.#celsius;
  }
}

const t = new Temperature(100);
console.log(`${t}`);      // 100°C
console.log(t.fahrenheit);// 212
// t.fahrenheit = 0;      // 静默失败（无 setter，严格模式报错）
```
