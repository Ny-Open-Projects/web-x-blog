---
title: [SCN-739] 笔试题——实现 t-digest（近似分位数聚合）与跨粒度合并？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-739：手写简化 t-digest

**需求与边界**：
- 需求：流式插入数值，内存受限压缩质心；quantile(q) 近似分位数；merge(digests) 跨粒度合并（分钟→小时）。
- 边界：① 压缩误差可控（delta 参数控制质心数）；② 空digest quantile 返回 null；③ 合并保持近似精度。

**答**：
```javascript
class TDigest {
  constructor(delta = 100) { this.delta = delta; this.centroids = []; this.count = 0; }
  push(v, w = 1) {
    this.centroids.push({ mean: v, weight: w });
    this.count += w;
    if (this.centroids.length > this.delta * 2) this.compress();
  }
  compress() {
    this.centroids.sort((a, b) => a.mean - b.mean);
    const out = []; let sum = 0;
    for (const c of this.centroids) {
      sum += c.weight;
      const q = sum / this.count;
      // 分位数位置越靠中质心可越宽（k-size 缩放），尾部更细
      const kLimit = 4 * this.count * q * (1 - q) / this.delta;
      const last = out.at(-1);
      if (last && last.weight + c.weight <= kLimit) {   // 合并相邻质心
        last.mean = (last.mean * last.weight + c.mean * c.weight) / (last.weight + c.weight);
        last.weight += c.weight;
      } else out.push({ ...c });
    }
    this.centroids = out;
  }
  quantile(q) {
    if (!this.count) return null;
    this.centroids.sort((a, b) => a.mean - b.mean);
    let cum = 0;
    for (const c of this.centroids) {
      const w = c.weight;
      if (cum + w / 2 >= q * this.count) return c.mean;  // 质心中点覆盖目标分位
      cum += w;
    }
    return this.centroids.at(-1).mean;
  }
  static merge(digests) {                             // 跨粒度合并（无偏）
    const m = new TDigest(digests[0]?.delta ?? 100);
    for (const d of digests) for (const c of d.centroids) m.push(c.mean, c.weight);
    m.compress();
    return m;
  }
}
```

**评分点**:
- 质心压缩规则（中带宽大、尾带宽小）。
- merge 合并近似无偏（对比「分位数平均」的有偏）。
- quantile 边界（空/尾部）处理。
- compress 触发时机（数量超限）。
