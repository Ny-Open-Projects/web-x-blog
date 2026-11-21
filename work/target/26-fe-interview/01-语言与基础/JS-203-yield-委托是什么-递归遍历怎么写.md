---
title: [JS-203] yield* 委托是什么：递归遍历怎么写
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 生成器]
type: 面试题
---

## JS-203：yield* 委托是什么：递归遍历怎么写

**答**：
- yield* 把执行权委托给另一个可迭代对象/生成器——像「内联展开」，直到内层耗尽再回到外层
- 递归遍历树的标准姿势：每个节点 yield 自身值 + yield* 遍历子节点
- 返回值：yield* 表达式的值是「被委托迭代器的返回值」（done:true 时的 value）——可串联传递
- 常见坑：yield* 后面必须是可迭代对象，普通对象会 TypeError

```javascript
function* walk(tree) {
  yield tree.value;
  for (const child of tree.children ?? []) {
    const last = yield* walk(child); // 委托递归
  }
}
const tree = { value: 1, children: [{ value: 2, children: [{ value: 4 }] }, { value: 3 }] };
console.log([...walk(tree)]); // [1, 2, 4, 3] 深度优先
```
