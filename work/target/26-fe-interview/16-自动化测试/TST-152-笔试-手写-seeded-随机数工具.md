---
title: [TST-152] 笔试：手写 seeded 随机数工具（测试随机逻辑的可控性）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-152：笔试：手写 seeded 随机数工具（测试随机逻辑的可控性）
**答**：
- 需求：实现 `createSeededRandom(seed)`——给定种子生成确定性的「随机」序列（mulberry32 算法，32 位 state），提供 `next()`（0~1 浮点）、`int(min,max)`（含两端）、`pick(arr)`（随机取元素）、`shuffle(arr)`（Fisher-Yates）。同种子序列完全一致，用于测试抽奖、AB 分流、随机排序等逻辑。
- 为什么不用 mock Math.random：mock 只能给定值序列，表达力差且影响全局；seeded random 在生产代码里也可用（重放线上问题），是「依赖注入随机源」的最佳实践。
- 边界：int(max) 边界包含；shuffle 不修改原数组（纯函数）；seed=0 也能工作（state 不能恒 0，mulberry32 里已处理）。

```javascript
function createSeededRandom(seed = 1) {
  let state = seed >>> 0 || 1;                     // 避免恒 0 死循环
  const next = () => {                             // mulberry32
    state |= 0; state = (state + 0x6D2B79F5) | 0;
    let t = Math.imul(state ^ (state >>> 15), 1 | state);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  return {
    next,
    int: (min, max) => min + Math.floor(next() * (max - min + 1)), // 含两端
    pick: (arr) => arr[Math.floor(next() * arr.length)],
    shuffle: (arr) => {                            // Fisher-Yates，不改原数组
      const a = [...arr];
      for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(next() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
      }
      return a;
    },
  };
}

// ---- 测试随机抽奖逻辑：同种子结果可复现 ----
const rng = createSeededRandom(42);
const lucky = [1, 2, 3, 4, 5].map(() => rng.int(1, 100));
expect(lucky).toEqual(createSeededRandom(42) && (() => {
  const r = createSeededRandom(42);
  return [1, 2, 3, 4, 5].map(() => r.int(1, 100));
})()); // 两同种子实例序列一致

// 边界验证
const r2 = createSeededRandom(7);
for (let i = 0; i < 1000; i++) {
  const v = r2.int(1, 6);
  expect(v).toBeGreaterThanOrEqual(1);
  expect(v).toBeLessThanOrEqual(6);                // 永不出界
}
```

**评分点**：
1. PRNG 实现确定性：同种子序列一致（核心语义）。
2. seed=0/负数不死循环（state 化处理）。
3. int 含两端、shuffle 纯函数不改原数组。
4. 能说出依赖注入随机源比 mock Math.random 更优（生产可重放）。
