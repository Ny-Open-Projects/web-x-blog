---
title: [FRP-012] diff 子节点时双端比较与最长递增子序列各起什么作用？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-012：diff 子节点时双端比较与最长递增子序列各起什么作用？

**答**：
- Vue2 用**双端比较**：新旧列表各拿头尾四个指针，四步匹配（旧头-新头、旧尾-新尾、旧头-新尾、旧尾-新头），能高效处理"列表反转/前插"这类常见变更，都失配时退化为按 key 查找。
- Vue3 改用"先 patch 同前缀/后缀，再对中间乱序部分建 key→index 映射"：算出**最长递增子序列（LIS）**，LIS 里的节点 DOM 不用动，只移动其余节点——移动次数最少。
- LIS 价值示例：`ABCDE → ABDEC`，LIS 是 `BDE`（或 ABE），只需移动 A 或 C，而不是全部重排。
- React 的简化策略是"单向从左到右遍历 + key Map 查找"，不做 LIS，靠 key 依然保证正确性（见 FRP-044）。

```javascript
// 简化实现，帮助理解最长递增子序列（Vue3 源码同款算法）
function getSequence(arr) {
  const p = arr.slice();       // p[i] 记录：第 i 项接在哪个下标后面
  const result = [0];          // result 存下标，贪心维护的递增序列
  let i, j, u, v, c;
  for (i = 0; i < arr.length; i++) {
    if (arr[i] === 0) continue;             // 新增节点（索引 -1）不参与
    j = result[result.length - 1];
    if (arr[j] < arr[i]) {                  // 大于队尾：直接追加
      p[i] = j;
      result.push(i);
      continue;
    }
    // 二分查找第一个 >= arr[i] 的位置并替换（贪心：让序列尾尽量小）
    u = 0; v = result.length - 1;
    while (u < v) {
      c = (u + v) >> 1;
      arr[result[c]] < arr[i] ? (u = c + 1) : (v = c);
    }
    if (arr[i] < arr[result[u]]) {
      if (u > 0) p[i] = result[u - 1];
      result[u] = i;
    }
  }
  // 回溯：从最后一项向前还原真正的最长递增子序列下标
  u = result.length; v = result[u - 1];
  while (u-- > 0) { result[u] = v; v = p[v]; }
  return result;
}

// diff 中的应用：newToOldIndex 数组，LIS 即"不需要移动的节点集合"
const newToOld = [5, 9, 3, 9, 10, 9, 4, 5, -1]; // -1 表示新增节点
console.log(getSequence(newToOld)); // [5, 6, 7] —— 位于 LIS 的节点 DOM 不动，其余做 insertBefore
```
