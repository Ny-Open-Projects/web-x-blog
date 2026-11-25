---
title: [ALG-459] 手写数位 DP 与字符串边界（大数区间）：超长编号
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-459：手写数位 DP 与字符串边界（大数区间）：超长编号

**答**：
- 题目：编号超 Number.MAX_SAFE_INTEGER（如 19 位），区间端点以字符串给出——数位 DP 天然按位处理，不转 Number 即可。
- 思路：L/R 都用字符串；比较 L-1 的技巧：逐位减一借位；或用 BigInt 做 L-1/R 运算（BigInt 支持任意精度）。
- 评分点：避免 Number 精度丢失；BigInt 做端点减一；按位比较（字符串字典序对等长数字串成立）。

```javascript
function countInRangeBig(L, R, m = 13) {
  const bigSub1 = (s) => {                                  // 字符串减一
    const arr = s.split('').map(Number);
    let i = arr.length - 1;
    while (arr[i] === 0) arr[i--] = 9;
    arr[i]--;
    return arr.join('').replace(/^0+(?=.)|^(0+)$/ '$1') || '0';
  };
  const f = (N) => {                                        // [0, N] 能被 m 整除的个数
    const digits = N.split('').map(Number);
    const memo = new Map();
    function dfs(pos, rem, tight) {
      if (pos === digits.length) return rem === 0 ? 1 : 0;
      const key = pos * m + rem;
      if (!tight && memo.has(key)) return memo.get(key);
      const maxD = tight ? digits[pos] : 9;
      let total = 0;
      for (let d = 0; d <= maxD; d++)
        total += dfs(pos + 1, (rem * 10 + d) % m, tight && d === maxD);
      if (!tight) memo.set(key, total);
      return total;
    }
    return dfs(0, 0, true);
  };
  const L2 = BigInt(L) - 1n;
  return f(R) - f(L2.toString());                           // BigInt 端点处理
}
```
