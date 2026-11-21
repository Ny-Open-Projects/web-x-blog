"""评估门禁:分层硬门禁 + 总分软门禁 + 结构化报告。"""


def run_eval(model, evalset):
    by_intent = {}
    for case in evalset:
        got = model(case["q"])
        ok = case["expect"] in got
        by_intent.setdefault(case["intent"], []).append(ok)
    detail = {k: sum(v) / len(v) for k, v in by_intent.items()}
    overall = sum(sum(v) for v in by_intent.values()) / sum(len(v) for v in by_intent.values())
    return detail, overall


def gate(baseline_detail, baseline_overall, new_detail, new_overall,
         hard_floor=0.8, soft_drop=0.02):
    report = {"verdict": "pass", "violations": []}
    for intent, acc in new_detail.items():
        if acc < hard_floor:
            report["verdict"] = "block"
            report["violations"].append(f"硬门禁: 意图[{intent}] 准确率 {acc:.0%} < {hard_floor:.0%}")
    if new_overall < baseline_overall - soft_drop:
        report["verdict"] = "block"
        report["violations"].append(
            f"软门禁: 总分回退 {baseline_overall - new_overall:.1%} > {soft_drop:.0%}")
    elif new_overall < baseline_overall:
        report["violations"].append(f"提示: 总分小幅回退 {baseline_overall - new_overall:.1%}")
    return report


if __name__ == "__main__":
    evalset = [{"q": q, "expect": tag, "intent": tag}
               for q, tag in [("退货", "售后"), ("退款", "售后"), ("发票", "售后"),
                              ("物流", "物流"), ("包裹", "物流"),
                              ("你好", "闲聊"), ("天气", "闲聊"), ("笑话", "闲聊")]]
    answers = dict((c["q"], c["expect"]) for c in evalset)

    def old_model(q):
        return f"标准回答含 {answers.get(q)}"

    def new_model(q):
        if q == "笑话":
            return "该功能已升级维护"             # 闲聊层崩塌场景
        return f"新回答含 {answers.get(q)}"

    bd, bo = run_eval(old_model, evalset)
    nd, no = run_eval(new_model, evalset)
    print("基线:", {k: f"{v:.0%}" for k, v in bd.items()}, f"总分 {bo:.0%}")
    print("新版:", {k: f"{v:.0%}" for k, v in nd.items()}, f"总分 {no:.0%}")
    report = gate(bd, bo, nd, no)
    print("门禁结论:", report["verdict"])
    for v in report["violations"]:
        print(" -", v)
    assert report["verdict"] == "block", "闲聊层崩塌必须被拦"
