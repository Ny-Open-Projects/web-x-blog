---
title: [1157] 检索管线的哪个参数对质量影响最大，怎么科学定位
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 敏感度]
type: 面试题
---

## 1157：检索管线的哪个参数对质量影响最大，怎么科学定位

**答**：
- 敏感度分析方法：对每个参数做「单变量扰动」（±20%/±50% 三档），跑评估集记录指标变化斜率；斜率最大的参数是敏感参数，优化优先级据此排序。
- 常见结论参考：top-k 与 rerank 阈值通常最敏感、chunk 大小其次、BM25 权重相对钝感（但精确词场景例外）——你的语料要实测，别抄结论。
- 敏感度数据的生产用途：参数变更的评审依据（动敏感参数要过全量评估，钝感参数可以快速放行）。
- 追问钩子：参数间交互效应怎么处理？——单变量扫描会漏交互（如 top-k 与 chunk 大小强耦合），敏感度初筛后对 top2 参数做小网格联合实验，两层方法配合。

```ts
const params = { topK: 5, chunkSize: 600, rerankCut: 0.4, bm25Weight: 1 };
const slopes = {};
for (const [k, v] of Object.entries(params)) {
  const pts = [v * 0.5, v, v * 1.5].map(async x => runEval(await withParam(k, x)));
  slopes[k] = await slope(pts);           // 指标随参数变化的斜率
}
const priority = Object.entries(slopes).sort((a, b) => b[1] - a[1]); // 敏感度排序
```
