---
title: [JS-278] 输出题：TDZ 报错题
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 作用域]
type: 笔试题
---

## JS-278：输出题：TDZ 报错题

**题目**：判断各语句的输出/报错，并解释 TDZ 的边界（typeof 也会炸）。

**答**：
```javascript
// ① 函数体内访问外部未初始化的 let
const f = () => console.log(x);
// let x = 1;  // 若先 f() 后声明 → ReferenceError
// ② typeof 也逃不过 TDZ
// console.log(typeof y); let y = 2;  // ❌ ReferenceError（typeof 的安全保护失效）
// ③ 参数默认值引用后续参数
// function g(a = b, b = 1) {}        // g() ❌ ReferenceError：b 在默认值求值时处于 TDZ
// ④ 块级作用域内同名遮蔽
let z = 1;
{
  // console.log(z);  // ❌ ReferenceError——块内 z 的 TDZ，遮蔽外层
  let z = 2;
}
// ⑤ const 未赋值
// const c;  // ❌ SyntaxError（声明即必须初始化，编译期错误）

function safe() {
  let a = 1;
  return () => a;   // 闭包引用已初始化的 let：正常
}
```
```
核心：TDZ 从「块开始」到「声明语句执行」；typeof 对 let/const 不再安全；
函数默认值按从左到右求值，引用右侧参数即 TDZ。
```

**评分点**：
- typeof 在 TDZ 内也抛错（颠覆 typeof 安全直觉）——核心判分点
- 块内同名遮蔽导致外层变量也进 TDZ
- 参数默认值从左到右求值的引用限制
- 区分 SyntaxError（const 缺初始化）与 ReferenceError（TDZ 访问）
