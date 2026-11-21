"""数据测试分级门禁:blocker 一票否决,warn 超量同样拦截"""

CHECK_RESULTS = [
    # 检查名, 严重级别, 是否通过
    ("行数波动 < 5%", "blocker", True),
    ("主键唯一", "blocker", False),
    ("空值率 < 1%", "warn", False),
    ("枚举值合法", "warn", False),
    ("更新时间戳新鲜", "info", True),
]

WARN_LIMIT = 1


def gate(results, warn_limit=WARN_LIMIT):
    blocker_fail = [n for n, sev, ok in results if sev == "blocker" and not ok]
    warn_fail = [n for n, sev, ok in results if sev == "warn" and not ok]
    info_fail = [n for n, sev, ok in results if sev == "info" and not ok]
    blocked = bool(blocker_fail) or len(warn_fail) > warn_limit
    reasons = []
    if blocker_fail:
        reasons.append("阻断级失败: " + ", ".join(blocker_fail))
    if len(warn_fail) > warn_limit:
        reasons.append(f"警告级失败 {len(warn_fail)} 项超过阈值 {warn_limit}")
    return {"decision": "BLOCK" if blocked else "PASS",
            "blocker_fail": blocker_fail, "warn_fail": warn_fail,
            "info_fail": info_fail, "reasons": reasons}


if __name__ == "__main__":
    r = gate(CHECK_RESULTS)
    print("决策:", r["decision"])
    for reason in r["reasons"]:
        print("  理由:", reason)
    print("随附警告:", ", ".join(r["warn_fail"]) or "无")
    print("要点:分级让门禁既有牙齿又不至于草木皆兵,阈值要和团队约定并文档化")
