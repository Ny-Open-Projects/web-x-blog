---
title: [JS-263] 笔试：手写用 yield* 展平多层嵌套数组
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 生成器]
type: 笔试题
---

## JS-263：笔试：手写用 yield* 展平嵌套数组

**题目**：实现 `flat(arr, depth)` 生成器版深/浅展平：逐个产出叶子元素，depth 控制层级；要求流式产出（不构造中间数组）。

**答**：
```javascript
function* flat(arr, depth = 1) {
  for (const item of arr) {
    if (Array.isArray(item) && depth > 0) {
      yield* flat(item, depth - 1);   // 委托递归
    } else {
      yield item;
    }
  }
}
const nested = [1, [2, [3, [4]]], 5];
console.log([...flat(nested, 1)]);   // [1, 2, [3, [4]], 5]
console.log([...flat(nested, Infinity)]); // [1, 2, 3, 4, 5]

// 流式消费：不用等全量展开
for (const x of flat(nested, Infinity)) {
  if (x === 3) break; // 找到即停
}
```

**评分点**：
- yield* 委托递归是核心（不是递归 concat/递归展开数组）
- depth 语义与递减传递；Infinity 支持全展平
- 流式可中断消费（与 Array.prototype.flat 的 eager 区别）
- Array.isArray 判断（别用 typeof）
