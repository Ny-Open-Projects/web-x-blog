"""数据质量指标: 完整性 / 唯一性 / 一致性三维评分"""
rows = [
    {"uid": 1, "phone": "138", "status": "PAID"},
    {"uid": 2, "phone": None, "status": "paid"},
    {"uid": 2, "phone": "139", "status": "PAID"},   # uid 与 email 双重问题
    {"uid": 4, "phone": "137", "status": None},
]
completeness = sum(1 for r in rows if r["phone"] is not None) / len(rows)
uids = [r["uid"] for r in rows]
uniqueness = len(set(uids)) / len(uids)
valid = {"PAID", "PENDING", "FAILED"}
consistency = sum(1 for r in rows if r["status"] in valid) / len(rows)
score = (completeness + uniqueness + consistency) / 3
for name, v in (("完整性", completeness), ("唯一性", uniqueness), ("一致性", consistency)):
    print(f"{name}: {v:.0%}")
print(f"综合质量分: {score:.0%} <- 低于阈值触发治理工单, 趋势比单值重要")
