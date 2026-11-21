"""半自动化发布的检查单执行器(纯标准库)。"""


def run_checklist(items, state):
    """items: (名称, 检查函数, 是否阻断)。阻断项失败立即停止并判 no-go。"""
    report, go = [], True
    for name, check, blocking in items:
        try:
            ok, detail = check(state)
        except Exception as exc:                 # 检查项自身抛错按失败处理
            ok, detail = False, "检查项异常: {}".format(exc)
        report.append({"item": name, "ok": ok, "blocking": blocking,
                       "detail": detail})
        print("[{}] {:<14} {}".format("PASS" if ok else "FAIL", name, detail))
        if not ok:
            if blocking:
                go = False
                print("[STOP] 阻断项失败, 终止后续检查, 判定 no-go")
                break
            print("       警告: 非阻断失败, 继续但需人工确认")
    return go, report


def check_tests(state):
    ok = state["tests_green"]
    return ok, "单测与集成全绿" if ok else "存在失败用例"


def check_migration(state):
    ok = state["migration_compatible"]
    return ok, "DDL 向后兼容" if ok else "存在不兼容变更, 旧代码读新库会炸"


def check_config(state):
    ok = state["config_diff_reviewed"]
    return ok, "配置差异已评审" if ok else "配置有未评审差异"


def check_canary(state):
    return state["canary_plan"], "灰度方案就绪" if state["canary_plan"] else "未准备灰度"


ITEMS = [
    ("测试通过", check_tests, True),
    ("迁移兼容", check_migration, True),
    ("配置评审", check_config, False),
    ("灰度方案", check_canary, True),
]

state_bad = {"tests_green": True, "migration_compatible": False,
             "config_diff_reviewed": False, "canary_plan": True}
print("== 场景一: 迁移不兼容 == ")
go, report = run_checklist(ITEMS, state_bad)
assert not go and len(report) == 2, "阻断项失败必须停止后续检查"
assert all(r["item"] != "灰度方案" for r in report)

state_good = {"tests_green": True, "migration_compatible": True,
              "config_diff_reviewed": False, "canary_plan": True}
print("== 场景二: 仅配置未评审 == ")
go2, report2 = run_checklist(ITEMS, state_good)
assert go2 and len(report2) == 4
assert not report2[2]["ok"] and report2[2]["blocking"] is False
print("判定 go, 但配置项需人工确认后发布")
print("要点: 检查单执行器把口头纪律变成可执行流水线, "
      "阻断项短路终止, 非阻断失败降级为警告, 每项产出可存档的检查记录")
