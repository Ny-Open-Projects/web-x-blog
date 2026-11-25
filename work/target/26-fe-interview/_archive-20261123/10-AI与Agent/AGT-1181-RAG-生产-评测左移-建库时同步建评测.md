---
title: [1181] 知识库建设时怎么「评测左移」
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 评测]
type: 面试题
---

## 1181：知识库建设时怎么「评测左移」

**答**：
- 左移含义：评估集与知识库同步建设，不是建完库再补评测——每篇重要文档入库时生成「配套探针题」（2~3 条带证据引用），评估集随知识库自然生长。
- 好处：评估集的证据引用天然准确（建库时标）、覆盖随文档增长无死角、验收即评测（文档入库批次跑探针，可达性不达标不收货）。
- 落地机制：入库流水线的「验收环节」= 探针检索断言；文档 owner 的交付定义包含「探针通过」。
- 追问钩子：左移后评估集会不会全是「文档视角」而缺「用户视角」？——会，探针题只保证「文档可检索」，不保证「用户真会这么问」；用户视角靠线上 query 聚类持续补充，两条腿走路。

```ts
async function ingestWithEval(doc, owner) {
  const probes = await genProbes(doc, 2);           // 配套探针题
  const build = await indexDoc(doc);
  const pass = await verifyProbes(probes, build);   // 入库即验收
  if (!pass.ok) return reject(owner, pass.failures); // 不达标不收货
  await evalStore.add(probes.map(p => ({ ...p, evidence: [doc.id], owner })));
  return build;
}
```
