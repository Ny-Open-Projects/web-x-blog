---
title: [ALG-466] 手写数位 DP 记忆化边界清理：查询间状态污染 bug
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-466：手写数位 DP 记忆化边界清理：查询间状态污染 bug

**答**：
- 题目：多次调用数位 DP（不同上界）共享 memo——tight=true 的状态被缓存后污染下次查询。经典 bug：记忆化 key 未含 tight。
- 思路：规则：tight=true 的分支绝不入 memo（每条 tight 路径唯一且依赖上界）；memo 按查询复用时确认状态不依赖上界。
- 评分点：tight 不缓存的铁律；跨查询 memo 共享的条件；debug 手段（小范围暴力对拍）。

```javascript
function createCounter() {                                 // 可复用的计数器（memo 跨查询）
  const memo = new Map();
  return function count(N) {
    const digits = String(N).split('').map(Number);
    function dfs(pos, mod, tight) {
      if (pos === digits.length) return mod === 0 ? 1 : 0;
      // ❌ 错误：if (memo.has(key)) return ...  不分 tight 一律缓存
      // ✅ 正确：tight=true 不缓存（依赖上界 N 的具体位）
      const key = pos * 8 + mod;
      if (!tight && memo.has(key)) return memo.get(key);
      const maxD = tight ? digits[pos] : 9;
      let total = 0;
      for (let d = 0; d <= maxD; d++)
        total += dfs(pos + 1, (mod + d) % 7, tight && d === maxD);
      if (!tight) memo.set(key, total);                    // 只缓存 tight=false
      return total;
    }
    return dfs(0, 0, true);
  };
}
// 若状态依赖「上界内容」以外的查询参数（如模数 m 变化）→ memo 也要按 m 分片
```
