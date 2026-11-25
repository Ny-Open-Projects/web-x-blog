---
title: [HW-333] 手写一个 A/B 分流引擎：分桶哈希与互斥实验组
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-333：手写一个 A/B 分流引擎：分桶哈希与互斥实验组

**答**：
- 需求：实现 ABEngine：实验 {key, variants: [{name, weight}], layer}；assign(uid, expKey) 分桶（哈希到 0~9999 区间按权重切分）；分层互斥（同 layer 实验共享流量空间，不同层独立——哈希盐含 layer）；曝光与转化配对上报。
- 边界：权重和不必为 1（归一化）；同实验同一 uid 恒同组（盐稳定）；互斥层实现（layer 前缀哈希 + 层内剩余流量均匀）。
- 评分点：权重切分；分层盐；配对上报。

```javascript
class ABEngine {
  constructor(experiments, layers) { this.exps = new Map(experiments.map(e => [e.key, e]));
    this.layers = layers; }                                   // layers: {layer1: ['expA','expB']}
  assign(uid, expKey) {
    const exp = this.exps.get(expKey);
    const layer = exp.layer ?? 'default';
    const layerExps = this.layers[layer] ?? [expKey];
    const layerShare = Math.floor(10000 / layerExps.length);  // 层内均分流量空间
    const space = hashStr(uid + layer) % 10000;               // 层级哈希定空间
    const mySpace = layerExps.indexOf(expKey);
    if (space < mySpace * layerShare || space >= (mySpace + 1) * layerShare)
      return null;                                            // 不在本实验流量空间（互斥）
    const inSpace = space - mySpace * layerShare;
    const total = exp.variants.reduce((s, v) => s + v.weight, 0);
    let acc = 0;
    for (const v of exp.variants) {                           // 权重切分
      acc += v.weight / total * layerShare;
      if (inSpace < acc) return v.name;
    }
    return exp.variants.at(-1)?.name ?? null;
  }
  expose(uid, expKey, variant) { track('ab-expose', { uid, expKey, variant, eid: expKey + ':' + uid }); }
  convert(uid, expKey, metric) { track('ab-convert', { uid, expKey, metric }); }   // 与曝光配对分析
}
function hashStr(s) { let h = 2166136261; for (const c of s) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619); } return h >>> 0; }
```
