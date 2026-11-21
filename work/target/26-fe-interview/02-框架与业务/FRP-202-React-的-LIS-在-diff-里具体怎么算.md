---
title: [FRP-202] React diff 里的最长递增子序列（LIS）具体怎么算？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-202：React diff 里 LIS 具体怎么算？
**答**：
- 数据：newChildren 中「可复用」的节点按新顺序排列，取它们在旧列表中的 index 序列 oldIndices。
- 目标：找出 oldIndices 的最长递增子序列——这些节点位置关系不变，无需移动。
- 算法：贪心 + 二分（patience sorting）：结果数组 seq 保持递增，每元素二分替换；前驱数组 prev 记录路径，回溯得到完整序列。
- 移动判定：newOrder 中不在 LIS 里的节点需要 insertBefore 移动。
- 复杂度 O(n log n)；Vue3 的 LIS 同算法，只是比较维度（新数组中旧索引）与 React 一致。
```javascript
// oldIndices = [2, 0, 3, 1] → LIS = [0, 1] (对应 index 0 与 1 的节点不动)
function lis(arr) {
  const res = [], prev = new Array(arr.length).fill(-1)
  arr.forEach((x, i) => {
    if (!res.length || arr[res[res.length - 1]] < x) { prev[i] = res[res.length - 1] ?? -1; res.push(i) }
    else {
      let lo = 0, hi = res.length - 1
      while (lo < hi) { const mid = (lo + hi) >> 1; arr[res[mid]] < x ? lo = mid + 1 : hi = mid }
      prev[i] = res[lo - 1] ?? -1
      res[lo] = i
    }
  })
  let cur = res[res.length - 1], out = []
  while (cur > -1) { out.unshift(arr[cur]); cur = prev[cur] }
  return out
}
```
