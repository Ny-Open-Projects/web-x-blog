---
title: [901] RAG 分块策略为什么不能一刀切？给一个按文档类型拆分的生产案例
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 分块策略]
type: 面试题
---

## 901：RAG 分块策略为什么不能一刀切？给一个按文档类型拆分的生产案例

**答**：
- 分块决定检索召回的上限：FAQ 类按「一问一答」天然分块，长文档要按标题层级切，代码要按函数边界切，一刀切固定 512 token 会把表格和步骤序列切碎。
- 生产案例：帮助中心迁移后 NDCG 从 0.62 掉到 0.55，原因是统一用 markdown 标题切分把 API 表格拆散；改为「表格整块保留 + 标题分块」后回升到 0.71。
- 每个 chunk 要携带元数据（文档路径、章节标题、更新时间），拼接进 prompt 时让模型知道上下文归属。
- 追问钩子：chunk 越大越好吗？——过大稀释向量语义、挤占上下文窗口，通常 300~800 token + 10~15% 重叠是起点，最终以评估集为准。

```ts
function chunkDoc(doc: Doc): Chunk[] {
  const chunks: Chunk[] = [];
  for (const sec of doc.sections) {
    if (sec.type === 'table') {
      // 表格整块保留：拆散后行列对应关系丢失，检索命中也无法回答
      chunks.push({ text: sec.heading + '\n' + sec.raw, meta: sec.meta });
    } else if (sec.tokens <= MAX_CHUNK) {
      chunks.push({ text: sec.heading + '\n' + sec.body, meta: sec.meta });
    } else {
      // 长章节滑动窗口切分，带重叠防止关键句被切断
      for (const w of slidingWindow(sec.body, 600, 80)) {
        chunks.push({ text: sec.heading + '\n' + w, meta: sec.meta });
      }
    }
  }
  return chunks;
}
```

