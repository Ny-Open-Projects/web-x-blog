---
title: [ALG-104] 权限系统用二进制位存储权限（READ=1、WRITE=2、DELETE=4、ADMIN=8），用户态是一个整数。如何统计用户拥有几项权限、如何判断有无某权限？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-104：权限系统用二进制位存储权限（READ=1、WRITE=2、DELETE=4、ADMIN=8），用户态是一个整数。如何统计用户拥有几项权限、如何判断有无某权限？
**答**：统计二进制中 1 的个数用 Brian Kernighan 算法：`n &= n - 1` 每次消掉最低位的 1，循环次数恰好等于 1 的个数，比逐位右移快（只循环 k 次，k 为 1 的个数）。判断权限用按位与：`perm & MASK` 非 0 即有。复杂度 O(k)。

```javascript
function countBits(n) {
  let c = 0;
  while (n) { n &= n - 1; c++; } // 每次消掉最低位的 1
  return c;
}
const READ = 1 << 0, WRITE = 1 << 1, DELETE = 1 << 2, ADMIN = 1 << 3;
const userPerm = READ | ADMIN;             // 二进制 1001
console.log(countBits(userPerm));          // 2 项权限
console.log(Boolean(userPerm & WRITE));    // false，无写权限
console.log(Boolean(userPerm & (READ | ADMIN))); // 掩码组合判断：true
// 撤销权限用清位：userPerm &= ~WRITE（WRITE 不在时无损）
```
