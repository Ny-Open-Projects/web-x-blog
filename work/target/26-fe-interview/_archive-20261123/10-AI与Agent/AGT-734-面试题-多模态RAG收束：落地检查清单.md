---
title: [AGT-734] 多模态 RAG 上线前的检查清单（解析/检索/生成/引用/成本）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-734：多模态 RAG 上线前的检查清单（解析/检索/生成/引用/成本）

**答**：
- 解析：质量门禁通过率（拒收率/人工复核积压）、图文一致性巡检基线建立；检索：三类 query（文本/图/混合）命中率验收、融合排序实验过；生成：预算分配压测（10 图上下文不爆）、降级链演练（vision 故障时服务可用）；引用：跨模态引用可跳转率、引用正确性抽检；成本：单次问答成本压到目标内、缓存命中率达标。
- 清单的本质是「每一段都有可量化的验收标准」，不达标不放大流量——多模态比纯文本多一倍的故障面，逐段验收比整体灰度更能定位问题。

```javascript
const MM_CHECKLIST = {
  ingest: { acceptRate: '>=0.85', patrolBaseline: true },
  retrieve: { hitRate: { text: 0.9, image: 0.8, mixed: 0.8 } },
  generate: { budgetStress: '10-img-ok', fallbackDrill: true },
  cite: { jumpRate: '>=0.95', citeAccuracy: '>=0.95' },
  cost: { perQueryUsd: '<=0.05', cacheHitRate: '>=0.7' },
};
function goNoGo(results) {
  return Object.entries(MM_CHECKLIST).every(([k, v]) =>
    meets(results[k], v));                          // 逐段验收
}
```

