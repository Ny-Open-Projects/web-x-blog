---
title: [ARC-149] RAG 平台架构（文档管道 / 向量库 / 评测）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-149：RAG 平台架构（文档管道 / 向量库 / 评测）如何设计？
**答**：
- 离线管道：文档接入（权限继承是关键：用户搜不到的文档，RAG 也不能喂给模型）→ 解析（PDF/HTML/Office 分别处理）→ 切分（按语义边界，保留标题层级做元数据）→ 向量化入库 → 定期增量更新（文档变更事件驱动）。
- 在线链路：混合检索（向量召回 + 关键词 BM25，取长补短）→ 重排（cross-encoder 精排）→ 组装 prompt → 生成带引用。
- 评测体系是平台成败关键：固定评测集（问题 + 标准答案 + 出处），指标含检索命中率、答案忠实度（防幻觉）、端到端准确率；每次切分策略/模型变更跑回归评测。
- 权限与合规：检索层按用户权限过滤（query-time filter），答案必须带出处链接可追溯。

```typescript
// RAG 核心链路（简化）
interface DocChunk { id: string; docId: string; acl: string[]; text: string; embedding: number[]; path: string[] }

// 离线管道：文档变更事件驱动增量更新
pipeline.on('doc.updated', async (doc) => {
  await vectorStore.deleteByDoc(doc.id);
  const chunks = semanticSplit(doc.content, { maxLen: 512, keepHeadings: true });  // 语义切分
  await vectorStore.upsert(chunks.map(c => ({ ...c, acl: doc.acl, embedding: await embed(c.text) })));
});

// 在线检索：混合检索 + 权限过滤 + 重排
async function answer(question: string, user: User) {
  const [vecHits, kwHits] = await Promise.all([
    vectorStore.search(await embed(question), { filter: { acl_overlap: user.groups }, topK: 20 }),
    keywordSearch(question, { topK: 20, acl: user.groups }),                        // BM25
  ]);
  const merged = rrfFuse(vecHits, kwHits);                   // 混合融合
  const top = await reranker.rerank(question, merged, { topK: 5 });
  return llm.generate({
    context: top.map(c => `[${c.docId}] ${c.text}`),         // 强制带出处
    instruction: '仅根据资料回答，标注引用编号，资料没有则明确说不知道',
  });
}
// 评测集回归：evals/rag.jsonl { question, expected_answer, expected_source }
// 指标：retrieval_hit_rate / faithfulness / e2e_accuracy，模型或切分策略变更必须跑
```
