---
title: [ALG-465] 手写多约束数位 DP：双重规则编号
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-465：手写多约束数位 DP：双重规则编号

**答**：
- 题目：编号规则「不含 4 且 不含连续相同数字」双规则。状态 = (prev, started)（不含 4 是转移过滤不用占状态）。
- 思路：不含 4 → 填数时 d !== 4 过滤；连续相同 → prev 状态判断。两个规则一个是「值过滤」一个是「状态约束」——区分两类规则的实现方式。
- 评分点：值过滤 vs 状态约束的分类；状态设计只装必要的；多规则叠加的测试（对拍）。

```javascript
function countDoubleRule(N) {                              // 不含4 + 不连续相同
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, prev, started, tight) {
    if (pos === digits.length) return started ? 1 : 0;
    const key = pos * 220 + (prev + 1) * 2 + (tight ? 1 : 0) + (started ? 110 : 0);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      if (d === 4) continue;                               // 规则 1：值过滤
      if (started && d === prev) continue;                 // 规则 2：状态约束
      total += dfs(pos + 1, d, started || d > 0, tight && d === maxD);
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, -1, false, true);
}
// 测试：countDoubleRule 对拍暴力扫 [1, 1000] 逐一验证
```
