"""golden set 构建:三层标注结构 + 分层抽样 + 版本指纹与切分联动。"""
import json, random


def build_from_queries(logs, per_type=2):
    random.seed(3)
    by_type = {}
    for row in logs:
        by_type.setdefault(row["type"], []).append(row)
    golden = []
    for t, rows in sorted(by_type.items()):
        random.shuffle(rows)
        for r in rows[:per_type]:
            golden.append({"q": r["q"], "golden_chunks": r["matched_chunks"],
                           "ref_answer": r.get("answer"), "type": t, "src": "query_log"})
    return golden


def reverse_from_docs(docs):
    """文档反向出题:每个 chunk 配一个模板问题,标注来源。"""
    return [{"q": f"关于 {d['topic']} 的规定是什么", "golden_chunks": [d["chunk_id"]],
             "ref_answer": None, "type": "反向出题", "src": "doc_reverse"}
            for d in docs]


def fingerprint(golden):
    return hashlib.md5(json.dumps(golden, sort_keys=True, ensure_ascii=False)
                       .encode()).hexdigest()[:10]


import hashlib


if __name__ == "__main__":
    logs = [{"q": "退货运费谁出", "matched_chunks": ["c1"], "answer": "买家承担", "type": "政策"},
            {"q": "退货几天内", "matched_chunks": ["c2"], "answer": "七天", "type": "政策"},
            {"q": "多久发货", "matched_chunks": ["c3"], "answer": "48 小时", "type": "物流"},
            {"q": "偏远地区呢", "matched_chunks": ["c3"], "answer": "72 小时", "type": "物流"},
            {"q": "能开发票吗", "matched_chunks": ["c4"], "answer": "支持电子发票", "type": "发票"}]
    gs = build_from_queries(logs, per_type=1)
    print("分层抽样:", [(g["q"], g["type"]) for g in gs])
    assert {g["type"] for g in gs} == {"政策", "物流", "发票"}, "小意图类型必须保留"
    assert all(g["golden_chunks"] for g in gs), "检索级真值必填"

    rev = reverse_from_docs([{"topic": "隐私合规", "chunk_id": "c9"}])
    print("反向出题补充:", rev)
    assert rev[0]["src"] == "doc_reverse"

    fp = fingerprint(gs + rev)
    print("golden set 版本指纹:", fp)
    print("chunk 切分变更时必须重刷 golden_chunks 映射,否则评估失真")
