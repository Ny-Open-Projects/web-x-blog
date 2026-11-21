
WINDOW_DAYS = 30
SLO = 99.9
TOTAL_MIN = WINDOW_DAYS * 24 * 60
BUDGET_MIN = TOTAL_MIN * (1 - SLO / 100)

bad_minutes_7d = 30
burn_rate = (bad_minutes_7d / (7 * 24 * 60)) / (1 - SLO / 100)

print(f"30 天总分钟 {TOTAL_MIN:,},错误预算 {BUDGET_MIN:.1f} 分钟")
print(f"近 7 天不可用 {bad_minutes_7d} 分钟,burn rate {burn_rate:.1f}x")
if burn_rate > 6:
    print("动作:P0,冻结发布全力救火")
elif burn_rate > 1:
    print("动作:关注,减少非关键变更")
else:
    print("健康,可正常迭代")
