"""管道告警的三级阈值: 持续时间条件与回滞"""

SERIES = [55, 82, 85, 91, 93, 88, 92, 96, 70, 65]
WARN, CRIT, PAGE = 80, 90, 95
CRIT_SUSTAIN = 2      # 连续 2 个周期超 90 才升级 CRITICAL
CLEAR = 70            # 回滞: 低于 70 才解除


def evaluate(series):
    level, over = "正常", 0
    log = []
    for i, v in enumerate(series):
        if v > PAGE:
            level = "PAGE"
        elif v > CRIT:
            over += 1
            level = "CRITICAL" if over >= CRIT_SUSTAIN else "WARN"
        elif v > WARN:
            level, over = "WARN", 0
        elif v <= CLEAR:
            level, over = "正常", 0
        # WARN 与 CLEAR 之间保持原级别, 这就是回滞带
        log.append((i, v, level))
    return log


if __name__ == "__main__":
    for i, v, level in evaluate(SERIES):
        print(f"周期 {i}: 值 {v:>3} -> {level}")
    print("要点: 单点越线只 WARN, 持续越线才升级; 恢复用更低回滞线, 否则在阈值附近乒乓刷屏")
