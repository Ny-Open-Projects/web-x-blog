---
title: [AGT-077] GraphRAG 是什么概念？知识图谱如何增强检索？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-077：GraphRAG 是什么概念？知识图谱如何增强检索？
**答**：
- 普通 RAG 按块相似检索，回答「跨文档关联型问题」（A 公司的竞争对手的供应商有哪些）无力：关系散落在多个 chunk 里。
- GraphRAG 思想：离线用 LLM 从文档抽取实体与关系三元组构建知识图谱；检索时定位实体节点，沿关系边扩展邻域，把相关子图序列化为上下文。
- 常与向量检索混合：向量负责「找相关文本」，图负责「补关联结构与多跳路径」。
- 成本与难点：图谱构建是一次大额 LLM 开销，实体消歧（同名不同义）是工程难点；讲清适用边界即可。

```typescript
import { z } from 'zod';

// 极简 GraphRAG：实体抽取建图 + 邻域检索
interface GraphEdge { from: string; relation: string; to: string }

async function buildGraph(chunks: string[]): Promise<GraphEdge[]> {
  const edges: GraphEdge[] = [];
  for (const chunk of chunks) {
    const { triples } = await structuredLLM(
      [{ role: 'user', content: `从文本抽取实体关系三元组，实体名用规范化的唯一标识：\n${chunk}` }],
      z.object({ triples: z.array(z.object({ from: z.string(), relation: z.string(), to: z.string() })) }),
    );
    edges.push(...triples);
  }
  return edges;
}

export async function graphRetrieve(query: string, graph: GraphEdge[], hops = 2): Promise<string[]> {
  const { entities } = await structuredLLM(
    [{ role: 'user', content: `识别问题涉及的实体：${query}` }],
    z.object({ entities: z.array(z.string()) }),
  );
  // 沿关系边 BFS 扩展邻域
  let frontier = entities;
  const visited = new Set(entities);
  const contextEdges: GraphEdge[] = [];
  for (let h = 0; h < hops && frontier.length; h++) {
    const next: string[] = [];
    for (const e of graph) {
      if (frontier.includes(e.from) && !visited.has(e.to)) { contextEdges.push(e); next.push(e.to); visited.add(e.to); }
      if (frontier.includes(e.to) && !visited.has(e.from)) { contextEdges.push(e); next.push(e.from); visited.add(e.from); }
    }
    frontier = next;
  }
  // 子图序列化成文本上下文，与向量检索结果合并使用
  return contextEdges.map((e) => `${e.from} --${e.relation}--> ${e.to}`);
}
```

---

## 十七、模型与推理层
