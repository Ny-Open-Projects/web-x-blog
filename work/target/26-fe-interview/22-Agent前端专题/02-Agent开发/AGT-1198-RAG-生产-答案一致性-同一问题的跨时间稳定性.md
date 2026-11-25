---
title: [1198] 同一问题隔一周问两次，答案不一样怎么办
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 一致性]
type: 面试题
---

## 1198：同一问题隔一周问两次，答案不一样怎么办

**答**：
- 不一致的来源排序：知识库变更（文档更新——正当变更要保留）、检索抖动（top-k 边界分数接近，命中集合变化）、生成随机性（采样温度）、缓存与动态路径混用（一半走缓存一半走管线）。
- 治理分层：正当变更——答案带「依据版本与时间」，变化可解释；抖动——top-k 边界加平滑（分数带内保持上次命中集）；随机——温度调低 + 答案结构稳定（模板化骨架）。
- 一致性监控：抽样固定 query 集每日重放，答案相似度低于阈值告警——「稳定性」作为独立指标与准确性并列。
- 追问钩子：一致性和准确性冲突时（知识更新了）怎么办？——准确性优先，但变化必须「显式可解释」（答案标注更新原因），静默变化伤信任，一致但错误更伤。

```ts
const consistencySet = loadFixedQueries(50);
async function nightlyStability() {
  for (const q of consistencySet) {
    const [a1, a2] = [await cachedAnswer(q), await lastWeek(q)];
    const sim = await semanticSim(a1, a2);
    if (sim < 0.9 && !justifiesChange(q)) {
      alert('answer drift', { q, sim });            // 无正当理由的变化告警
    }
  }
}
```

