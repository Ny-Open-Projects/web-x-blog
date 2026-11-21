---
title: [JS-058] Map 与 Object 有什么区别？什么场景用 Map？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-058：Map 与 Object 有什么区别？什么场景用 Map？

**答**：
- Map 的键可以是任意类型（对象、NaN、函数），Object 键只能是字符串/Symbol。
- Map 有 size、保持插入顺序、增删查为 O(1)，频繁增删性能更稳定。
- Map 可直接 for...of 遍历，Object 需要 Object.keys 转换。
- 键数量动态变化、需要顺序与频繁删除时选 Map；少量静态配置用 Object。

```javascript
const m = new Map();
const objKey = { id: 1 };
m.set(objKey, 'user object');
m.set(NaN, 'nan value');
m.set(1, 'number key');
console.log(m.get(objKey));  // user object
console.log(m.get(NaN));     // nan value，Map 内 NaN 相等
console.log(m.size);         // 3

for (const [k, v] of m) console.log(k, v); // 直接遍历

m.delete(1);
console.log(m.has(1));       // false

// 与对象互转见 JS-054；初始化传二维数组
const conf = new Map([['theme', 'dark'], ['lang', 'zh']]);
```
