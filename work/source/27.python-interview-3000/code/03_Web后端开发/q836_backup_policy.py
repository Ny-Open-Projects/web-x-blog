
POLICY = {
    "全量": "每日一次, 加密后异地对象存储",
    "增量与归档": "WAL 连续归档, RPO 分钟级",
    "保留": "7 天日备 + 4 周周备 + 12 月月备",
    "演练": "每季度隔离环境恢复并跑数据校验脚本",
}

def rpo_rto(rpo_min: int, rto_min: int) -> str:
    return f"RPO {rpo_min} 分钟, RTO {rto_min} 分钟"

for k, v in POLICY.items():
    print(f"{k}: {v}")
print(rpo_rto(5, 30))
