
METRIC_REGISTRY = {
    "pay_conversion_rate": {
        "formula": "pay_users / view_users",
        "grain": "day + city",
        "owner": "growth-team",
        "freshness": "T+1",
        "source_table": "dws_user_event_day",
    },
    "avg_order_value": {
        "formula": "sum(amount) / count(order_id)",
        "grain": "day",
        "owner": "trade-team",
        "freshness": "T+1",
        "source_table": "dws_trade_day",
    },
}

def describe(name):
    m = METRIC_REGISTRY[name]
    return f"{name} = {m['formula']} 粒度 {m['grain']} 负责人 {m['owner']} 新鲜度 {m['freshness']}"

for n in METRIC_REGISTRY:
    print(describe(n))
print("报表与看板统一从注册表读定义,禁止在 SQL 里各自手写口径")
