---
title: [ALG-479] 手写数位 DP 调试技巧：小规模对拍
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-479：手写数位 DP 调试技巧：小规模对拍

**答**：
- 题目：数位 DP 的对拍调试方法论——小范围暴力逐数校验 + 状态 dump + 边界用例清单。
- 思路：① 对拍：暴力 [1, 1000] 逐数 rule(x) 累计对比 DP 结果；② 状态 dump：打印 memo 条目核对状态语义；③ 边界用例：L=R、L-1=0、全 9 数、含 0 前缀。
- 评分点：对拍框架；常见 bug 清单（tight 缓存/前导零/边界）；调试效率。

```javascript
function digitDPDebug(rule, testRange = 1000) {            // 对拍调试器
  const brute = (N) => { let c = 0;
    for (let x = 1; x <= N; x++) if (rule.check(x)) c++;
    return c; };
  const dp = createCounter(rule);                           // 复用模板（ALG-475）
  const mismatches = [];
  for (const n of [1, 9, 10, 99, 100, 999, testRange]) {    // 边界用例集
    const b = brute(n), d = dp(n);
    if (b !== d) mismatches.push({ n, brute: b, dp: d });
  }
  if (mismatches.length)
    console.error('数位 DP 不一致:', mismatches,
      '常见原因: tight 被缓存 / 前导零计数 / 终态漏 started');
  return { pass: mismatches.length === 0, mismatches };
}
// 常见 bug 清单：
// 1. tight=true 状态入 memo → 跨查询污染（ALG-466）
// 2. started 漏判 → 全零串被计数
// 3. 区间差 f(R) - f(L-1) 的 L-1 用 Number 精度丢失（ALG-459）
// 4. 状态 key 序列化不一致（对象 key 顺序）
```
