---
title: [JS-307] 输出题：Symbol.iterator 对象的 for-of 行为
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 迭代器]
type: 笔试题
---

## JS-307：输出题：自定义 Symbol.iterator 的 for-of 行为

**题目**：实现自定义迭代对象的 for-of 行为：done 提前为 true、value 为 undefined、多次迭代是否重新开始。

**答**：
```javascript
const box = {
  items: [1, 2, 3],
  [Symbol.iterator]() {
    let i = 0;
    return {
      next: () => i < this.items.length
        ? { value: this.items[i++], done: false }
        : { value: undefined, done: true },
    };
  },
};
for (const v of box) console.log(v);   // 1 2 3
for (const v of box) console.log(v);   // 再来一遍 1 2 3 —— 每次 [Symbol.iterator]() 新建迭代器

// 无限迭代器 + for-of 不 break = 死循环
const endless = {
  [Symbol.iterator]() {
    let i = 0;
    return { next: () => ({ value: i++, done: false }) };
  },
};
// for (const v of endless) {} // ❌ 挂死

// done: true 且带 value：for-of 不产出，但 spread 忽略；生成器 return 值仅 next 可见
const odd = {
  [Symbol.iterator]() {
    let n = 0;
    return { next: () => ++n < 3 ? { value: n, done: false } : { value: 'BYE', done: true } };
  },
};
console.log([...odd]);  // [1, 2] —— spread 丢弃 done:true 的 value
```

**评分点**：
- [Symbol.iterator] 每次调用返回新迭代器（可重复迭代）——核心
- done:true 时 value 被 for-of/spread 丢弃（仅手工 next 可见）
- 无限迭代器与 break 的必要性
- 迭代器协议的 {value, done} 完整性
