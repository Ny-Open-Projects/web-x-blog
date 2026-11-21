"""长查询的分级熔断: 连接秒级失败 语句限时 连续超时即断路"""

MAX_CONSECUTIVE = 3


class BreakerOpen(Exception):
    """熔断打开, 快速失败"""


def make_query(behavior):
    """模拟查询函数: behavior 依次决定每次调用 ok 或 timeout"""
    calls = {"n": 0}

    def query():
        i = calls["n"]
        calls["n"] += 1
        if i >= len(behavior):
            return "ok"
        if behavior[i] == "timeout":
            raise TimeoutError("语句超时")
        return "ok"

    return query, calls


def run_with_breaker(query, breaker_state):
    if breaker_state["open"]:
        raise BreakerOpen("熔断打开中, 不发查询, 快速失败等冷却")
    try:
        result = query()
        breaker_state["consecutive_timeouts"] = 0
        return result
    except TimeoutError:
        breaker_state["consecutive_timeouts"] += 1
        if breaker_state["consecutive_timeouts"] >= MAX_CONSECUTIVE:
            breaker_state["open"] = True
        raise


if __name__ == "__main__":
    query, calls = make_query(["timeout", "timeout", "timeout", "ok"])
    state = {"open": False, "consecutive_timeouts": 0}
    for i in range(3):
        try:
            run_with_breaker(query, state)
        except TimeoutError:
            print(f"第 {i + 1} 次语句超时, 连续计数 {state['consecutive_timeouts']}")
    assert state["open"], "连续 3 次超时应触发熔断"
    before = calls["n"]
    try:
        run_with_breaker(query, state)
    except BreakerOpen as e:
        print("熔断拦截:", e, f"-> 查询函数未被调用(调用数仍为 {calls['n']})")
    assert calls["n"] == before, "熔断打开后不得再碰依赖"
    print("要点: L1 连接超时保护建连, L2 语句超时保护单查, L3 熔断保护整个依赖, 逐级收窄爆炸半径")
