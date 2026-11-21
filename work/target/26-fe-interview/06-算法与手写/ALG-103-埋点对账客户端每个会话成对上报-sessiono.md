---
title: [ALG-103] 埋点对账：客户端每个会话成对上报 session_open / session_close，某个会话漏报导致它只出现一次。所有 id 都成对出现、只有一个落单，如何 O(n) 时间 O(1) 空间找出它？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-103：埋点对账：客户端每个会话成对上报 session_open / session_close，某个会话漏报导致它只出现一次。所有 id 都成对出现、只有一个落单，如何 O(n) 时间 O(1) 空间找出它？
**答**：异或。`a ^ a = 0` 且异或满足交换律，成对的 id 相互抵消为 0，最后只剩落单者。若扩展为"两个都落单"，全体异或得到 `a ^ b`，取其任意为 1 的位（`x & -x`）把集合分成两组再各异或一次即可。时间 O(n)，空间 O(1)，无需排序或哈希表。

```javascript
function findUnpaired(ids) {
  let x = 0;
  for (const id of ids) x ^= id; // 成对抵消，剩下奇数次的那个
  return x;
}
// 扩展：两个会话都落单
function findTwoUnpaired(ids) {
  let x = 0;
  for (const id of ids) x ^= id;      // x = a ^ b
  const low = x & -x;                  // 取最低不同的位，按它把集合分成两组
  let a = 0, b = 0;
  for (const id of ids) (id & low ? (a ^= id) : (b ^= id));
  return [a, b];
}
// findUnpaired([101, 102, 101, 102, 103]) => 103
```
