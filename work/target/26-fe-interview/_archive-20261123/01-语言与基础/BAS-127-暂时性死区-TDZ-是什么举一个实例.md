---
title: [BAS-127] 暂时性死区（TDZ）是什么？举一个实例。
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-127：暂时性死区（TDZ）是什么？举一个实例。
**答**：
- let/const 变量从"块级作用域开始"到"声明语句执行完"之间是死区，访问即抛 ReferenceError，而不是得到 undefined。
- `typeof` 也不再安全：对死区中的变量做 typeof 同样报错，这与未声明变量返回 'undefined' 不同。
- 本质是 let/const 用"先声明后访问"的强约束替代 var 的静默提升。

```javascript
{
  // 死区从块首开始，到 let x 这一行结束
  console.log(x);  // ReferenceError，不是 undefined
  let x = 1;
}
console.log(typeof undeclaredVar); // 'undefined'：未声明的变量 typeof 安全
console.log(typeof y);             // ReferenceError：死区内的变量 typeof 也不放过
let y;
```
