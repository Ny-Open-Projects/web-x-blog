---
title: [ALG-477] 手写数位 DP 与布隆/Bitmap 协同：大区间占用检测
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-477：手写数位 DP 与布隆/Bitmap 协同：大区间占用检测

**答**：
- 题目：号段占用检测——已分配号段存 Bitmap（1e9 位 = 125MB 太大）→ 分层：高位段 Bitmap（粗）+ 低位数位 DP 估算剩余。
- 思路：两层：高位 16 位用 Map<高16位, 低位 Bitmap 或计数>（活跃段才建）；查询「区间剩余」= 遍历覆盖的高位段，满段跳过、部分段逐位。与数位 DP 关系：部分段剩余可用数位 DP 快速估算（规则简单时）。
- 评分点：分层 Bitmap；满段跳过；精确 vs 估算的分级。

```javascript
class TieredBitmap {
  constructor({ highBits = 16, lowMax = 65535 } = {}) {
    this.high = highBits; this.lowMax = lowMax;
    this.segments = new Map();                              // 高位段 → {bitmap, used}
  }
  assign(id) {
    const hi = id >>> this.high, lo = id & this.lowMax;
    const seg = this.segments.get(hi) ?? this.segments.set(hi,
      { bitmap: new Uint8Array(this.lowMax + 1), used: 0 }).get(hi);
    if (!seg.bitmap[lo]) { seg.bitmap[lo] = 1; seg.used++; }
  }
  remainingInRange(lo, hi) {                                // 区间剩余（精确）
    let count = 0;
    const hiStart = lo >>> this.high, hiEnd = hi >>> this.high;
    for (let h = hiStart; h <= hiEnd; h++) {
      const seg = this.segments.get(h);
      const l = Math.max(lo & this.lowMax, h === hiStart ? lo & this.lowMax : 0);
      const r = Math.min(hi & this.lowMax, this.lowMax);
      if (!seg) { count += r - l + 1; continue; }           // 空段：全剩
      for (let i = l; i <= r; i++) if (!seg.bitmap[i]) count++;   // 精确扫（大段可数位 DP 估算）
    }
    return count;
  }
}
```
