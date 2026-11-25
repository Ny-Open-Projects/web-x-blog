---
title: [1184] 检索召回突然变差，排查清单怎么走
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 排查]
type: 面试题
---

## 1184：检索召回突然变差，排查清单怎么走

**答**：
- 排查五步有序走：① 基准测试（固定评估集跑分——先确认是真退化还是评估噪声）；② 数据面（索引版本/文档变更/分片健康——最近一次构建的 diff）；③ 模型面（embedding 服务版本漂移/降级——探针题验证）；④ 查询面（改写模块变更/分词异常——拿原始 query 直查）；⑤ 配置面（top-k/过滤/别名路由变更）。
- 排查纪律：每步「先排除后深入」，用固定基准集定位退化发生在哪一层，不做无方向的全链翻查。
- 时间线优先：把「变差的时间点」和各面变更时间线对齐，九成问题直接命中变更（改了什么，什么时候改的）。
- 追问钩子：五步都正常但还是差？——考虑「缓慢漂移」：语料增长稀释（新文档改变向量分布）、用户 query 分布漂移（新意图），这类要用分布对比而非单点排查。

```ts
async function recallDebug() {
  const base = await runEval(fixedSet);             // ① 基准
  if (base.acc > THRESHOLD) return '评估噪声';
  const timeline = await changeLog.recent();        // 变更时间线
  for (const face of ['index', 'model', 'query', 'config']) {
    const r = await probe(face, fixedSet);          // 分面探针
    if (r.degraded) return rootCause(face, timeline.intersect(face));
  }
  return '缓慢漂移：语料/query 分布对比';
}
```
