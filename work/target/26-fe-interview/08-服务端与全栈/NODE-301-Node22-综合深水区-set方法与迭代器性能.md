---
title: [NODE-301] Node 22 综合深水区：Set 方法与迭代器性能？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-301：Node 22 综合深水区：Set 方法与迭代器性能？
**答**:
- Set 原生方法（union/intersection/difference）在 V8 内建实现——比手写 filter+has 快（跳过 JS 层回调与临时数组），百万级集合运算可见提升。
- iterator helpers 惰性链：`.map().filter().take(n)` 单次遍历流式产出——对比 Array 链（每步全量物化）内存 O(k) vs O(n)。
- 适用边界：小数组（<1000）用 Array 更快（V8 优化充分）；大数据/流式/提前终止场景 helper 赢。
- 服务端应用：大日志/大用户集的筛选、权限集合运算（NODE-205）。

```javascript
// 性能对比心智
const big = Array.from({ length: 1e6 }, (_, i) => i);
// Array 链：3 次遍历 + 2 个中间数组
const r1 = big.filter(x => x % 2).map(x => x * 2).slice(0, 10);
// iterator：1 次遍历 + 流式
const r2 = big.values().filter(x => x % 2).map(x => x * 2).take(10).toArray();   // 提前终止
// Set 运算（V8 内建）
const a = new Set(big.slice(0, 5e5)), b = new Set(big.slice(2.5e5));
const inter = a.intersection(b);      // 内建：C++ 层遍历，快于 [...a].filter(x => b.has(x))
```
