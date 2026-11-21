
def remaining_budget(budget_minutes: float, used_minutes: float) -> float:
    return 1 - used_minutes / budget_minutes

month_min = 30 * 24 * 60
slo = 0.999
budget_min = month_min * (1 - slo)
print("月错误预算分钟:", round(budget_min, 1))
left = remaining_budget(budget_min, 10)
print("已用 10 分钟后剩余比例:", round(left, 3))
print("决策:", "冻结发布" if left <= 0 else "可继续发布")
