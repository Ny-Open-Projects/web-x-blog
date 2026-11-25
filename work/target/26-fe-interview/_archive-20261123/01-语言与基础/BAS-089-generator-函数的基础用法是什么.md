---
title: [BAS-089] generator 函数的基础用法是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-089：generator 函数的基础用法是什么？
**答**：
- function* 声明，调用后不立即执行而是返回迭代器；每次 next() 执行到下一个 yield 暂停并交出值。
- yield 可双向传值：next(x) 的 x 成为上一个 yield 表达式的返回值；实现 Symbol.iterator 后天然支持 for...of。
- 典型用途：惰性/无限序列、状态机；async/await 可视为 generator + 自动执行器演化来的语法糖。

```javascript
function* fib() {
  let [a, b] = [0, 1];
  while (true) { yield a; [a, b] = [b, a + b]; }  // 无限惰性序列
}
const it = fib();
console.log(it.next().value); // 0
console.log(it.next().value); // 1
console.log(it.next().value); // 1
console.log(it.next().value); // 2
```
