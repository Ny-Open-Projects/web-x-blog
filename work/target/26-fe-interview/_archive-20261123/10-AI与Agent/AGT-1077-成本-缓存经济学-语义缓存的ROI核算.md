---
title: [1077] 语义缓存值不值得上，怎么算 ROI
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 成本延迟, 缓存]
type: 面试题
---

## 1077：语义缓存值不值得上，怎么算 ROI

**答**：
- ROI 公式：节省 = 命中率 × 平均查询成本 - 缓存成本（存储 + 误命中的业务损失）；误命中风险是主变量——语义缓存答错一次的代价（用户信任）可能大于省的一毛钱。
- 收益边界：命中率取决于 query 分布的重复度；客服 FAQ 类重复度高（30%+ 命中率常见），开放对话类几乎无重复，不值得上。
- 折中方案：语义缓存只缓存「验证过的高置信答案」（评估分数 > 阈值的）+ TTL 短 + 严格阈值，把误命中压到可忽略。
- 追问钩子：为什么语义缓存的高命中率场景反而危险？——高频问题往往是「敏感问题」（价格、政策），缓存过期几分钟就可能给出过时答案，这类 query 要进「禁缓存清单」。

```ts
const NO_CACHE = ['price', 'policy', 'quota'];        // 敏感意图禁缓存
async function semanticCache(q, vec) {
  if (NO_CACHE.includes(intentOf(q))) return miss();
  const hit = await vecCache.nn(vec, { threshold: 0.95, verifiedOnly: true });
  if (hit) { metrics.hit(); return hit.answer; }
  metrics.miss(); return miss();
}
```

