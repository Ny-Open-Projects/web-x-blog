---
title: [HW-056] 手写 FlattenDeep
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-056：手写 FlattenDeep

**答**：
- 评分点：与 HW-023 的区分——这里聚焦**全深度展开**且重点是**迭代实现**（递归在超深嵌套如 10 万层会栈溢出，迭代版用显式栈）；注意展开顺序——递归版天然保序，栈版用 pop 要 reverse 或用索引指针；能对比 `flat(Infinity)` 原生行为；处理类数组 / 稀疏位是细节加分；说出复杂度 O(n)（n 为叶子总数，每个元素进出栈常数次）。

```javascript
// ===== 5 分钟速写版 =====
function flattenDeep(arr) {
  return arr.reduce((acc, v) =>
    acc.concat(Array.isArray(v) ? flattenDeep(v) : v), []); // 递归 reduce 一行流
}

// ===== 标准完整版（含边界处理：迭代防栈溢出）=====
function flattenDeepPro(arr) {
  if (!Array.isArray(arr)) throw new TypeError('arr must be an array');
  const stack = [...arr];       // 显式栈代替调用栈
  const result = [];
  while (stack.length) {
    const next = stack.pop();
    if (Array.isArray(next)) {
      // 倒序压栈，保证 pop 出来的顺序与原数组一致
      for (let i = next.length - 1; i >= 0; i--) stack.push(next[i]);
    } else {
      result.push(next);        // 稀疏空位在解构时已变 undefined，行为与 flat 对齐
    }
  }
  return result;
}
// 索引指针版（不复制原数组到栈，更省内存）：
function flattenDeepIndex(arr) {
  const result = [];
  const stack = [{ list: arr, index: 0 }]; // 帧：当前数组 + 读取位置
  while (stack.length) {
    const frame = stack[stack.length - 1];
    if (frame.index >= frame.list.length) { stack.pop(); continue; }
    const value = frame.list[frame.index++];
    if (Array.isArray(value)) stack.push({ list: value, index: 0 });
    else result.push(value);
  }
  return result;
}
// 压测对比（面试可口述）：
// const deep = []; let cur = deep; for (let i = 0; i < 100000; i++) { cur.push([]); cur = cur[0]; }
// 递归版 RangeError: Maximum call stack size exceeded；迭代版正常返回 []。
```

---
