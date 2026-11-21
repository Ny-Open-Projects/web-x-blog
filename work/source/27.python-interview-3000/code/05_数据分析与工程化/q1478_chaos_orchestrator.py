"""混沌用例编排器:注入 -> 断言 -> 恢复验证,产出演练报告"""

import time

CASES = [
    {
        "name": "下游超时 30 秒",
        "inject": lambda: "timeout_30s",
        "expect": lambda state: state.get("retry_ok") is True,
        "recover": lambda: "healthy",
    },
    {
        "name": "磁盘写满",
        "inject": lambda: "disk_full",
        "expect": lambda state: state.get("degraded_but_alive") is True,
        "recover": lambda: "healthy",
    },
]


def run_case(case):
    fault = case["inject"]()
    state = {}
    if fault == "timeout_30s":
        state["retry_ok"] = True          # 被测系统按设计应重试成功
        state["degraded_but_alive"] = True
    elif fault == "disk_full":
        state["retry_ok"] = False
        state["degraded_but_alive"] = True  # 预期: 降级但不崩溃
    time.sleep(0.02)
    passed = case["expect"](state)
    recovered = case["recover"]() == "healthy"
    return {"name": case["name"], "fault": fault,
            "assertion": passed, "recovered": recovered}


def orchestrate(cases):
    report = [run_case(c) for c in cases]
    for r in report:
        verdict = "PASS" if r["assertion"] and r["recovered"] else "FAIL"
        print(f"[{verdict}] {r['name']} 注入={r['fault']} "
              f"断言={r['assertion']} 恢复={r['recovered']}")
    print("要点:混沌用例三要素=注入点、可执行断言、恢复验证;FAIL 要开治理项")


if __name__ == "__main__":
    orchestrate(CASES)
