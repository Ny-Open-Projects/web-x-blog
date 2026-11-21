"""Q2584 检索结果的时效打分:先识别查询是否时效敏感。

时间衰减排序不该全局打开:什么是 RAG 这类稳定型查询被新鲜度
加权会推出旧闻漏掉经典;先检测查询里的时间信号,只对时效敏感
查询启用新鲜度加成。
"""
import re

TIME_HINTS = re.compile(r"最新|今年|今天|最近|2026|实时")
FRESH_WEIGHT = 0.3

DOCS = [
    {"id": "2023旧闻", "sim": 0.90, "freshness": 0.10},
    {"id": "2026新报", "sim": 0.78, "freshness": 0.95},
]


def is_fresh_query(q):
    return bool(TIME_HINTS.search(q))


def score(docs, query):
    fresh = is_fresh_query(query)
    out = []
    for d in docs:
        s = d["sim"] + (FRESH_WEIGHT * d["freshness"] if fresh else 0.0)
        out.append((d["id"], round(s, 3)))
    return sorted(out, key=lambda x: -x[1])


def main():
    q1 = "什么是 RAG"
    q2 = "2026 最新的 RAG 进展"
    assert is_fresh_query(q2) and not is_fresh_query(q1)
    r1 = score(DOCS, q1)
    r2 = score(DOCS, q2)
    assert r1[0][0] == "2023旧闻", r1
    assert r2[0][0] == "2026新报", r2
    print("稳定查询", q1, "→", r1, "纯相关度")
    print("时效查询", q2, "→", r2, "相关度加新鲜度,排序翻转")


if __name__ == "__main__":
    main()
