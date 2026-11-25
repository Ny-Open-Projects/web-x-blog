---
title: [JS-057] structuredClone 与旧方案相比有什么优势？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-057：structuredClone 与旧方案相比有什么优势？

**答**：
- `structuredClone` 原生深拷贝，支持循环引用、Map/Set/Date/RegExp/ArrayBuffer。
- 不支持函数、DOM 节点、Symbol 键、原型链（拷贝后变成普通对象）。
- 对比 JSON.parse(JSON.stringify)：后者丢 undefined/function/Symbol、日期变字符串、无法处理循环引用。
- 对比递归手写：原生实现更快更完整，但“保留类实例”需求仍需手写或库。

```javascript
const original = {
  date: new Date(),
  map: new Map([['k', 1]]),
  nested: { deep: [1, 2] },
};
original.self = original; // 循环引用

const cloned = structuredClone(original);
console.log(cloned.date instanceof Date);  // true
console.log(cloned.map instanceof Map);    // true
console.log(cloned.self === cloned);       // true，循环引用保留

// JSON 方案会挂掉
try {
  JSON.parse(JSON.stringify(original));
} catch (e) {
  console.log(e.name); // TypeError，循环引用
}

// 原型丢失
class Box { constructor() { this.v = 1; } }
const bc = structuredClone(new Box());
console.log(bc instanceof Box); // false
```

## 追问（补充）

**追问**：

1. 拷贝 ArrayBuffer 是共享内存还是复制？ → 默认是复制；用 `{ transfer: [buf] }` 则转移所有权，源端的 buffer 立刻变成 detached、byteLength 归零。
2. 为什么类实例克隆后 `instanceof` 为 false？ → 算法只搬运可结构化克隆的数据，不复制原型链，结果的原型是 Object.prototype，方法全部丢失。
3. 项目不支持 structuredClone 又需要 Date/循环引用，怎么降级？ → 用 `MessageChannel` 的 postMessage 做同构克隆，或手写带类型分支和 WeakMap 去重的深拷贝。
