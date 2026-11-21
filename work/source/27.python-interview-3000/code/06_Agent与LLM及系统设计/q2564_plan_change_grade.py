"""Q2564 计划变更的语义分级:结构变更重于参数漂移。

对 Q2563 的 diff 做风险分级:删除被依赖的步骤最危险直接阻断,
新增与参数漂移次之,纯顺序调换最低;总分决定 自动通过 或 人工复核。
"""

RISK = {"added": 1, "changed": 2, "reordered": 1, "removed": 3}


def grade_change(diff, dependents):
    score = 0
    notes = []
    for sid in diff["removed"]:
        blocked = dependents.get(sid, [])
        if blocked:
            score += 5
            notes.append("删除被依赖步骤:" + sid + " 阻断 " + ",".join(blocked))
        else:
            score += RISK["removed"]
            notes.append("删除无依赖步骤:" + sid)
    score += RISK["added"] * len(diff["added"])
    score += RISK["changed"] * len(diff["changed"])
    if diff["reordered"]:
        score += RISK["reordered"]
        notes.append("存在顺序调换")
    verdict = "auto-approve" if score <= 3 else "manual-review"
    return score, verdict, notes


def main():
    diff = {"added": ["s2b"], "removed": ["s2"], "changed": ["s1"], "reordered": True}
    deps = {"s2": ["s3"]}  # s3 依赖 s2 的输出
    score, verdict, notes = grade_change(diff, deps)
    assert score == 5 + 1 + 2 + 1, score
    assert verdict == "manual-review", verdict
    diff2 = {"added": [], "removed": [], "changed": ["s1"], "reordered": False}
    score2, verdict2, _ = grade_change(diff2, deps)
    assert score2 == 2 and verdict2 == "auto-approve"
    print("风险分:", score, "裁决:", verdict)
    for n in notes:
        print(" -", n)
    print("仅参数漂移:", score2, verdict2)


if __name__ == "__main__":
    main()
