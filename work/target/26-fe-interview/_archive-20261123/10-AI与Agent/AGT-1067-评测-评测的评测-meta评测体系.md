---
title: [1067] 「评测体系本身准不准」怎么评测
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 评测, meta]
type: 面试题
---

## 1067：「评测体系本身准不准」怎么评测

**答**：
- 评测体系的自检三问：判别力（能区分好坏版本吗？——好版本 vs 注入缺陷版本，分数应显著分化，分不开说明题目太弱）、稳定性（同配置重复跑分数方差小）、对齐性（评测分数与线上业务指标相关——评测涨线上也涨才是有效评测）。
- 判别力测试方法：定期做「退化实验」（故意注入已知缺陷：删掉重排/换弱模型），核心集分数应显著下降；不降的题目无判别力，淘汰或改写。
- 对齐性验证：评测分与线上代理指标（点踩率/完成率）做相关性分析，相关系数低说明评的不是业务关心的东西。
- 追问钩子：多久做一次 meta 评测？——季度一次判别力与稳定性；对齐性随线上数据积累持续算，相关性下降是评测体系老化的最早信号。

```ts
async function metaEval() {
  const normal = await runEval(core);
  const degraded = await runEval(core, { inject: 'remove_rerank' }); // 退化实验
  const sep = normal.acc - degraded.acc;
  if (sep < 0.03) return prune(weakItems(core, { normal, degraded })); // 无判别力题淘汰
  const corr = correlation(evalHistory, onlineProxyMetrics);
  if (corr < 0.4) return alert('评测与业务脱钩');
}
```
