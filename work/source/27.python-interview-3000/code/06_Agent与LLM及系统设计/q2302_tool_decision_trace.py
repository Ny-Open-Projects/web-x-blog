"""工具选择留痕:候选工具按相关度 权限 成本打分,胜出与落选都进决策日志。"""


def score_candidates(cands, query_tags, budget_left):
    scored = []
    for c in cands:
        overlap = len(set(c["tags"]) & set(query_tags))
        s = overlap * 3.0
        if not c["allowed"]:
            s -= 100.0
        if c["avg_cost"] > budget_left:
            s -= 20.0
        scored.append({"tool": c["name"], "score": round(s, 2),
                       "reason": "tag匹配%d 权限%s 预算%s" % (
                           overlap, "有" if c["allowed"] else "无",
                           "够" if c["avg_cost"] <= budget_left else "超")})
    scored.sort(key=lambda d: d["score"], reverse=True)
    return scored


def decide(cands, query_tags, budget_left):
    trace = score_candidates(cands, query_tags, budget_left)
    winner = trace[0]["tool"] if trace and trace[0]["score"] > 0 else None
    return {"winner": winner, "trace": trace}


if __name__ == "__main__":
    cands = [
        {"name": "order_api", "tags": ["order", "refund"], "allowed": True, "avg_cost": 0.02},
        {"name": "crm_lookup", "tags": ["customer"], "allowed": True, "avg_cost": 0.01},
        {"name": "raw_delete", "tags": ["order", "refund"], "allowed": False, "avg_cost": 0.0},
    ]
    d = decide(cands, ["refund", "order"], budget_left=0.05)
    assert d["winner"] == "order_api"
    assert [t["tool"] for t in d["trace"]] == ["order_api", "crm_lookup", "raw_delete"]
    assert d["trace"][2]["score"] < 0 and "无" in d["trace"][2]["reason"], "无权限候选垫底但留痕"
    d2 = decide(cands, ["weather"], budget_left=0.01)
    assert d2["winner"] is None, "无相关候选时显式说不知道 而不是硬选"
    assert all(t["score"] <= 0 for t in d2["trace"])
    d3 = decide(cands, ["refund", "order"], budget_left=0.005)
    assert "超" in d3["trace"][0]["reason"], "超预算也要扣分留痕"
    print("决策留痕通过:候选评分 胜出落选全留痕 无候选显式弃权")
