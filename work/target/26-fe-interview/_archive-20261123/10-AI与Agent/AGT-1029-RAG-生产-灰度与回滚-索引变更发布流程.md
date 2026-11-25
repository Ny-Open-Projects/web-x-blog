---
title: [1029] RAG 索引策略变更（分块/模型）怎么灰度上线
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 发布]
type: 面试题
---

## 1029：RAG 索引策略变更（分块/模型）怎么灰度上线

**答**：
- 索引变更风险高于代码变更：影响所有查询的召回分布，必须灰度；方案是「双索引别名」——新旧索引并存，按流量比例或租户灰度路由。
- 灰度观察指标：检索命中率、拒答率、答案质量抽检、查询延迟（新索引分片数变化会改变延迟）；观察期至少一周（覆盖周内流量波动）。
- 回滚预案：别名切回即回滚，秒级生效；新索引写入继续双写，保证回滚后数据不缺。
- 追问钩子：灰度期间新旧索引的评估分数怎么看？——同一评估集分别跑双索引出对比报告，灰度流量的线上指标做交叉验证，两边都过才全量。

```ts
async function rolloutIndex(newIdx, { percent = 10 }) {
  await aliasCreate(newIdx + '-canary', newIdx);   // 灰度别名
  router.setRule(q => hash(q.userId) % 100 < percent ? 'canary' : 'stable');
  // 观察一周，达标后逐步 10 -> 50 -> 100，别名原子切换
  metrics.watch(['retrieval_hit', 'reject_rate', 'latency_p95'], { alert: true });
}
```
