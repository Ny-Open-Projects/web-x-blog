---
title: [BAS-129] 标签语句怎么配合 break 和 continue 使用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-129：标签语句怎么配合 break 和 continue 使用？
**答**：
- `label: statement` 给语句打标签，break label 一次性跳出整个标签块，continue label 直接进入标签所在外层循环的下一轮。
- 用于多层嵌套循环的精准跳出，避免用标志位层层判断；日常代码少用，面试考概念。

```javascript
outer:
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) continue outer;  // 跳过本轮内层，直接进入外层下一轮
    if (i === 2) break outer;     // 一次性跳出两层循环
    console.log(i, j);
  }
}
// 输出：0 0  1 0  然后中断
```
