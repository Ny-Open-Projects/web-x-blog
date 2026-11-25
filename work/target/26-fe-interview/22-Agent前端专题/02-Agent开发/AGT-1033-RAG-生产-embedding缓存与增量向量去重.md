---
title: [1033] 重复文档反复入库，向量层怎么去重省成本
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 去重]
type: 面试题
---

## 1033：重复文档反复入库，向量层怎么去重省成本

**答**：
- 入库前去重三步：精确去重（内容 hash）、近重去重（simhash/minhash，阈值内视为重复不重新 embedding）、段落级去重（同一文档被多处引用的段落只索引一次，多文档引用计数）。
- embedding 结果缓存：以「文本 hash + 模型版本」为 key，同文本重入库直接复用向量——批量爬虫场景能省 30%+ 的 embedding 成本。
- 引用计数删除：段落被多文档引用时，删一个文档只减计数，计数归零才真正删向量，防止误删其他文档的证据。
- 追问钩子：去重会不会误删「重复但上下文不同」的段落？——会，所以去重粒度到「段落 + 所属文档」两元组，跨文档重复段落用引用计数而非物理删除。

```ts
async function ingestDoc(doc) {
  const chunks = chunkDoc(doc);
  for (const c of chunks) {
    const h = hash(c.text);
    if (await dedupe.exists(h)) { await refCount.incr(h, doc.id); continue; } // 近重/精确
    const vec = await embedCache(c.text, MODEL_VER);   // embedding 缓存
    await index.add({ ...c, vec, h });
    await refCount.set(h, 1, doc.id);
  }
}
async function removeDoc(docId) {
  for (const h of await refCount.of(docId)) {
    if ((await refCount.dec(h, docId)) === 0) await index.delete(h); // 归零才删
  }
}
```
