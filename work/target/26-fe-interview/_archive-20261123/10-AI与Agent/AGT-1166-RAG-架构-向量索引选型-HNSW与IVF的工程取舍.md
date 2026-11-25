---
title: [1166] HNSW、IVF、Flat 向量索引怎么按场景选
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 索引选型]
type: 面试题
---

## 1166：HNSW、IVF、Flat 向量索引怎么按场景选

**答**：
- 三者取舍：Flat 精确检索（小库 <10 万向量，延迟可接受，零召回损失）；HNSW 图索引（召回高、延迟低、内存大、构建慢、删除支持弱）；IVF 倒排（内存省、可增删、召回靠 nprobe 调、大库首选）。
- 工程决策锚点：库规模（10 万内 Flat、百万级 HNSW/IVF）、更新频率（高频更新选 IVF，HNSW 删除重建成本高）、内存预算（HNSW 内存是向量的 2~3 倍）。
- 混合方案：热数据 HNSW（低延迟）+ 冷数据 IVF（省内存），按访问频率分层迁移。
- 追问钩子：HNSW 的「删除支持弱」具体指什么？——图索引删点会破坏连通性，多数实现标记墓碑（逻辑删除）不回收，删多了召回下降需定期重建，更新频繁的语料慎用。

```ts
function pickIndex({ size, updateQps, memBudget }) {
  if (size < 1e5) return 'flat';                        // 小库精确检索
  if (updateQps > 10) return 'ivf';                     // 高频更新
  if (memBudget < size * 768 * 4 * 2) return 'ivf';     // 内存紧张
  return 'hnsw';                                        // 默认：低延迟高召回
}
```
