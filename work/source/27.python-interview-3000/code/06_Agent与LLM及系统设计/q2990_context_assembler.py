"""Q2990 上下文组装器:系统/历史/检索/预算 四源拼装。

组装器决定「这次调用带什么进上下文」:系统提示永远保留且排最前;
最新一条用户消息永远保留;检索片段按相关度从高到低塞入;历史消息
从新到旧回填。四者共享一个 token 预算,超预算时按优先级从低到高
丢弃(最老历史先丢、低相关检索先丢),并统计丢弃情况供调试。
"""


def estimate_tokens(text):
    """粗估:中文约 1 字 1 token,英文按 4 字符 1 token,取混合近似。"""
    cjk = sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
    return cjk + (len(text) - cjk) // 4 + 1


class ContextAssembler:
    def __init__(self, budget):
        self.budget = budget

    def assemble(self, system, history, docs, latest_user):
        # 优先级:system > latest_user > 检索 > 历史(新到旧)
        system_msgs = [{"role": "system", "content": system}]
        latest = [{"role": "user", "content": latest_user}]
        fixed_cost = sum(estimate_tokens(m["content"])
                         for m in system_msgs + latest)
        remaining = self.budget - fixed_cost
        if remaining < 0:
            raise ValueError("预算小于系统提示与最新消息之和")

        used_docs, dropped_docs = [], 0
        for doc in sorted(docs, key=lambda d: -d["score"]):
            cost = estimate_tokens(doc["text"])
            if cost <= remaining:
                used_docs.append(doc)
                remaining -= cost
            else:
                dropped_docs += 1

        used_history, dropped_hist = [], 0
        for msg in reversed(history):
            cost = estimate_tokens(msg["content"])
            if cost <= remaining:
                used_history.insert(0, msg)   # 回填保持时间顺序
                remaining -= cost
            else:
                dropped_hist += 1

        messages = system_msgs + used_history + \
            [{"role": "system", "name": "retrieval", "content": d["text"]}
             for d in used_docs] + latest
        return {"messages": messages, "tokens": self.budget - remaining,
                "dropped_docs": dropped_docs,
                "dropped_history": dropped_hist}


def main():
    history = [{"role": "user", "content": "我要查订单 %d 的物流" % i}
               for i in range(8)]
    history.append({"role": "assistant", "content": "好的,请提供订单号。"})
    docs = [
        {"text": "物流政策:下单后 48 小时内发货。", "score": 0.91},
        {"text": "偏远地区顺延两天,新疆西藏除外。", "score": 0.62},
        {"text": "这条完全无关的长文本 " * 12, "score": 0.30},
    ]

    asm = ContextAssembler(budget=120)
    out = asm.assemble("你是物流客服", history, docs, "订单 o_7 到哪了")
    msgs = out["messages"]
    assert msgs[0]["role"] == "system" and "物流客服" in msgs[0]["content"]
    assert msgs[-1]["content"] == "订单 o_7 到哪了"     # 最新消息必在
    assert msgs[0]["content"] != msgs[-1]["content"]
    texts = [m["content"] for m in msgs]
    assert "物流政策:下单后 48 小时内发货。" in texts   # 高相关检索入选
    assert out["dropped_docs"] >= 1                     # 无关长文被挤出
    assert out["tokens"] <= 120
    # 检索片段按分数排序入上下文
    retrieval = [m["content"] for m in msgs if m.get("name") == "retrieval"]
    assert retrieval and retrieval[0].startswith("物流政策"), retrieval

    # 小预算:历史被大量丢弃但核心仍在
    asm2 = ContextAssembler(budget=40)
    out2 = asm2.assemble("你是物流客服", history, docs[:1], "o_7 到哪了")
    assert out2["messages"][-1]["content"] == "o_7 到哪了"
    assert out2["dropped_history"] > 0
    try:
        ContextAssembler(budget=5).assemble("系统提示很长" * 10, [], [],
                                            "hi")
        raise AssertionError("应当报预算不足")
    except ValueError as exc:
        assert "预算" in str(exc)
    print("组装消息数:", len(msgs), "| 预算内 token:", out["tokens"])
    print("丢弃: 检索 %d 条, 历史 %d 条" % (out["dropped_docs"],
                                            out["dropped_history"]))


if __name__ == "__main__":
    main()
