---
title: [AGT-473] 笔试题——实现实验分流一致性（同用户同版本+多实验正交）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-473：手写分流服务：稳定分桶、多实验正交、互斥实验组、流量窃取防护

**需求与边界**：
- 输入：用户 id、实验配置列表（含互斥域）；输出：各实验的分组。
- 边界要求：① 同用户同实验稳定同组（hash 种子=实验 id）；② 多实验正交（不同实验的 hash 域独立，不相关干扰）；③ 同域互斥实验（用户只能进一个）；④ 分组比例精确（按配置权重）。

**答**：
```javascript
function assignExperiments(userId, experiments) {
  const result = {};
  const domainTaken = new Map();               // 互斥域占用
  for (const exp of experiments) {
    // 1. 互斥域：已占用则跳过
    if (exp.domain && domainTaken.has(exp.domain)) {
      result[exp.id] = { group: 'none',
        reason: 'domain_conflict' };
      continue;
    }
    // 2. 稳定分桶：hash 种子含实验 id（正交）
    const h = hash(`${exp.id}:${userId}`) % 10000 / 10000;
    let acc = 0, group = 'control';
    for (const g of exp.groups) {              // [{id, weight}]
      acc += g.weight;
      if (h < acc) { group = g.id; break; }
    }
    result[exp.id] = { group, bucket: h };
    if (exp.domain && group !== 'control')
      domainTaken.set(exp.domain, exp.id);
  }
  return result;
}
// 正交原理：hash 种子含实验 id → 同用户在不同实验的
// 分桶相互独立（不相关）；
// 互斥域（如 checkout 流程实验）：进 A 就不能进 B，
// 控制组不占域（可进其他实验）。
// 分组比例：权重累加区间匹配，10000 精度。
```

**评分点**:
- hash 种子含实验 id 实现正交（不同实验独立不干扰）。
- 互斥域机制（控制组不占域，实验组独占）。
- 权重累加分桶保证比例精确，同用户稳定同组。
- 互斥冲突显式返回 reason（可观测）。
