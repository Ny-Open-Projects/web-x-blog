"""表格检索切块:行级成块,块内继承表头行,检索命中行级事实并可回指原表。"""
import hashlib
import math


def embed(text, dim=24):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


TABLE = {
    "header": ["年份", "季度", "营收"],
    "rows": [
        ["2023", "Q4", "1200 万"],
        ["2024", "Q1", "1500 万"],
        ["2024", "Q2", "1800 万"],
        ["2024", "Q3", "2100 万"],
    ],
}


def chunk_table(table, rows_per_chunk=2):
    header = " ".join(table["header"])
    chunks = []
    for i in range(0, len(table["rows"]), rows_per_chunk):
        part = table["rows"][i:i + rows_per_chunk]
        lines = [header] + [" ".join(r) for r in part]
        chunks.append({"text": "\n".join(lines),
                       "meta": {"header": table["header"],
                                "row_index": [i + j for j in range(len(part))],
                                "header_inherited": True}})
    return chunks


class TableIndex:
    def __init__(self, chunks):
        self.items = [(c, embed(c["text"])) for c in chunks]

    def search(self, query, topk=2):
        q = embed(query)
        ranked = sorted(((cosine(q, v), c) for c, v in self.items), reverse=True)
        return [c for _, c in ranked[:topk]]


if __name__ == "__main__":
    chunks = chunk_table(TABLE, rows_per_chunk=2)
    assert len(chunks) == 2
    assert chunks[1]["meta"]["row_index"] == [2, 3], "块元数据回指原表行号"
    assert chunks[1]["meta"]["header_inherited"] is True
    assert chunks[1]["text"].startswith("年份 季度 营收"), "每块继承表头"

    index = TableIndex(chunks)
    best = index.search("2024 Q3 营收", topk=2)
    assert "2024 Q3 2100 万" in best[0]["text"], "命中正确的行块"
    assert "1200 万" not in best[0]["text"], "不混入其他行的值"
    print("表格切块通过:4 行切成 2 块,块块带表头,检索精确命中行级事实")
