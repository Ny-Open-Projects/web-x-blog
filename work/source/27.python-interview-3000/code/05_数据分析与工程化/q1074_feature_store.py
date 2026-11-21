import math

def featurize(raw):
    """唯一转换入口:离线批量与在线单条共用,保证训练与推理一致"""
    return {
        "amount_log1p": round(math.log1p(raw["amount"]), 6),
        "recent_7d_cnt": raw.get("recent_7d_cnt", 0),
        "is_new_user": 1 if raw["orders_total"] <= 1 else 0,
    }

offline = {"amount": 200.0, "orders_total": 3, "recent_7d_cnt": 2}
online = {"amount": 200.0, "orders_total": 3, "recent_7d_cnt": 2}
assert featurize(offline) == featurize(online)
print("同一函数保证 offline 与 online 特征一致:", featurize(online))
print("特征存储本质:离线批查 + 在线点查双通道,共用变换、血缘与版本")
