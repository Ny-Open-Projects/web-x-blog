---
title: [AGT-219] Embedding 模型选型——领域向量模型怎么选与怎么评估？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-219：embedding 模型怎么选——通用模型不够用时怎么办？

**答**:
- 选型流程：先跑领域评测集（自建 100~300 条金标 query→文档对，算 recall@k）再选型，不要只看 MTEB 榜单——榜单是通用语料，你的领域（医疗/法律/代码）语义分布可能完全不同。
- 评估维度：效果（领域 recall）、维度与成本（维度越高存储越贵）、长度支持（长文档块需要 8k 上下文的 embedding）、多语言、推理延迟。
- 领域不够用的升级路径：加指令前缀（bge 系列的 query/instruction 前缀对效果影响大）、领域词表+查询扩展（改写层补救，成本最低）、对比学习微调（用业务正负样本对微调，几千条即可见效，成本中）。
- 换模型即全量重嵌入：embedding 空间不兼容，切换模型=重建索引+双跑灰度（新旧并行评测对比后切流）——所以选型要慎重，把切换成本写进决策。

```javascript
async function evalEmbedding(model, dataset) {
  let hit = 0;
  for (const { query, goldId } of dataset) {
    const qv = await embed(model, query);
    const docs = await vectorSearch(qv, { k: 10, model });
    if (docs.some(d => d.id === goldId)) hit++;
  }
  return hit / dataset.length;   // 领域 recall@10
}
// 双跑灰度：新旧模型并行索引 → 评测对比
// → 按流量比例切流 → 全量切换后下线旧索引
```
