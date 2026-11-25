---
title: [AGT-144] embedding 模型要切换（升级/换供应商）时，迁移策略怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-144：embedding 模型要切换（升级/换供应商）时，迁移策略怎么设计？
**答**：
- 核心问题：新旧模型的向量不在同一空间，直接混用检索必坏——迁移期必须「双跑」：同一份知识库同时维护新旧两套向量，读流量灰度切到新模型。
- 标准流程：影子索引全量重嵌入 → 用标注 query 集对比新旧召回质量（recall@k、命中成本）→ 按 doc 分批切流量 → 旧索引保留一个观察期后下线。
- 成本控制：重嵌入是「文档数 × 单价」的一次性大账单，用 Batch API 跑离线、按 last_embedded_at 增量跳过未变更 chunk。
- 回滚设计：切换期间保留旧索引与旧路由开关，召回质量劣化立即切回；新查询（query embedding）与文档向量必须同模型版本，用索引元数据里的 modelTag 强校验。

```typescript
// embedding 迁移：影子索引 + 双跑灰度 + 模型标签强校验
const MODELS = {
  v1: { id: 'text-embedding-3-small', dim: 1536 },
  v2: { id: 'text-embedding-3-large', dim: 3072 },
} as const;
type ModelTag = keyof typeof MODELS;

export async function reindexShadow(docs: { id: string; text: string }[], from: ModelTag, to: ModelTag) {
  // 离线批量重嵌入到影子索引（Batch API，成本优先）
  await batchEmbed(docs.map((d) => d.text)).then((vectors) =>
    vectorAdmin.createShadowIndex(`kb-${to}`, docs.map((d, i) => ({ id: d.id, values: vectors[i], meta: { modelTag: to } }))));
}

export async function searchDual(query: string, ratioToV2: number, queryAcl?: unknown): Promise<{ text: string }[]> {
  const useV2 = Math.random() * 100 < ratioToV2; // 按比例灰度切流
  const tag: ModelTag = useV2 ? 'v2' : 'v1';
  const vec = await embedWith(query, tag);
  const hits = await vectorAdmin.query(useV2 ? `kb-${tag}` : `kb-main`, vec, tag); // 查询与文档同版本空间
  metrics.inc(`search.model.${tag}`);                                              // 对比新旧召回的评测指标
  return hits;
}

// 元数据强校验：向量库里的 modelTag 必须与查询模型一致，不一致直接报错而非静默混用
const vectorAdmin = {
  createShadowIndex: async (n: string, items: any[]) => { void n; void items; },
  query: async (index: string, vec: number[], tag: ModelTag) => {
    void vec;
    const meta = await getIndexMeta(index);
    if (meta.modelTag !== tag) throw new Error(`embedding 空间混用：索引 ${meta.modelTag} vs 查询 ${tag}`);
    return [] as { text: string }[];
  },
};
async function batchEmbed(texts: string[]) { return texts.map(() => new Array(3072).fill(0)); }
async function embedWith(t: string, tag: ModelTag) { void tag; return new Array(1536).fill(0); }
function getIndexMeta(i: string) { return Promise.resolve({ modelTag: 'v1' as ModelTag }); }
```
