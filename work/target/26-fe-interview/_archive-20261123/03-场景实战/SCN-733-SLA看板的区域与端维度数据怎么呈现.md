---
title: [SCN-733] SLA 看板的区域/端/运营商维度怎么呈现？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-733：区域/端维度呈现怎么做？
**答**：
- 核心交叉维度：区域 × 端（PC/iOS/Android/H5）× 运营商——性能问题最常藏在交叉维度里（某省某运营商 CDN 节点劣化，大盘看不出）。
- 热力矩阵：区域 × 指标热力图，异常格子（偏离大盘 3σ）自动标红并支持点击下钻到该省该运营商明细。
- 小样本保护：低流量区域（如海外某国）样本少，显示置信区间与「样本不足」标注，不做硬性达标判断。
- 归因提示：区域劣化自动关联该区域最近变更（CDN 调度/机房变更）。
- 追问钩子：为什么大盘 P95 突涨要立刻看区域热力——大盘劣化多数是局部聚集（某区域/运营商/版本），区域热力是最快的二分定位手段。

```javascript
function regionHeat(rows) {                          // rows: [{region, isp, metric, p95, n}]
  const globalP95 = quantile(rows.flatMap(r => Array(Math.min(r.n, 100)).fill(r.p95)), 0.5);
  return rows.map(r => ({
    ...r,
    z: (r.p95 - globalP95) / Math.sqrt(globalP95),   // 偏离度
    flag: r.z > 3 && r.n > 1000 ? 'ABNORMAL' : r.n < 1000 ? 'LOW_SAMPLE' : 'OK',
  }));
}
```
