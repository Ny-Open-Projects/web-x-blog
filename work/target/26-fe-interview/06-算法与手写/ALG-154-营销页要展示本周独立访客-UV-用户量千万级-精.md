---
title: [ALG-154] 营销页要展示"本周独立访客 UV"，用户量千万级，精确 Set 去重内存吃不消。HyperLogLog 的思想是什么？如何用 JS 演示？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-154：营销页要展示"本周独立访客 UV"，用户量千万级，精确 Set 去重内存吃不消。HyperLogLog 的思想是什么？如何用 JS 演示？
**答**：HLL 核心思想：hash 后的二进制里"前导零个数"越大越罕见，出现的最大前导零可粗估基数；把用户按 hash 前缀分成 m 个桶，各桶独立记录最大前导零，再取调和平均合并——随机性互相抵消，标准误差约 1.04/√m，KB 级内存估千万 UV。演示版用 `Math.clz32` 取前导零；真实实现需偏置校正与分段偏差修正。

```javascript
function hash32(s) {
  let h = 2166136261;
  for (const c of s) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619); }
  return h >>> 0;
}
class SimpleHLL {
  constructor(buckets = 64) { this.regs = new Array(buckets).fill(0); }
  add(id) {
    const h = hash32(String(id));
    const idx = h & (this.regs.length - 1);            // 低 6 位选桶
    const rest = h >>> 6;
    // 前导零个数：rest 为 0 时取满位宽
    const zeros = rest === 0 ? 26 : Math.clz32(rest) - 5;
    this.regs[idx] = Math.max(this.regs[idx], zeros);  // 每桶记最大前导零
  }
  count() { // 调和平均合并（真实实现另需偏置校正）
    const m = this.regs.length;
    const avg = this.regs.reduce((s, r) => s + Math.pow(2, -r), 0);
    return Math.round(0.79402 * m * m / avg);
  }
}
// 64 桶，KB 级内存估百万 UV，误差约 1.04/8 ≈ 13%
```
