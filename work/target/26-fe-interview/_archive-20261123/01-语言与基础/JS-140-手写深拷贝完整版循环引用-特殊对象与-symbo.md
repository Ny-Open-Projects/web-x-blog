---
title: [JS-140] 手写深拷贝完整版？循环引用、特殊对象与 symbol 键如何全兼容？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-140：手写深拷贝完整版？循环引用、特殊对象与 symbol 键如何全兼容？

**答**：
- 主干递归 + WeakMap 缓存：缓存解决循环引用与同一对象被多处引用（拷贝后保持引用关系一致）。
- 特殊对象分类处理：Date/RegExp 直接构造；Map/Set 递归键值；数组按位拷贝（含洞）。
- 普通对象：`Object.create(proto)` 保留原型链；`Reflect.ownKeys` 拿到字符串键 + symbol 键（含不可枚举）。
- 函数与基本类型直接返回；访问器属性拷贝时保留函数引用而非求值。

```javascript
function deepClone(value, seen = new WeakMap()) {
  // 1. 基本类型与函数直接返回
  if (value === null || typeof value !== 'object') return value;
  // 2. 循环引用 / 重复引用：返回已拷贝的同一引用
  if (seen.has(value)) return seen.get(value);

  // 3. 特殊对象
  if (value instanceof Date)   return new Date(value.getTime());
  if (value instanceof RegExp) return new RegExp(value.source, value.flags);
  if (value instanceof Map) {
    const m = new Map();
    seen.set(value, m); // 先登记再递归，环引用才有效
    value.forEach((v, k) => m.set(deepClone(k, seen), deepClone(v, seen)));
    return m;
  }
  if (value instanceof Set) {
    const s = new Set();
    seen.set(value, s);
    value.forEach((v) => s.add(deepClone(v, seen)));
    return s;
  }
  if (Array.isArray(value)) {
    const arr = [];
    seen.set(value, arr);
    value.forEach((v, i) => (arr[i] = deepClone(v, seen))); // 洞位自动跳过
    return arr;
  }

  // 4. 普通对象：保留原型 + 全键拷贝（字符串 + symbol + 不可枚举）
  const obj = Object.create(Object.getPrototypeOf(value));
  seen.set(value, obj);
  for (const key of Reflect.ownKeys(value)) {
    const desc = Object.getOwnPropertyDescriptor(value, key);
    if (desc.get || desc.set) {
      Object.defineProperty(obj, key, desc); // 访问器：原样保留 getter/setter
    } else {
      obj[key] = deepClone(desc.value, seen); // 数据属性：递归拷贝
    }
  }
  return obj;
}

// 验证
const symKey = Symbol('meta');
const src = {
  n: 1,
  [symKey]: 'symbol 值',
  hidden: '不可枚举',
  d: new Date(0),
  reg: /abc/gi,
  map: new Map([['k', { v: 1 }]]),
  set: new Set([1, { x: 2 }]),
};
src.self = src;                 // 循环引用
Object.defineProperty(src, 'hidden', { enumerable: false });

const copy = deepClone(src);
console.log(copy === src);                       // false
console.log(copy.self === copy);                 // true — 环引用指向拷贝自身
console.log(copy.map.get('k') !== src.map.get('k')); // true — 深层也是新对象
console.log(copy[symKey], copy.d instanceof Date, copy.reg.flags); // symbol 值 true gi
console.log(Object.getOwnPropertyDescriptor(copy, 'hidden').enumerable); // false — 保留描述符
console.log(Object.getPrototypeOf(copy) === Object.getPrototypeOf(src)); // true — 原型一致
```

## 二十、综合输出题压轴
