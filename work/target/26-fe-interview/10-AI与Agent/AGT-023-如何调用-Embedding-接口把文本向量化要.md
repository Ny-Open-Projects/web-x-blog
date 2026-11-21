---
title: [AGT-023] 如何调用 Embedding 接口把文本向量化？要注意什么？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-023：如何调用 Embedding 接口把文本向量化？要注意什么？
**答**：
- Embedding 把文本映射成定长浮点向量，语义相近的文本向量距离更近，是向量检索的基础。
- 接口支持批量 input，务必分批（如 64 条/批）调用，注意不同服务商的批量与单条长度上限。
- 批量返回按 `index` 归位，防止顺序错乱；入库时向量与原文、元数据要绑定存储。
- 查询与文档必须用同一个 embedding 模型，换模型要全量重建索引。

```typescript
// 批量化 Embedding：分批请求，按 index 归位
export async function embed(texts: string[]): Promise<number[][]> {
  const BATCH_SIZE = 64;
  const vectors: number[][] = [];

  for (let i = 0; i < texts.length; i += BATCH_SIZE) {
    const batch = texts.slice(i, i + BATCH_SIZE);
    const res = await fetch(`${OPENAI_BASE_URL}/embeddings`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
      },
      body: JSON.stringify({ model: 'text-embedding-3-small', input: batch }),
    });
    if (!res.ok) throw new Error(`Embedding 失败：${res.status}`);
    const data = await res.json();
    for (const item of data.data) {
      vectors[item.index + i] = item.embedding; // 按 index 归位
    }
  }
  return vectors;
}

export async function embedQuery(query: string): Promise<number[]> {
  return (await embed([query]))[0];
}
```
