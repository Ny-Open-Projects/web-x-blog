"""查询澄清追问流:意图分差过小视为歧义,生成澄清问题,答复后重写查询。"""

CORPUS_INTENTS = [
    {"intent": "refund", "kw": ["退货", "退款"], "score": 0.0},
    {"intent": "exchange", "kw": ["换货"], "score": 0.0},
]


def intent_scores(query):
    """意图打分桩:命中关键词计分,确定性可复现。"""
    for it in CORPUS_INTENTS:
        it["score"] = sum(1.0 for k in it["kw"] if k in query)
    return CORPUS_INTENTS


class ClarifyFlow:
    AMBIGUOUS_GAP = 1.0                          # top1 与 top2 分差小于该值视为歧义

    def start(self, query):
        cands = sorted(intent_scores(query), key=lambda x: -x["score"])
        top, second = cands[0], cands[1]
        if top["score"] == 0:
            return {"action": "search", "query": query}
        if top["score"] - second["score"] < self.AMBIGUOUS_GAP:
            options = [c["intent"] for c in cands if c["score"] > 0]
            return {"action": "clarify",
                    "question": "您想咨询的是 %s 还是 %s?" % (options[0], options[1]),
                    "options": options, "pending": query}
        return {"action": "search", "query": self.rewrite(query, top["intent"])}

    def resume(self, pending, choice):
        """用户答复澄清后:把所选意图并入查询,歧义解除。"""
        return {"action": "search", "query": self.rewrite(pending, choice)}

    @staticmethod
    def rewrite(query, intent):
        return "[%s] %s" % (intent, query)


if __name__ == "__main__":
    flow = ClarifyFlow()
    r1 = flow.start("我要退货")
    assert r1["action"] == "search" and "refund" in r1["query"], "意图明确直接检索"

    r2 = flow.start("这个能用吗")
    assert r2["action"] == "search" and r2["query"] == "这个能用吗", "零命中不追问"

    r3 = flow.start("退货还是换货好")
    assert r3["action"] == "clarify" and r3["options"] == ["refund", "exchange"]
    r4 = flow.resume(r3["pending"], "exchange")
    assert r4["action"] == "search" and r4["query"] == "[exchange] 退货还是换货好"
    print("澄清流通过:分差小触发追问,答复后槽位并入查询,零命中直接检索")
