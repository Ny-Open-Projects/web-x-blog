"""多源档案合并: 字段级优先级与新鲜度仲裁"""

PROFILES = {
    # 字段 -> [(来源, 值, 优先级, 更新批次)]
    "phone": [("crm", "138****", 3, "d5"), ("app", "139****", 2, "d1"), ("3rd", "137****", 1, "d2")],
    "city": [("crm", None, 3, "d5"), ("app", "杭州", 2, "d1"), ("3rd", "上海", 1, "d3")],
    "vip_level": [("crm", "gold", 3, "d5"), ("app", "silver", 2, "d1")],
}


def merge(records, min_priority=0):
    """优先级高者胜, 同级取更新者, 空值跳过"""
    valid = [r for r in records if r[1] is not None and r[2] >= min_priority]
    if not valid:
        return None, "无可用来源"
    valid.sort(key=lambda r: (-r[2], r[3]))
    return valid[0][1], f"来源 {valid[0][0]} 优先级 {valid[0][2]} 批次 {valid[0][3]}"


if __name__ == "__main__":
    for field, records in PROFILES.items():
        value, why = merge(records)
        print(f"{field:<10} -> {str(value):<10} ({why})")
    print("city 只信 App 及以上来源:", merge(PROFILES['city'], min_priority=2)[0])
    print("要点: 规则按字段配置; 每字段留来源与时间戳可回放; 空值永远让位, 三方来源默认最低级")
