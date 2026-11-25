---
title: [WCN-509] 大促容量评估：百万 QV 页面下，元素 chunk 的 CDN 命中率与降级策略怎么算？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-509：大促容量评估：百万 QV 页面下，元素 chunk 的 CDN 命中率与降级策略怎么算？

**答**：
- 结论：命中率取决于「产物版本收敛度」——版本越集中、长尾越少，命中率越高。
- 估算：按 tag+版本维度统计 PV 分布，命中率 ≈ Σ(高频版本 PV)/总 PV，长尾版本走回源。
- 降级链：CDN  miss → 边缘缓存 → 源站 → 内置兜底实现（保底可交互，即使最新 chunk 不可用）。
- 追问：大促前如何人为收敛版本？（答：冻结发布 + 强制全量到统一版本）

```javascript
function cdnHitRate(pvByVersion) {
  const total = Object.values(pvByVersion).reduce((a, b) => a + b, 0);
  const top = Object.values(pvByVersion).sort((a,b)=>b-a).slice(0, 3).reduce((a,b)=>a+b, 0);
  return { hitRate: +(top / total).toFixed(3), tailVersions: Object.keys(pvByVersion).length - 3 };
}
const pv = { 'v3.1.0': 800000, 'v3.0.9': 120000, 'v3.0.8': 50000, 'v2.9.0': 30000 };
// => hitRate 0.97, 但有 1 个长尾版本要回源

// 大促兜底：最新 chunk 不可用时回退到已验证版本
const FALLBACK = 'v3.0.9';
```
