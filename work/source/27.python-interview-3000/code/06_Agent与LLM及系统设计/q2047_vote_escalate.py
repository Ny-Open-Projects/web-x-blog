"""消歧的升级决策:平票或低置信不硬答,生成候选澄清项交回用户。"""


def decide(vote_result, options_meta=None):
    """根据投票结果决定作答还是升级澄清。"""
    if not vote_result["ranked"]:
        return {"action": "clarify", "options": [],
                "reason": "无任何来源支撑,应引导用户换个问法"}
    if vote_result["confident"]:
        return {"action": "answer", "value": vote_result["winner"],
                "reason": "加权优势充分,直接作答"}
    top = [v for v, _ in vote_result["ranked"][:2]]
    meta = options_meta or {}
    return {"action": "clarify", "options": top,
            "labels": [meta.get(v, v) for v in top],
            "reason": "来源分歧大,请用户选一个方向"}


if __name__ == "__main__":
    strong = {"winner": "15 天", "confident": True,
              "ranked": [("15 天", 1.3), ("7 天", 0.4)], "margin": 0.9}
    d1 = decide(strong)
    assert d1["action"] == "answer" and d1["value"] == "15 天"

    tie = {"winner": "A 方案", "confident": False,
           "ranked": [("A 方案", 0.61), ("B 方案", 0.59)], "margin": 0.02}
    d2 = decide(tie, options_meta={"A 方案": "按官网 2025 版",
                                   "B 方案": "按客服口径"})
    assert d2["action"] == "clarify"
    assert d2["options"] == ["A 方案", "B 方案"]
    assert d2["labels"][1] == "按客服口径", "澄清项要带人话标签"

    empty = {"winner": None, "confident": False, "ranked": [], "margin": 0}
    d3 = decide(empty)
    assert d3["action"] == "clarify" and d3["options"] == []
    assert "换" in d3["reason"]
    print("升级决策通过:强优势作答,平票转澄清带标签,零来源引导换问法")
