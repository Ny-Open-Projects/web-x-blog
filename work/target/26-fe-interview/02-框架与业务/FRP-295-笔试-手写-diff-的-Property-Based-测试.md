---
title: [FRP-295] 笔试：手写 diff 的 property-based 测试生成器
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-295：笔试：手写 diff 的 property-based 测试
**答**：实现 `randomCase(seed, n)`：生成随机「旧列表/新列表」对（key 池有限、含增删乱序），对每对运行待测 diff，断言：1) 最终顺序等于新列表；2) 保留节点 DOM 引用不变（复用）；3) moves ≤ minimalMoves 理论值。跑 500 组。

```javascript
function mulberry32(seed) { return () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296 } }
function randomCase(rand) {
  const pool = ['a','b','c','d','e','f']
  const before = pool.filter(() => rand() > 0.4)
  const after = pool.filter(() => rand() > 0.4)
  if (rand() > 0.5) after.reverse()
  return [before, after]
}
function propertyTest(diffFn, rounds = 500) {
  const rand = mulberry32(42)
  for (let i = 0; i < rounds; i++) {
    const [before, after] = randomCase(rand)
    const { container, stats, nodeOf } = runDiff(diffFn, before, after)
    // 断言 1：最终顺序
    assert.deepEqual([...container.children].map(n => n.dataset.key), after)
    // 断言 2：复用引用
    before.filter(k => after.includes(k)).forEach(k => assert(nodeOf(k).reused, `key ${k} 未复用`))
    // 断言 3：移动上限
    assert(stats.moves <= minimalMoves(before, after))
  }
}
```
**评分点**：
- 可复现随机源（seed 固定，失败可重放）。
- 三条性质断言（顺序/复用/上限）覆盖 diff 语义。
- 有限 key 池逼迫复用与冲突场景。
- 能说明 property-based 与手写用例的互补（覆盖想象不到的组合）。
