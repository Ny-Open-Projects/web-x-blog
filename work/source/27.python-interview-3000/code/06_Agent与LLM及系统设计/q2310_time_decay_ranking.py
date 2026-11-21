"""检索时间衰减:相关度乘以半衰期衰减因子,新文档不碾压老权威,可配衰减速率。"""
def decay(age_days, half_life=30.0):
    return 0.5 ** (age_days / half_life)


def rank_with_decay(cands, now_day, half_life=30.0, w_rel=0.7, w_fresh=0.3):
    out = []
    for c in cands:
        age = max(0.0, now_day - c["pub_day"])
        d = decay(age, half_life)
        score = round(w_rel * c["rel"] + w_fresh * d, 4)
        out.append({"id": c["id"], "score": score, "decay": round(d, 4)})
    out.sort(key=lambda x: -x["score"])
    return out


if __name__ == "__main__":
    cands = [
        {"id": "老权威", "rel": 0.90, "pub_day": 0},
        {"id": "新速讯", "rel": 0.50, "pub_day": 359},
    ]
    harsh = rank_with_decay(cands, now_day=360, half_life=30.0)
    assert harsh[0]["id"] == "新速讯", "半衰期 30 天 老权威被压没"
    assert harsh[0]["score"] > harsh[1]["score"]
    mild = rank_with_decay(cands, now_day=360, half_life=365.0)
    assert mild[0]["id"] == "老权威", "半衰期放宽 老权威回顶端"
    assert decay(360, 30) < decay(360, 365), "同一文档在宽松政策下衰得更慢"
    assert decay(0) == 1.0, "当天文档不衰减"
    print("时间衰减通过:半衰期 harsh 压老 mild 保权威 衰减率是政策")
