"""演练清单执行器:步骤状态机,人工确认门,失败即中止并出报告"""

import time

STEPS = [
    ("预检", lambda: "ok", False),
    ("停写", lambda: "ok", True),      # True = 需人工确认
    ("切流", lambda: "ok", True),
    ("恢复写", lambda: "error: 连接池未释放", False),
    ("验证", lambda: "ok", False),
]
CONFIRM_ANSWERS = ["y", "y"]           # 预置确认应答,模拟人工


def run_drill(steps, answers):
    report, answer_idx = [], 0
    aborted = False
    for step in steps:
        name, action = step[0], step[1]
        need_confirm = len(step) > 2 and step[2]
        if need_confirm:
            ans = answers[answer_idx] if answer_idx < len(answers) else "n"
            answer_idx += 1
            if ans != "y":
                report.append((name, "SKIPPED", "人工未确认", ""))
                aborted = True
                break
        t0 = time.perf_counter()
        result = str(action())
        cost = time.perf_counter() - t0
        if result.startswith("error"):
            report.append((name, "FAILED", result, f"{cost:.4f}s"))
            aborted = True
            break
        report.append((name, "PASSED", result, f"{cost:.4f}s"))
    status = "ABORTED" if aborted else "PASSED"
    return report, status


if __name__ == "__main__":
    report, status = run_drill(STEPS, CONFIRM_ANSWERS)
    print(f"演练结论: {status}")
    for r in report:
        print("  ", " ".join(x for x in r if x))
    print("要点:演练步骤有 passed/failed/skipped 三态,失败即停不硬跑后面的步骤;确认门保证高危动作必须有人点头;报告留档供复盘与下次演练对照")
