"""评估集构建:分层抽样 + 双标一致性 Kappa + 版本冻结。"""
import json, random


def stratified_sample(pool, per_intent=2, seed=1):
    random.seed(seed)
    by = {}
    for item in pool:
        by.setdefault(item["intent"], []).append(item)
    picked = []
    for intent, items in sorted(by.items()):
        random.shuffle(items)
        picked += items[:per_intent]
    return picked


def kappa(a, b, labels):
    """双标一致性 Cohen's Kappa。"""
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = sum((a.count(l) / n) * (b.count(l) / n) for l in labels)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


if __name__ == "__main__":
    pool = [{"id": i, "intent": t, "q": f"问题{i}关于{t}"}
            for i, t in enumerate(["售后"] * 5 + ["物流"] * 3 + ["闲聊"] * 4)]
    evalset = stratified_sample(pool, per_intent=2)
    print("分层抽样:", [(e["id"], e["intent"]) for e in evalset])
    assert {e["intent"] for e in evalset} == {"售后", "物流", "闲聊"}, "小意图必须被保留"

    rater_a = ["good", "good", "bad", "good", "bad", "good"]
    rater_b = ["good", "good", "bad", "bad", "bad", "good"]
    k = kappa(rater_a, rater_b, ["good", "bad"])
    print(f"双标 Kappa = {k:.2f}", "达标" if k >= 0.6 else "需重训标注规范")
    assert k >= 0.6, "一致性过低,评估集不可信"

    frozen = json.dumps(sorted([e["id"] for e in evalset]))
    print("冻结版本指纹:", frozen)
    print("评估集 v1 定稿,后续改动走评审")
