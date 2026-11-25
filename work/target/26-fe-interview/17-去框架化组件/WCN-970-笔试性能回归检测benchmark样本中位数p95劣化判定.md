---
title: [WCN-970] 手写性能回归检测：对比两次 benchmark 样本判定是否显著劣化
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-970：手写性能回归检测：对比两次 benchmark 样本判定是否显著劣化

**题目**：实现 `detectRegression(before, after, { threshold = 0.1, minSamples = 5 } = {})`，before/after 为数值数组（同一次基准的多次采样，单位 ms）。要求：① 样本数不足 minSamples 时返回 `{ reliable:false, reason:'样本不足', ratio:null }`；② 计算两组中位数，ratio = (afterMedian - beforeMedian) / beforeMedian（beforeMedian 为 0 时按 1 处理）；③ ratio > threshold 判定 `regressed:true`，否则 false；④ 计算两组 p95（排序后取 95% 位置，向上取整索引），p95Ratio 同样规则；⑤ 返回 `{ reliable, regressed, ratio, p95Ratio, beforeMedian, afterMedian }`。请自足实现并给出可运行示例。

**答**：

```javascript
function detectRegression(before, after, { threshold = 0.1, minSamples = 5 } = {}) {
  if (!Array.isArray(before) || !Array.isArray(after) ||
      before.length < minSamples || after.length < minSamples) {
    return { reliable: false, reason: '样本不足', ratio: null };
  }
  const median = a => { const s = [...a].sort((x, y) => x - y), m = s.length >> 1;
    return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
  const p95 = a => { const s = [...a].sort((x, y) => x - y);
    return s[Math.ceil(s.length * 0.95) - 1]; };
  const bm = median(before), am = median(after);
  const base = bm || 1;
  const ratio = (am - bm) / base;
  const p95Ratio = (p95(after) - p95(before)) / base;
  return { reliable: true, regressed: ratio > threshold,
    ratio: +ratio.toFixed(3), p95Ratio: +p95Ratio.toFixed(3),
    beforeMedian: bm, afterMedian: am };
}
console.log(detectRegression([10,11,10,12,10], [15,16,15,17,15])); // regressed true
console.log(detectRegression([10,11], [15,16])); // 样本不足
```

**评分点**：
- 样本不足判定正确（含非数组健壮性）。
- 中位数计算正确（奇偶处理）。
- ratio 与 p95Ratio 公式正确（beforeMedian 为0按1）。
- regressed 阈值判定正确。
- 返回结构完整、示例可运行。
