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
