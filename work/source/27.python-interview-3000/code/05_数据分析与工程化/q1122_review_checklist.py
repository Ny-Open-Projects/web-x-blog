
def review(pr):
    issues = []
    if pr["additions"] + pr["deletions"] > 400:
        issues.append("改动超过 400 行,建议拆分 PR")
    if pr["logic_touched"] and not pr["tests_changed"]:
        issues.append("改了逻辑但没动测试")
    if pr["title"] == "update":
        issues.append("标题无信息量,写清动机与影响面")
    if not pr["rollback_note"]:
        issues.append("缺少回滚说明")
    return issues or ["LGTM"]

PR = {"title": "update", "additions": 520, "deletions": 30,
      "tests_changed": False, "logic_touched": True, "rollback_note": ""}
for line in review(PR):
    print("-", line)
