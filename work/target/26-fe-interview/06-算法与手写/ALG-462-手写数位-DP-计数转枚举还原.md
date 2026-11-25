---
title: [ALG-462] 手写数位 DP 计数转枚举还原：合法编号生成
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-462：手写数位 DP 计数转枚举还原：合法编号生成

**答**：
- 题目：按序生成「所有不含 4 的编号」第 start 个起的 k 个（分页拉取号码池）。Kth 生成 + 区间跳过。
- 思路：复用 ALG-461 的 kth 函数：起始 = kth(start)，后续逐次 kth(start+i)（或在上一个编号基础上「下一个合法数」——从编号+1 逐位找下一个无 4 的）。
- 评分点：kth 复用 vs「下一合法数」递推；批量生成的性能（缓存计数函数）；分页一致性。

```javascript
function* generateValidIds(start, k) {                     // 生成器：第 start 起共 k 个
  let current = kthWithoutFour(start);                     // 复用 ALG-461
  yield current;
  for (let i = 1; i < k; i++) {
    current = nextValid(current);                          // 下一合法数递推
    yield current;
  }
}
function nextValid(num) {                                  // 从 num 起下一个不含 4 的数
  let x = BigInt(num) + 1n;
  while (String(x).includes('4')) {                        // 朴素递推（数位 DP 可加速）
    // 含 4：跳到「4 所在位之后全 0」再继续——数位优化
    const idx = String(x).indexOf('4');
    const prefix = String(x).slice(0, idx);
    x = BigInt(prefix + '5' + '0'.repeat(String(x).length - idx - 1)) + 1n;
    x -= 1n;
    x += 1n;
    if (String(x).includes('4')) continue;                 // 进位后可能再含 4
  }
  return x.toString();
}
// 批量优化：计数函数 memo 全局共享，kth 调用 O(位数×10) 均摊
```
