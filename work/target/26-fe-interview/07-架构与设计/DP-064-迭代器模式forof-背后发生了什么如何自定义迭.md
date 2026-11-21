---
title: [DP-064] 迭代器模式：for-of 背后发生了什么？如何自定义迭代器？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-064：迭代器模式：for-of 背后发生了什么？如何自定义迭代器？（高频）
**答**：
- 迭代器协议：对象实现 `Symbol.iterator` 返回一个含 `next()` 的对象，`next()` 返回 `{ value, done }`。
- for-of/展开运算符/解构 都基于该协议——统一遍历接口，不关心内部结构（链表/树/懒序列都能被 for-of）。
- Generator 是迭代器的语法糖：`function*` 自动生成 `next()` 状态机，还能 `yield*` 委托。
- 前端应用：树结构遍历、分页惰性加载、无限流数据。

```javascript
// 1. 自定义迭代器：让普通对象支持 for-of
class Range {
  constructor(start, end) { this.start = start; this.end = end; }
  [Symbol.iterator]() {
    let cur = this.start;
    const end = this.end;
    return {
      next: () => (cur <= end ? { value: cur++, done: false } : { value: undefined, done: true }),
    };
  }
}
console.log([...new Range(1, 3)]); // [1, 2, 3] —— 展开运算符消费迭代器
for (const n of new Range(1, 3)) process.stdout.write(n + ' '); // 1 2 3
console.log();

// 2. Generator 等价实现：语法糖
function* rangeGen(start, end) {
  for (let i = start; i <= end; i++) yield i;
}
console.log([...rangeGen(1, 3)]); // [1, 2, 3]

// 3. 实战：树的深度优先遍历器 —— 复杂结构统一进 for-of
function* walkTree(node) {
  yield node.name;
  for (const child of node.children ?? []) yield* walkTree(child); // 委托递归
}
const tree = { name: 'src', children: [{ name: 'a.js' }, { name: 'components', children: [{ name: 'Btn.vue' }] }] };
console.log([...walkTree(tree)]); // ['src', 'a.js', 'components', 'Btn.vue']

// 4. 惰性序列：无限流按需取值（迭代器省内存的本质）
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) yield a, [a, b] = [b, a + b]; // 无限生成，不预计算
}
const fib = fibonacci();
console.log(fib.next().value, fib.next().value, fib.next().value); // 0 1 1
```
