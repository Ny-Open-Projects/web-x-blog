---
title: [AGT-451] 笔试题——实现 RAG 上下文压缩策略路由（按问题类型选压缩法）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-451：手写压缩路由：事实型抽取/总结型摘要/全量型分治，忠实性校验兜底

**需求与边界**：
- 输入：query、召回块、token 预算；输出：压缩后上下文。
- 边界要求：① 问题类型分类（事实/总结/对比全量）决定策略；② 数字与实体压缩后必须原文保留（校验不过回退原文）；③ 分治 map-reduce 处理超预算全量；④ 单块超预算的截断保留首尾。

**答**：
```javascript
async function compressContext(query, docs, budget, { classify, extract,
  summarize, mapReduce }) {
  const total = tokens(docs);
  if (total <= budget) return { context: docs, strategy: 'none' };
  const type = await classify(query);       // fact/summary/full
  let out;
  if (type === 'fact') {
    out = await extract(docs, query);       // 只抽相关句
  } else if (type === 'summary') {
    out = await summarize(docs);            // 每块摘要
  } else {
    out = await mapReduce(docs, query);     // 全量：分治
  }
  // 忠实性校验：压缩前后数字/实体比对
  const before = extractNumsEntities(docs);
  const after = extractNumsEntities(out);
  const lost = [...before].filter(x => !after.has(x));
  if (lost.length && type === 'fact')
    return { context: docs, strategy: 'fallback_raw',  // 事实型丢失→回退原文
      warning: `数字/实体丢失: ${[...lost].slice(0, 3)}` };
  // 单块仍超预算：截断保留首尾
  return { context: out.map(d => tokens(d) > budget / docs.length
    ? headTail(d, budget / docs.length) : d),
    strategy: type, lost };
}
const headTail = (d, n) => {
  const half = Math.floor(n / 2);
  return { ...d, text: d.text.slice(0, half) + '\n[...]\n' +
    d.text.slice(-half) };                  // 首尾保留（尾部常含结论）
};
```

**评分点**:
- 三类问题路由三种压缩法（fact 抽取/summary 摘要/full 分治），策略与问题类型匹配。
- 忠实性校验：数字实体比对，事实型丢失直接回退原文（不硬上）。
- 超预算单块首尾截断（尾部结论保留）。
- warning 与 strategy 随返回（可观测）。
