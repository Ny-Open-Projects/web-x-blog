---
title: [JS-280] 输出题：类型转换与 reduce 加法陷阱
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 类型]
type: 笔试题
---

## JS-280：输出题：类型转换与 reduce 陷阱

**题目**：判断 `[1,2,3].reduce(...)` 各种初始值形态的输出，并解释 reduce 无初始值时的行为。

**答**：
```javascript
// ① 无初始值：第一个元素作为 acc，从第二个开始迭代
[1, 2, 3].reduce((a, b) => a + b);        // 6

// ② 空数组无初始值 → TypeError！
// [].reduce((a, b) => a + b);            // ❌ Reduce of empty array

// ③ 带初始值的类型陷阱
['1', '2', '3'].reduce((a, b) => a + b, 0);  // "0123"（0+字符串=拼接）
['1', '2', '3'].reduce((a, b) => a + b);     // "123"

// ④ 混合类型
[1, 'a'].reduce((a, b) => a + b);            // '1a'
[{}, 'a'].reduce((a, b) => a + b);           // '[object Object]a'

// ⑤ reduceRight 与此相反
[1, 2, 3].reduceRight((a, b) => `${a}-${b}`); // '3-2-1'（acc 从最后一个开始）

// ⑥ 对象数组求和的正确姿势
const sum = [{ v: 1 }, { v: 2 }].reduce((a, b) => a + b.v, 0); // 3
```

**评分点**：
- 无初始值时 acc=首元素、跳过第一个——易错行为
- 空数组 + 无初始值的 TypeError（考边界）
- 字符串拼接陷阱（初始值 0 与字符串相遇）
- reduceRight 的方向语义
