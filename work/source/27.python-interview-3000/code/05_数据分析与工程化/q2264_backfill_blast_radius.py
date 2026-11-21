"""数据回填的影响面限制: 切片配额, 并发上限与冻结黑名单"""

from datetime import date, timedelta

RANGE = (date(2026, 2, 1), date(2026, 2, 10))   # 待回填 10 天分区
MAX_CONCURRENCY = 2
DAILY_QUOTA = 4                                  # 每个执行日最多 4 个切片
BLACKOUT = (20, 23)                              # 业务高峰 20-23 点不排任务
FREEZE = {date(2026, 2, 6): "大促演练冻结"}       # 冻结日直接跳过

if __name__ == "__main__":
    start, end = RANGE
    days = [start + timedelta(d) for d in range((end - start).days + 1)]
    runnable, skipped = [], []
    for d in days:
        if d in FREEZE:
            skipped.append((d, FREEZE[d]))
        else:
            runnable.append(d)
    batches = [runnable[i:i + DAILY_QUOTA] for i in range(0, len(runnable), DAILY_QUOTA)]
    print(f"待回填 {len(days)} 天, 冻结跳过 {len(skipped)} 天: {[(str(d), r) for d, r in skipped]}")
    print(f"执行分批: {len(batches)} 个执行日, 每日配额 {DAILY_QUOTA} 切片, 单批并发上限 {MAX_CONCURRENCY}")
    for i, b in enumerate(batches, 1):
        print(f"  执行日 {i}: {[str(x) for x in b]}")
    print(f"排程约束: 高峰 {BLACKOUT[0]}-{BLACKOUT[1]} 点不跑; 上线前先干跑输出本计划人工确认")
    print("要点: 回填四限 -- 切片, 每日配额, 并发上限, 黑名单冻结; 影响面先算后跑")
