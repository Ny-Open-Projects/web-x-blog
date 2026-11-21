"""管道健康分:时效、完整、一致三项加权,输出 0-100 与分级"""

import datetime as dt

PIPELINES = [
    # name, 计划完成时刻, 实际完成时刻, 期望行数, 实际行数, 主键重复数
    ("ods_order", dt.time(2, 0), dt.time(2, 5), 100000, 99998, 0),
    ("dwd_order", dt.time(3, 0), dt.time(3, 40), 100000, 100000, 12),
    ("ads_funnel", dt.time(4, 0), dt.time(4, 1), 5000, 5000, 0),
]

WEIGHTS = {"freshness": 0.4, "completeness": 0.35, "consistency": 0.25}


def freshness_score(planned, actual, grace_minutes=10):
    """晚于计划即扣分,宽限期外按每分钟线性衰减,60 分钟归零"""
    delay = (dt.datetime.combine(dt.date(2025, 6, 16), actual)
             - dt.datetime.combine(dt.date(2025, 6, 16), planned)).total_seconds() / 60
    if delay <= 0:
        return 1.0
    return max(0.0, 1 - max(0.0, delay - grace_minutes) / 60)


def completeness_score(expected, actual):
    return min(1.0, actual / expected) if expected else 1.0


def consistency_score(dup_keys):
    return 1.0 if dup_keys == 0 else max(0.0, 1 - dup_keys / 1000)


def health_score(row):
    name, planned, actual, expected, actual_rows, dups = row
    parts = {
        "freshness": freshness_score(planned, actual),
        "completeness": completeness_score(expected, actual_rows),
        "consistency": consistency_score(dups),
    }
    total = sum(parts[k] * WEIGHTS[k] for k in parts) * 100
    grade = "A" if total >= 95 else "B" if total >= 85 else "C" if total >= 70 else "D"
    return name, round(total, 1), grade, {k: round(v, 3) for k, v in parts.items()}


if __name__ == "__main__":
    for name, total, grade, parts in map(health_score, PIPELINES):
        print(f"{name}: {total} 分 [{grade}] 明细 {parts}")
    print("健康分进看板并按日趋势展示,连续三天降级要触发治理工单")
