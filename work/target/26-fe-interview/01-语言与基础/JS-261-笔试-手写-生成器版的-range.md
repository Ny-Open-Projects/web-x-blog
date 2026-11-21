---
title: [JS-261] 笔试：手写生成器版的 range
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 生成器]
type: 笔试题
---

## JS-261：笔试：手写生成器版 range

**题目**：实现 `range(start, end, step)` 生成器：支持正负 step、step 为 0 抛错、开区间 [start, end)；要求可与 for-of/展开/解构配合。

**答**：
```javascript
function* range(start, end, step = start <= end ? 1 : -1) {
  if (step === 0) throw new RangeError('step 不能为 0');
  if (start <= end) {
    if (step <= 0) throw new RangeError('递增序列 step 应为正');
    for (let i = start; i < end; i += step) yield i;
  } else {
    if (step >= 0) throw new RangeError('递减序列 step 应为负');
    for (let i = start; i > end; i += step) yield i;
  }
}

// 用法
console.log([...range(0, 5)]);        // [0,1,2,3,4]
console.log([...range(5, 0)]);        // [5,4,3,2,1]
console.log([...range(0, 10, 3)]);    // [0,3,6,9]
for (const i of range(0, 3)) console.log(i);
```

**评分点**：
- step 符号与方向的一致性校验（增序负 step 是死循环）
- step=0 显式抛错
- 开区间边界（< end，不是 <=）
- 生成器自动支持 for-of（内建 Symbol.iterator）
