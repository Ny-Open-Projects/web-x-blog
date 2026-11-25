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
      result.push(next);        // 注意：spread 已把空位变成 undefined，与 flat 不一致（flat 剔除空位）
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

## 补充：评分点与变体

**评分点**：

- 迭代版用显式栈时 pop 得到的是反序，必须压栈时逆序 push 或改成索引指针正向遍历，否则结果顺序整体颠倒
- 展开判据只用 `Array.isArray`，不展开 arguments 与类数组是合理取舍，但要主动说明这条边界
- 稀疏数组与 undefined 要明确策略：`flat` 会**剔除**空位（`[1,,3].flat()` → `[1,3]`）、`map` 保留空位但不调用回调、`[...arr]` 把空位变成 undefined，三者行为都不同，混用会埋坑
- 复杂度 O(n)（n 为叶子总数，每元素进出栈常数次），递归版深度受调用栈限制约一万层

**变体与延伸**：

1. 十万层嵌套如何不爆栈 → 迭代加显式栈，JS 没有尾调用优化，只能靠迭代而非递归改写
2. 要同时展开类数组 → 用 Array.from 归一化，或把判据放宽到带 length 的对象并处理字符串误判
3. 要求不改原数组 → 新建结果数组，元素仍是引用（浅拷贝），嵌套其中的对象不会被复制
