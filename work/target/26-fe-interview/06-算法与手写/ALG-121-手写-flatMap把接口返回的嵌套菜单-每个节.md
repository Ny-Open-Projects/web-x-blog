---
title: [ALG-121] 手写 flatMap：把接口返回的嵌套菜单（每个节点可能返回子项数组）拍平一层，且要支持指定展开深度？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-121：手写 flatMap：把接口返回的嵌套菜单（每个节点可能返回子项数组）拍平一层，且要支持指定展开深度？
**答**：flatMap = map 后再 flatten 一层（默认深度 1）。实现要点：回调返回数组才展开，返回非数组直接收集；递归参数传 `depth - 1` 控制深度；`depth: Infinity` 可全拍平。不展开 `null/undefined` 稀疏位。时间 O(n)，n 为展开后的元素总数。

```javascript
function flatMap(arr, fn, depth = 1) {
  const out = [];
  (function walk(list, d) {
    for (const item of list) {
      if (item == null) continue;             // 跳过稀疏位
      const mapped = fn(item);
      // 是数组且还有展开预算 => 递归展开；否则直接收集
      if (d > 0 && Array.isArray(mapped)) walk(mapped, d - 1);
      else out.push(mapped);
    }
  })(arr, depth);
  return out;
}
// 场景：菜单树拍一层做面包屑
// flatMap([1, 2], x => [x, x * 10]) => [1, 10, 2, 20]
// flatMap([1, [2, [3]]], x => x, Infinity) => [1, 2, 3]
```

## 十三、函数式与组合

> ALG-122 ~ ALG-128：compose/pipe、memoize、once、currying、debounce、throttle、deepEqual——前端数据管道与交互防抖节流的基本功。
