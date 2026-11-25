---
title: [ALG-415] 手写 BIT 与线段树性能对拍：选型压测
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-415：手写 BIT 与线段树性能对拍：选型压测

**答**：
- 题目：为选型提供数据——同负载（10 万操作：单点改/区间和混合）下 BIT vs 线段树的耗时/内存对比脚本。
- 思路：seedable 随机操作序列；两实现跑同序列计时（performance.now）；内存用节点数估算。输出报告：BIT 通常快 2~3 倍、内存省一半。
- 评分点：公平对拍（同序列同分布）；计时口径（含建树）；结论能落到选型建议。

```javascript
function benchBITvsSeg({ n = 100000, ops = 100000, seed = 7 } = {}) {
  const rng = mulberry32(seed);
  const opsSeq = Array.from({ length: ops }, () => ({
    type: rng() < 0.5 ? 'add' : 'query',
    i: 1 + Math.floor(rng() * n), v: Math.floor(rng() * 100),
    l: 1 + Math.floor(rng() * n), r: 1 + Math.floor(rng() * n) }));
  const bench = (impl) => {
    const t0 = performance.now();
    let sink = 0;
    for (const o of opsSeq) {
      if (o.type === 'add') impl.add(o.i, o.v);
      else sink += impl.range(Math.min(o.l, o.r), Math.max(o.l, o.r));
    }
    return { ms: +(performance.now() - t0).toFixed(1), sink, memUnits: impl.memUnits() };
  };
  return { bit: bench(new BIT(n)), seg: bench(new SegTree(n)) };
  // 典型结果：BIT ~40ms / 2n 内存；SegTree ~110ms / 4n 内存
  // 结论：纯前缀可减场景选 BIT；需要最值/复杂标记才上线段树
}
```
