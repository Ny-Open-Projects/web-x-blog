---
title: [HW-245] 手写一个 OT 变换性质验证器：TP1 与收敛性对拍
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-245：手写一个 OT 变换性质验证器：TP1 与收敛性对拍

**答**：
- 需求：实现 OTPropertyTest：随机生成操作序列（插入/删除、随机位置），对每对并发 op 断言 TP1（交换应用结果一致）；多客户端场景（3 客户端随机本地 op + 服务器仲裁）断言最终文档收敛一致；输出失败案例的操作序列（可复现）。
- 边界：随机位置不超过当前文本长度；删除长度不超过剩余文本；收敛断言在全部 op 广播完成后执行。
- 评分点：随机对拍框架；失败可复现（seed）；收敛判定。

```javascript
function otPropertyTest({ rounds = 1000, seed = 42 } = {}) {
  let rng = mulberry32(seed);                              // 可复现随机
  for (let r = 0; r < rounds; r++) {
    const doc = randomText(rng);
    const a = randomOp(doc, rng), b = randomOp(doc, rng);  // 并发双 op
    const { a1, b1 } = transform(a, b, rng() - 0.5);
    const docAB = applyOp(applyOp(doc, a), b1);
    const docBA = applyOp(applyOp(doc, b), a1);
    if (docAB !== docBA)
      return { pass: false, seed, round: r, doc, a, b, docAB, docBA };   // 失败可复现
  }
  return { pass: true };
}
function randomText(rng) { return Array.from({ length: 20 }, () =>
  String.fromCharCode(97 + Math.floor(rng() * 26))).join(''); }
function randomOp(doc, rng) {
  const pos = Math.floor(rng() * (doc.length + 1));
  if (rng() < 0.5) return { type: 'insert', pos, text: 'XY' };
  const len = 1 + Math.floor(rng() * Math.min(3, doc.length - pos));
  return { type: 'delete', pos, text: doc.slice(pos, pos + len) };
}
function mulberry32(seed) { return () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0;
  let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
  t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
```
