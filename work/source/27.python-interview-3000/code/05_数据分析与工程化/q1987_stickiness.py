"""DAU/MAU 粘性比:滚动窗口口径与自然期口径的差异"""

ACTIVE = {
    1: {"u1", "u2", "u3", "u4"},
    2: {"u1", "u2", "u5"},
    3: {"u1", "u3", "u6", "u7", "u8"},
    4: {"u1", "u2", "u3"},
    5: {"u1", "u4", "u9"},
    6: {"u1", "u10", "u11", "u12"},
    7: {"u1", "u2", "u3", "u13"},
}
WINDOW = 5  # 演示用 5 天窗口,生产 MAU 用滚动 30 天


def rolling_mau(active, day, window):
    s = set()
    for d in range(day - window + 1, day + 1):
        s |= active.get(d, set())
    return s


if __name__ == "__main__":
    for day in sorted(ACTIVE):
        dau = len(ACTIVE[day])
        mau = rolling_mau(ACTIVE, day, WINDOW)
        print(f"第{day}天 DAU={dau:>2}  滚动{WINDOW}日 MAU={len(mau):>2}  粘性比 {dau / len(mau):.2f}")
    last = max(ACTIVE)
    all_users = set().union(*ACTIVE.values())
    print(f"自然期口径:整期去重 {len(all_users)} 人,末日粘性比 {len(ACTIVE[last]) / len(all_users):.2f}")
    print("要点:MAU 要逐日滚动重算而不是自然月一次;粘性比看趋势不看绝对值,跌一半常见于拉新带来的分母膨胀")
