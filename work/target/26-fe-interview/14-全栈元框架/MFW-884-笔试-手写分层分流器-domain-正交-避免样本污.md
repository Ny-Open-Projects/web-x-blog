---
title: [MFW-884] 笔试：手写分层分流器（domain 正交 + 避免样本污染）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-884：笔试：手写分层分流器（domain 正交 + 避免样本污染）

**答**：
- 结论：每个实验层有独立的 domain 与 salt，同一用户在不同正交层用不同哈希盐，保证分配独立不相关；层内按 key 稳定分桶。
- 关键：salt 隔离是正交性的核心——同一用户在不同层被独立分配，避免样本污染；分桶稳定（相同输入恒定）。
- 追问钩子：为什么要稳定哈希而不是随机？——随机会导致同一用户每次刷新变体不同，破坏体验一致性。

```javascript
function hash(s) { let h = 2166136261; for (const c of s) h = (h ^ c.charCodeAt(0)) * 16777619; return h >>> 0; }

function createLayeredBucketer(layers) {
  // layers: [{ name, domain, salt, buckets: { A:0.5, B:0.5 } }]
  return {
    assign(userId, layerName) {
      const layer = layers.find(l => l.name === layerName);
      if (!layer) throw new Error('unknown layer');
      const r = (hash(userId + ':' + layer.salt) % 1000) / 1000; // 独立盐
      let acc = 0;
      for (const [variant, p] of Object.entries(layer.buckets)) {
        acc += p;
        if (r < acc) return variant;
      }
      return Object.keys(layer.buckets)[0];
    }
  };
}
// 自测：跨层正交（独立盐），同层稳定
const b = createLayeredBucketer([
  { name: 'ui', domain: 'ui', salt: 's1', buckets: { A: .5, B: .5 } },
  { name: 'price', domain: 'price', salt: 's2', buckets: { A: .5, B: .5 } }
]);
console.log(b.assign('u1', 'ui') === b.assign('u1', 'ui')); // true（稳定）
```

**评分点**：
- 每层独立 salt 实现正交，避免跨层样本污染
- 按累积概率分桶，支持任意权重配置
- 稳定哈希保证同一用户变体恒定
- 边界：未知层抛错、权重不和为 1 的兜底（加分）
