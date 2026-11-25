---
title: [MFW-883] A/B 实验里怎么避免辛普森悖论误导结论
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-883：A/B 实验里怎么避免辛普森悖论误导结论

**答**：
- 结论：辛普森悖论指分组看都提升、合并看却下降，源于样本结构不均；做法是分层随机（按重要维度分层）而非全局随机，保证各组结构可比。
- 落地：按设备/地区/新老用户等维度分层，在每层内独立随机分流；分析时既看总体也看分层结果。
- 追问钩子：为什么全局随机也可能导致结构不均？——小样本或流量波动下，各维度比例在两组间可能偶然失衡。

```javascript
// 分层随机：在层内分桶，保证结构可比
function stratifiedAssign(user, layers, salt) {
  const key = layers.map(l => l + ':' + user[l]).join('|'); // 层内 key
  return hash(key + salt) % 100 < 50 ? 'A' : 'B';
}
// 若只按 userId 全局随机，某些层（如设备）在两组比例可能失衡 → 悖论
function globalAssign(user, salt) { return hash(user.id + salt) % 100 < 50 ? 'A' : 'B'; }
// 分析：既看总体指标，也按层拆解验证一致性
function analyze(resultsByLayer) {
  const overall = { A: 0, B: 0, nA: 0, nB: 0 };
  for (const layer of Object.values(resultsByLayer)) {
    overall.A += layer.A; overall.nA += layer.nA;
    overall.B += layer.B; overall.nB += layer.nB;
  }
  return {
    overallLift: overall.B / overall.nB - overall.A / overall.nA,
    perLayer: Object.fromEntries(Object.entries(resultsByLayer).map(
      ([k, v]) => [k, v.B / v.nB - v.A / v.nA]))
  };
}
// 若 overallLift 与 perLayer 符号相反 → 警惕辛普森悖论，查分层结构
```
