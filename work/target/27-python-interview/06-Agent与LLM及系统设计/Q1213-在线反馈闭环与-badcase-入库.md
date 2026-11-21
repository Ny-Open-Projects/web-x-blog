---
title: [Q1213] 在线反馈闭环与 badcase 入库
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1213 · 在线反馈闭环与 badcase 入库

> 难度:★★★☆ | 标签:RAG, 运营

**问**:线上用户点踩后,badcase 怎么流转才能变成系统改进?

**答**:闭环五步:捕获(点踩 + 会话上下文 + 检索快照一并留存,缺检索快照就无法归因)、归因(自动跑 Q1200 四分法初判)、入库(badcase 库带标签与状态:待审/已归因/已修复/忽略)、修复(按归因类型进不同 backlog:切分/改写/生成)、回归(修复后 badcase 自动进 golden set,防止复发)。运营要点:badcase 要去重聚合(同一根因多条只算一个工单);设"复发率"指标衡量闭环有效性;用户反馈要回复或公示改进,否则反馈量会衰减。

```python
# file: code/06_Agent与LLM及系统设计/q1213_feedback_loop.py
"""badcase 闭环:捕获带检索快照 -> 自动归因 -> 状态机流转 -> 回归防复发。"""


class BadCaseStore:
    STATES = {"new", "triaged", "fixing", "fixed", "wont_fix"}

    def __init__(self):
        self.cases, self._next = [], 0

    def add(self, query, answer, retrieval_snapshot, feedback):
        self._next += 1
        case = {"id": self._next, "query": query, "answer": answer,
                "retrieval": retrieval_snapshot, "feedback": feedback,
                "state": "new", "root_cause": None}
        self.cases.append(case)
        return case["id"]

    def auto_triage(self, case, gold_in_recall, gold_in_context, supported):
        if not gold_in_recall:
            cause = "retrieval"
        elif not gold_in_context:
            cause = "ranking"
        elif not supported:
            cause = "generation"
        else:
            cause = "annotation"
        case["root_cause"] = cause
        case["state"] = "triaged"
        return cause

    def transition(self, case_id, to):
        assert to in self.STATES
        case = next(c for c in self.cases if c["id"] == case_id)
        case["state"] = to

    def promote_to_golden(self, case):
        assert case["state"] == "fixed"
        return {"q": case["query"], "golden_chunks": case["retrieval"]["gold"],
                "type": "badcase_regress", "src": f"badcase-{case['id']}"}


if __name__ == "__main__":
    store = BadCaseStore()
    cid = store.add("退货要几天", "三十天内可退",
                    {"recall": ["c1", "c9"], "context": ["c1"], "gold": "c2"}, "bad")
    case = store.cases[0]
    cause = store.auto_triage(case, gold_in_recall=False, gold_in_context=False, supported=False)
    print("自动归因:", cause)
    assert cause == "retrieval"

    store.transition(cid, "fixing")
    store.transition(cid, "fixed")
    golden_entry = store.promote_to_golden(case)
    print("回归条目:", golden_entry)
    assert golden_entry["type"] == "badcase_regress"

    # 去重聚合:同根因多条归并
    cid2 = store.add("退货几天", "三十天内可退", {"recall": [], "context": [], "gold": "c2"}, "bad")
    store.auto_triage(store.cases[1], False, False, False)
    groups = {}
    for c in store.cases:
        groups.setdefault(c["root_cause"], []).append(c["id"])
    print("按根因聚合:", {k: len(v) for k, v in groups.items()})
    assert len(groups["retrieval"]) == 2, "同根因可合并为一个修复工单"
    print("闭环:捕获含快照,归因驱动修复,修复进回归")
```

**追问**:
- 检索快照存什么才够归因?答:query 原文与改写、召回列表带分数与排名、最终上下文集合、切分版本与索引版本——四个版本号缺一不可,否则时间一长无法复现。
- 点踩很少是不是系统没问题?答:不一定,可能是反馈入口太深;要对照隐式信号(改写率、放弃率)交叉验证,反馈率本身也是监控对象。
