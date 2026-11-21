"""用户生命周期阶段划分:近因 x 消费的状态机"""

USERS = [
    # user_id, 注册至今天数, 最近一次活跃距今天数, 近90天订单数, 近90天消费
    ("u1", 15, 1, 1, 50),
    ("u2", 90, 3, 6, 900),
    ("u3", 400, 10, 20, 5000),
    ("u4", 200, 45, 3, 200),
    ("u5", 500, 120, 10, 3000),
    ("u6", 60, 8, 0, 0),
]


def stage(days_since_register, days_since_active, orders_90d, spend_90d):
    if days_since_active > 90:
        return "churned 流失"
    if days_since_active > 30:
        return "sleeping 沉睡"
    if orders_90d >= 10 or spend_90d >= 3000:
        return "mature 成熟"
    if days_since_register <= 30:
        return "new 新手"
    return "growing 成长"


if __name__ == "__main__":
    counts = {}
    for uid, reg, act, orders, spend in USERS:
        s = stage(reg, act, orders, spend)
        counts[s] = counts.get(s, 0) + 1
        print(f"{uid}: {s}")
    print("阶段分布:", counts)
    print("关键规则:先判流失再判成熟,避免'高消费但已流失'被误标为成熟")
