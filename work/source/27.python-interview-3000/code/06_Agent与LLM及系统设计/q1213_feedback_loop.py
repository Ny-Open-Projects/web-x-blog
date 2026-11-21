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
