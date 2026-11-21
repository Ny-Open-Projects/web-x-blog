"""扫描预算守卫: 估算超预算即拒跑, 放行必须显式"""


class BudgetExceeded(Exception):
    """预估扫描量超过预算"""


ROWS_PER_PARTITION = 8000
BUDGET_ROWS = 20000


def estimate(partitions):
    return len(partitions) * ROWS_PER_PARTITION


def guard(plan, budget=BUDGET_ROWS, allow_over_budget=False):
    est = estimate(plan)
    if est <= budget:
        return f"放行: 预估扫描 {est} 行 <= 预算 {budget} 行"
    if allow_over_budget:
        return f"警告: 预估 {est} 行超预算 {budget} 行, 已显式放行并留痕"
    raise BudgetExceeded(
        f"预估扫描 {est} 行超出预算 {budget} 行, 建议: 缩小日期区间 / 提高分区粒度 / 显式 allow_over_budget")


if __name__ == "__main__":
    wide = ["2026-03-01", "2026-03-02", "2026-03-03"]
    narrow = wide[:2]
    try:
        guard(wide)
    except BudgetExceeded as e:
        print("预算守卫拒绝:", e)
    else:
        raise AssertionError("超预算必须拒绝")
    print(guard(narrow))
    print(guard(wide, allow_over_budget=True))
    assert "警告" in guard(wide, allow_over_budget=True)
    print("要点: 守卫把成本事故前移到提交时, 超预算是常态化的诱惑, 放行必须留下显式痕迹")
