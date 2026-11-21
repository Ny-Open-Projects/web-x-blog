"""影子运行: 新逻辑双跑对账, 达标才切流"""

DAYS = [
    # 天, GMV 相对差, 订单数相对差, 明细行数差
    ("D1", 0.0082, -0.0004, 0),
    ("D2", 0.0031, -0.0002, 0),
    ("D3", 0.0006, 0.0000, 0),
    ("D4", -0.0004, 0.0001, 0),
    ("D5", 0.0002, 0.0000, 0),
    ("D6", 0.0001, 0.0000, 0),
    ("D7", 0.0000, 0.0000, 0),
]
TOL = 0.005
NEED = 5   # 连续达标天数门槛建议


def gate(days, tol, need):
    streak = 0
    for day, gmv, order, rows in days:
        ok = abs(gmv) <= tol and abs(order) <= tol and rows == 0
        streak = streak + 1 if ok else 0
        print(f"{day}: GMV差 {gmv:+.2%} 订单差 {order:+.2%} -> "
              f"{'达标' if ok else '超标'} 连续达标 {streak}/{need}")
    return streak >= need


if __name__ == "__main__":
    promote = gate(DAYS, TOL, NEED)
    print(f"切流判定: {'通过, 可切换读端' if promote else '未通过, 继续双跑并归因超标天'}")
    print("要点: 新逻辑写影子表零影响; 对账含总量与行数; 差异先归因再切流, 预期差异进台账")
