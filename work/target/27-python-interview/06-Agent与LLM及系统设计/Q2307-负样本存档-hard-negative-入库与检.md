---
title: [Q2307] 负样本存档:hard negative 入库与检索复用
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2307 · 负样本存档:hard negative 入库与检索复用

> 难度:★★★☆ | 标签:RAG, 评估, 数据

**问**:用户问水果价格,检索把 iPhone 发布会排第一,这种"看着相关其实答非所问"的例子怎么变废为宝?

**答**:这类案例叫 hard negative:字面或语义上与查询有交集、排名靠前、但对 answering 无贡献的块。把 query 与 doc 对记进负样本存档,标注排名与原因,沉淀成资产而不是散落在 badcase 群里。两个用法:检索侧做查询级降权,同 query 再次出现时对存档负样本加惩罚分,立即止血;评估侧做回归集,每次调排序模型或换嵌入都要验证这些历史陷阱不再上榜。注意惩罚的作用域是查询级,跨查询乱加会把别的合法场景打坏。存档要定期清洗:有些"负样本"其实是语料缺失的信号,该进语料建设而不是降权。

```python
# file: code/06_Agent与LLM及系统设计/q2307_hard_negative_archive.py
"""负样本存档:检索靠前但不该命中的块记为 hard negative,评估时验证不再上榜。"""


class NegativeArchive:
    def __init__(self):
        self.items = []

    def record(self, query, doc, rank, reason="ranked_high_but_irrelevant"):
        self.items.append({"query": query, "doc": doc, "rank": rank, "reason": reason})

    def penalty_view(self):
        pen = {}
        for it in self.items:
            pen.setdefault(it["query"], {})[it["doc"]] = -0.3
        return pen


def rerank_with_archive(ranked, query, archive):
    pen = archive.penalty_view().get(query, {})
    adj = [(d, round(s + pen.get(d, 0.0), 4)) for d, s in ranked]
    adj.sort(key=lambda t: t[1], reverse=True)
    return adj


if __name__ == "__main__":
    arch = NegativeArchive()
    arch.record("苹果 价格", "iphone 发布会", 1)
    ranked = [("iphone 发布会", 0.9), ("水果 促销", 0.8)]
    before = [d for d, _ in ranked]
    after = rerank_with_archive(ranked, "苹果 价格", arch)
    assert before[0] == "iphone 发布会", "负样本原本高居榜首"
    assert after[0][0] == "水果 促销", "惩罚后正例登顶"
    assert after[1][1] == 0.6, "hard negative 被降权"
    arch.record("苹果 价格", "iphone 发布会", 1)
    assert len(arch.penalty_view()["苹果 价格"]) == 1, "重复记录去重 不叠加惩罚"
    other = rerank_with_archive(ranked, "苹果 手机", arch)
    assert other[0][0] == "iphone 发布会", "惩罚只对同查询生效"
    print("负样本存档通过:记录 hard negative 查询级降权 隔离生效范围")
```

**追问**:
- 负样本和 badcase 库什么关系? 答:badcase 是现象记录,负样本是其中可执行化的子集,带结构化字段能直接进排序逻辑
- 惩罚分怎么定? 答:从让正例刚好登顶的最小值起步,回放历史查询验证不误伤,写进配置带版本
