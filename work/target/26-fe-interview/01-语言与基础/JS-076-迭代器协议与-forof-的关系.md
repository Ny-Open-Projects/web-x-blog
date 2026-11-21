---
title: [JS-076] 迭代器协议与 for...of 的关系？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-076：迭代器协议与 for...of 的关系？

**答**：
- 可迭代协议：对象实现 `Symbol.iterator` 方法，返回一个带 next() 的迭代器。
- next() 返回 `{ value, done }`，done 为 true 表示遍历结束。
- for...of、展开运算符、解构、Array.from 都消费可迭代对象。
- for...in 遍历可枚举字符串键，for...of 遍历值；普通对象默认不可迭代。

```javascript
const range = {
  from: 1,
  to: 3,
  [Symbol.iterator]() {          // 迭代器工厂
    let cur = this.from;
    const end = this.to;
    return {
      next() {
        return cur <= end
          ? { value: cur++, done: false }
          : { value: undefined, done: true };
      },
    };
  },
};

for (const n of range) console.log(n); // 1 2 3
console.log([...range]);               // [1, 2, 3]
const [x1, x2] = range;                // 解构也消费迭代器

// for...in 与 for...of 对比
const arr = ['a', 'b'];
for (const i in arr) console.log(i);    // '0' '1'，键
for (const v of arr) console.log(v);    // 'a' 'b'，值
// for (const v of { a: 1 });           // TypeError，普通对象不可迭代
```
