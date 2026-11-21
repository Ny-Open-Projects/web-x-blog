---
title: [JS-033] Object.create、Object.assign 与原型操作怎么用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-033：Object.create、Object.assign 与原型操作怎么用？

**答**：
- `Object.create(proto, props)` 创建指定原型的新对象，`create(null)` 生成无原型对象，适合做纯字典。
- `Object.assign(target, ...src)` 拷贝**可枚举自有**属性，浅拷贝。
- `Object.setPrototypeOf` 修改原型（性能差，尽量在创建时定好）。
- `Object.freeze` 冻结对象防修改（浅层），`isFrozen` 检测。

```javascript
const proto = { greet() { return 'hi'; } };
const obj = Object.create(proto, {
  name: { value: 'Tom', enumerable: true, writable: true },
});
console.log(obj.greet()); // hi，来自原型

const dict = Object.create(null);
dict.key = 1;
console.log(dict.toString); // undefined，无原型污染风险

const merged = Object.assign({}, { a: 1 }, { b: 2, a: 9 });
console.log(merged); // { a: 9, b: 2 }，后面的覆盖前面

const nested = { a: { b: 1 } };
const copy = Object.assign({}, nested);
copy.a.b = 99;
console.log(nested.a.b); // 99，浅拷贝
```

## 五、Promise 与异步
