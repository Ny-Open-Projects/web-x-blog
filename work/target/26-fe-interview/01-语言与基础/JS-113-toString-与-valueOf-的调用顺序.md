---
title: [JS-113] toString 与 valueOf 的调用顺序是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-113：toString 与 valueOf 的调用顺序是什么？

**答**：
- ToPrimitive 流程：先看 `Symbol.toPrimitive(hint)`；没有则按 hint 走——number 型先 valueOf 后 toString，string 型相反。
- 无 hint 的默认场景（`+`、`==`）：普通对象按 number 型顺序（先 valueOf）；Date 是特例，先 toString。
- valueOf 返回原始值即止；返回对象则继续调 toString；两者都返回对象才抛 TypeError。
- 记忆：`String(obj)`/模板串走 toString；`Number(obj)`/算术走 valueOf 优先。

```javascript
const obj = {
  valueOf()  { console.log('→ valueOf');  return 10; },
  toString() { console.log('→ toString'); return 'obj'; },
};

console.log(obj + 1);       // valueOf → 11（默认 hint，先 valueOf）
console.log(`${obj}`);      // toString → 'obj'（hint string）
console.log(String(obj));   // toString → 'obj'
console.log(Number(obj));   // valueOf → 10
console.log(obj == 10);     // valueOf → true
console.log(obj + '');      // valueOf → '10'（+ 默认仍是先 valueOf）

// Symbol.toPrimitive 优先级最高
const obj2 = {
  [Symbol.toPrimitive](hint) { return hint === 'string' ? 'str' : 'num'; },
  valueOf() { return 1; },
  toString() { return '2'; },
};
console.log(`${obj2}`, obj2 + 1); // str num

// Date 特例：默认 hint 先 toString
const d = new Date(0);
console.log(d + '');    // 'Thu Jan 01 1970 08:00:00 GMT+0800 ...'
console.log(Number(d)); // 0

// 都不返回原始值 → TypeError
const bad = { valueOf: () => ({}), toString: () => ({}) };
try { bad + 1; } catch (e) { console.log(e instanceof TypeError); } // true
```
