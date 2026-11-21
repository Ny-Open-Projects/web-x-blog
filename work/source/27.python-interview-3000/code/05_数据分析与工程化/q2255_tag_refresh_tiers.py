"""用户标签的更新频率分层: 新鲜度 SLA 与成本匹配"""

import math

# 标签, 刷新方式, 新鲜度 SLA 天, 更新成本相对值
TAGS = [
    ("风险分", "实时触发", 0.5, 10),
    ("最近活跃档", "每日批", 1, 3),
    ("品类偏好", "每周批", 7, 2),
    ("生命周期", "每月批", 30, 5),
]
EVENT_DAYS = [0, 1, 2, 3, 5, 8, 13, 21, 34]   # 用户行为发生的日期偏移
BATCH_DAYS = {"每日批": 1, "每周批": 7, "每月批": 30}


def worst_staleness(mode, event_days):
    """批处理: 事件要等下一个批周期才可见, 返回最坏陈旧天数"""
    if mode == "实时触发":
        return 0
    step = BATCH_DAYS[mode]
    worst = 0
    for d in event_days:
        visible = math.ceil((d + 1) / step) * step
        worst = max(worst, visible - d)
    return worst


if __name__ == "__main__":
    print(f"{'标签':<8}{'刷新方式':<8}{'最坏陈旧':>8}{'SLA':>6}{'成本':>5}  判定")
    for name, mode, sla, cost in TAGS:
        worst = worst_staleness(mode, EVENT_DAYS)
        ok = worst <= sla
        print(f"{name:<8}{mode:<8}{worst:>6}天{sla:>5}天{cost:>5}  {'达标' if ok else '超时: 提频或改触发'}")
    print("设计规则: 频率跟决策场景走, 能批不实时; 标签值突变可插队触发刷新, 成本与时效兼顾")
