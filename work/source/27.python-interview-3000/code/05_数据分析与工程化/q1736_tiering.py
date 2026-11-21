"""分区生命周期:按年龄分层并生成迁移动作,删除前必须校验归档完成"""

from datetime import date, timedelta

TODAY = date(2025, 10, 28)
HOT_DAYS, WARM_DAYS = 90, 365


def tier_of(dt):
    age = (TODAY - dt).days
    if age <= HOT_DAYS:
        return "hot"
    if age <= WARM_DAYS:
        return "warm"
    return "cold"


def archived_ok(dt):
    """演示:假设 2025 之前分区已归档且校验和比对通过"""
    return dt < date(2025, 1, 1)


def actions(partitions):
    plan = []
    for dt in partitions:
        t = tier_of(dt)
        if t == "warm":
            plan.append((dt, "压缩并迁到温存储"))
        elif t == "cold":
            if archived_ok(dt):
                plan.append((dt, "从集群删除"))
            else:
                plan.append((dt, "先归档到对象存储并校验,再删除"))
    return plan


if __name__ == "__main__":
    partitions = [date(2024, 5, 1) + timedelta(days=30 * i) for i in range(18)]
    for dt, act in actions(partitions):
        print(f"  {dt} [{tier_of(dt)}] -> {act}")
    print("要点:分层动作必须是状态机不是定时强删——hot 压缩、warm 归档、cold 校验副本与校验和后才删除;删除永远 dry-run 先行")
