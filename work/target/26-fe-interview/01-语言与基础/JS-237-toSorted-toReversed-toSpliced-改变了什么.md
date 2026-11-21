---
title: [JS-237] toSorted/toReversed/toSpliced/with 改变了什么
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-237：不可变数组方法（toSorted 系列）改变了什么

**答**：
- ES2023 四件套：toSorted / toReversed / toSpliced / with——返回新数组，原数组不动
- 替代的手写模式：[...arr].sort()、arr.slice().reverse()、复制后 splice——React/Vue 状态更新不再需要显式复制
- with(i, value)：不可变的「按下标替换」——以前 splice 是唯一选择（会变更原数组）
- 语义对齐：与 Redux 不可变更新、immutable 习惯完全一致，减少 [...arr] 样板
- 性能注意：仍会复制一份，超大数组高频调用时注意成本（TypedArray 也有对应方法）

```javascript
const arr = [3, 1, 2];
arr.toSorted();                       // [1, 2, 3]，arr 仍是 [3,1,2]
arr.with(0, 99);                      // [99, 1, 2]
arr.toSpliced(1, 1);                  // [3, 2]
// React 里的旧写法
setList(l => [...l].sort(cmp));       // 现在：setList(l => l.toSorted(cmp))
```
