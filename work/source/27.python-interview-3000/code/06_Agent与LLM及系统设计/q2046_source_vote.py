"""答案消歧来源投票:多来源取值冲突时,按权威分与新鲜度加权投票定答案。"""


def vote(candidates):
    """candidates: [{value, authority, days}] authority 为来源权威分,days 为距今天数。"""
    if not candidates:
        return {"winner": None, "score": 0.0, "margin": 0.0, "ranked": [],
                "dissent": [], "confident": False}
    weight = {}
    for c in candidates:
        decay = 1.0 / (1.0 + c["days"] * 0.1)      # 越新权重越高
        weight[c["value"]] = weight.get(c["value"], 0.0) + c["authority"] * decay
    ranked = sorted(weight.items(), key=lambda kv: -kv[1])
    total = sum(weight.values())
    top_value, top_w = ranked[0]
    runner = ranked[1][1] if len(ranked) > 1 else 0.0
    margin = top_w - runner
    return {"winner": top_value, "score": round(top_w, 3),
            "margin": round(margin, 3),
            "ranked": ranked,
            "dissent": [v for v, _ in ranked[1:]],
            "confident": total > 0 and margin / total > 0.2}


if __name__ == "__main__":
    # 官方文档新且权威,论坛旧且弱:官方赢, dissent 留痕
    r1 = vote([
        {"value": "15 天", "authority": 0.9, "days": 2},
        {"value": "15 天", "authority": 0.5, "days": 30},
        {"value": "7 天", "authority": 0.4, "days": 400},
    ])
    assert r1["winner"] == "15 天"
    assert r1["dissent"] == ["7 天"], "落选值必须留痕供审计"
    assert r1["confident"] is True

    # 同权威但一新一旧:新的赢
    r2 = vote([
        {"value": "V2 接口", "authority": 0.8, "days": 1},
        {"value": "V1 接口", "authority": 0.8, "days": 200},
    ])
    assert r2["winner"] == "V2 接口" and r2["confident"] is True

    # 权威分互相抵消:第一名优势不足 -> 不置信
    r3 = vote([
        {"value": "A 方案", "authority": 0.6, "days": 10},
        {"value": "B 方案", "authority": 0.6, "days": 12},
    ])
    assert r3["confident"] is False, "微弱领先必须标记不置信"
    assert r3["margin"] / (r3["score"] + r3["ranked"][1][1]) < 0.2

    assert vote([])["confident"] is False, "无来源不能拍板"
    print("来源投票通过:权威加新鲜度加权,获胜值定案, dissent 留痕, 弱优势标记不置信")
