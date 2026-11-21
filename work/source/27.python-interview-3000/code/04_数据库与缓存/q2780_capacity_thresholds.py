"""容量预警的三色阈值: 滞回状态机 + 剩余天数加速定级"""
def classify(pct, days_left, prev):
    if pct >= 85 or days_left <= 7:
        return "RED"
    if prev == "RED":                          # 红色降档更苛刻, 防抖
        if pct < 80 and days_left > 7:
            return "YELLOW" if pct >= 65 else "GREEN"
        return "RED"
    if pct >= 70 or days_left <= 30:
        return "YELLOW"
    if prev == "YELLOW":
        return "GREEN" if (pct < 65 and days_left > 30) else "YELLOW"
    return "GREEN"

series = [
    (60, 90, None),      # 正常
    (72, 40, None),      # 升黄
    (66, 40, "YELLOW"),  # 回落但未过降档阈值, 滞回保持黄
    (64, 40, "YELLOW"),  # 过降档阈值, 回绿
    (88, 40, None),      # 直升红
    (82, 40, "RED"),     # 未过红色降档线, 保持红
    (78, 40, "RED"),     # 降到黄
    (50, 5,  "YELLOW"),  # 水位不高但 5 天就满, 剩余天数加速直判红
]
for pct, days, prev in series:
    print("水位 %2d%%, 剩余 %2d 天, 上一状态 %-6s -> %s"
          % (pct, days, prev or "-", classify(pct, days, prev)))
