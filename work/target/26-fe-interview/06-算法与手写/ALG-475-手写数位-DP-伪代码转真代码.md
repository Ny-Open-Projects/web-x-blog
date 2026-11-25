---
title: [ALG-475] 手写数位 DP 伪代码转真代码：模板填空
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-475：手写数位 DP 伪代码转真代码：模板填空

**答**：
- 题目：给出数位 DP 通用模板伪代码，要求填空补全「状态定义/转移/终态/记忆化边界」四处。考察模板的完整理解。
- 要点：四处填空——① 状态（pos + 业务状态 + tight + started）；② 转移（枚举 0..maxD，业务过滤与状态转移）；③ 终态（started 与业务判定）；④ 记忆化（只缓存 tight=false）。
- 评分点：四处全部正确；能指出模板的「规则注入点」；空串/前导零处理。

```javascript
function digitDPTemplate(N, rule) {                        // 通用模板（四处标注）
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, state, tight, started) {
    // ① 状态定义：pos 位指针 + rule 提供的业务状态 + tight + started（前导零）
    if (pos === digits.length)
      return started && rule.accept(state) ? 1 : 0;        // ③ 终态：started 且业务判定
    const key = `${pos}|${rule.stateKey(state)}|${tight ? 1 : 0}|${started ? 1 : 0}`;
    if (!tight && memo.has(key)) return memo.get(key);     // ④ 记忆化：只存非 tight
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {                      // ② 转移：枚举 0..maxD
      if (!rule.canTake(state, d, started)) continue;      //    业务过滤（如禁 4）
      total += dfs(pos + 1, rule.transition(state, d, started),
        tight && d === maxD, started || d > 0);
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, rule.init(), true, false);
}
// rule 示例：{ init: () => ({mod: 0}), canTake: (s, d) => d !== 4,
//   transition: (s, d) => ({mod: (s.mod * 10 + d) % 7}), accept: s => s.mod === 0 }
```
