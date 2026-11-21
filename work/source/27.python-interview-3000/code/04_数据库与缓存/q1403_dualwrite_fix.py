"""双写不一致的批量修复: 以源库为准生成差异并订正"""
old_db = {
    1001: {"amount": 9900, "status": "paid"},
    1002: {"amount": 2500, "status": "pending"},
    1003: {"amount": 180, "status": "paid"},
    1004: {"amount": 6600, "status": "paid"},
}
new_db = {
    1001: {"amount": 9900, "status": "paid"},
    1002: {"amount": 2500, "status": "paid"},   # 状态漂移
    1003: {"amount": 1800, "status": "paid"},   # 金额多写一个 0
    1005: {"amount": 500, "status": "paid"},    # 新库多出行
}

def audit(src, dst):
    drift, missing = [], []
    for k, v in src.items():
        if k not in dst:
            missing.append(k)
        elif dst[k] != v:
            drift.append(k)
    extra = [k for k in dst if k not in src]
    return drift, missing, extra

drift, missing, extra = audit(old_db, new_db)
print("漂移:", drift, "新库缺失:", missing, "新库多余:", extra)
fixed = 0
for k in drift + missing:
    new_db[k] = dict(old_db[k])       # 以源库为权威
    fixed += 1
for k in extra:
    new_db.pop(k)
    fixed += 1
print(f"订正 {fixed} 行; 复检结果: {audit(old_db, new_db)}")
print("修复必须幂等可重跑: 带批次号与时间戳, 防止覆盖窗口期的合法新写入")
