---
title: [Q1197] GraphRAG:实体关系图检索
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1197 · GraphRAG:实体关系图检索

> 难度:★★★★ | 标签:RAG, 知识图谱

**问**:GraphRAG 解决什么普通 RAG 解决不了的问题?自己实现一个迷你版要几步?

**答**:GraphRAG 擅长"多跳与全局性问题"——"A 和 C 有什么关系"需要跨文档拼证据,普通向量检索每次只抓最相似的片段,拼不出关系链。迷你版三步:离线抽取(从每个 chunk 抽实体与关系三元组,桩可用词典+共现)、构图(实体为节点,关系为边,带来源 chunk 引用)、查询(识别 query 中的实体,沿关系图扩 1-2 跳,把路径上的 chunk 收集给 LLM)。代价是离线抽取成本高,适合语料稳定、问题偏分析型的场景。

```python
# file: code/06_Agent与LLM及系统设计/q1197_graphrag_mini.py
"""迷你 GraphRAG:实体共现构图 + 多跳扩展 + 带 chunk 溯源的关系回答。"""


class MiniGraphRAG:
    def __init__(self):
        self.graph = {}                      # entity -> {neighbor: [chunk_ids]}
        self.chunks = {}

    def ingest(self, chunk_id, text, known_entities):
        self.chunks[chunk_id] = text
        present = [e for e in known_entities if e in text]
        for i, a in enumerate(present):
            for b in present[i + 1:]:
                self.graph.setdefault(a, {}).setdefault(b, []).append(chunk_id)
                self.graph.setdefault(b, {}).setdefault(a, []).append(chunk_id)

    def related(self, entity, hops=2):
        seen, frontier, paths = {entity}, [entity], []
        for _ in range(hops):
            nxt = []
            for node in frontier:
                for nb, chunk_ids in self.graph.get(node, {}).items():
                    if nb not in seen:
                        seen.add(nb)
                        nxt.append(nb)
                        paths.append((node, nb, chunk_ids))
            frontier = nxt
            if not frontier:
                break
        return paths

    def answer_evidence(self, query_entities, hops=2):
        evidence, used_chunks = [], set()
        for e in query_entities:
            for a, b, cids in self.related(e, hops):
                for cid in cids:
                    if cid not in used_chunks:
                        used_chunks.add(cid)
                        evidence.append(f"{a} - {b} [{cid}]: {self.chunks[cid]}")
        return evidence


if __name__ == "__main__":
    g = MiniGraphRAG()
    g.ingest("c1", "张伟 是 Acme 的 CTO", ["张伟", "Acme"])
    g.ingest("c2", "Acme 投资 了 BetaLabs", ["Acme", "BetaLabs"])
    g.ingest("c3", "BetaLabs 发布 了 Star 模型", ["BetaLabs", "Star"])
    ev = g.answer_evidence(["张伟"], hops=2)
    print("两跳证据链:")
    for e in ev:
        print("  -", e)
    assert any("BetaLabs" in e for e in ev), "两跳必须到达 BetaLabs"
    assert all("[" in e for e in ev), "每条证据带 chunk 溯源"
    print("关系链拼出跨文档证据,单路向量检索做不到这一点")
```

**追问**:
- 实体抽取全是噪声怎么办?答:词典/模型抽取后加"实体归一"(别名合并)与出现频次过滤,长尾噪声节点不进图,宁可图稀疏也别图脏。
- 图更新怎么做?答:按 chunk 级增量——chunk 重解析时删除旧三元组(带 chunk_id 反向索引)再加新的,保证图与语料一致。
