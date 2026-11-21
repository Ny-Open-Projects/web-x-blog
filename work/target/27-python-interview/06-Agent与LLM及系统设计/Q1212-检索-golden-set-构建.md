---
title: [Q1212] 检索 golden set 构建
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1212 · 检索 golden set 构建

> 难度:★★★☆ | 标签:RAG, 评估

**问**:RAG 评估集(golden set)怎么建?和普通评估集差别在哪?

**答**:RAG golden set 每条要三层标注:query、golden chunk(应被检回的片段,可以多个)、golden answer(参考答案)——比普通问答集多一层"检索级真值",这也是归因(Q1200)的前提。构建途径:从真实 query 日志分层抽样,人工把 query 与最相关 chunk 关联;从文档反向出题(选 chunk 让标注员写问题,快但分布偏"文档式问法");badcase 回流必收。维护原则:golden set 版本化,chunk 切分变更时 golden 映射要重刷,否则评估失真。

```python
# file: code/06_Agent与LLM及系统设计/q1212_golden_set.py
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
```

**追问**:
- golden chunk 标注分歧大怎么办?答:允许"可接受集合"(多个都算对)而非单一片段,hit 定义为命中集合内任一片段;分歧率高的类型说明切分有问题,先修切分。
- 反向出题的分布偏差怎么纠正?答:反向题只做补充(≤30%),主力量必须来自真实 query 抽样,并把反向题单独打标便于分层分析。
