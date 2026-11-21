---
title: [JS-306] 输出题：yield* 的返回值
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 生成器]
type: 笔试题
---

## JS-306：输出题：yield* 的返回值

**题目**：yield* 表达式的值是什么？内层生成器 return 的值如何传递与回收。

**答**：
```javascript
function* inner() {
  yield 'a';
  yield 'b';
  return 'INNER-DONE';   // return 值只能被 yield* 捕获
}
function* outer() {
  const result = yield* inner();  // 委托完，result = 内层 return 值
  yield 'outer got: ' + result;
}
const g = outer();
g.next(); // { value: 'a', done: false }
g.next(); // { value: 'b', done: false }
g.next(); // { value: 'outer got: INNER-DONE', done: false }

// 对普通可迭代对象委托：yield* 的值为 undefined（迭代器无 return 语义）
function* overArr() {
  const r = yield* [1, 2];   // r === undefined
  yield r;
}
console.log([...overArr()]); // [1, 2, undefined]

// 递归收集 return 值：树遍历汇总的经典用法
function* sumTree(node) {
  let total = 0;
  for (const c of node.children ?? []) total += yield* sumTree(c);
  yield node.v;
  return total + node.v;
}
```

**评分点**：
- yield* 捕获内层 return 值（生成器委托）——核心
- 对普通可迭代委托时返回 undefined（无 return 语义）
- 外层「看不到」内层 return 除非用 yield* 接收
- 树遍历汇总的递归应用（加分）
