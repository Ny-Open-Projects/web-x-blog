"""发布后的自动回滚判定: 连续窗口与硬上限"""

WINDOWS = [
    # 观察窗口, 错误率, p99 延迟 ms
    ("W1", 0.002, 210), ("W2", 0.004, 230), ("W3", 0.011, 260),
    ("W4", 0.012, 250), ("W5", 0.013, 240), ("W6", 0.013, 235),
]
ERR_SOFT, ERR_HARD = 0.005, 0.015
LAT_HARD = 400
CONSECUTIVE = 3


def decide(windows):
    streak = 0
    for name, err, lat in windows:
        if err > ERR_HARD or lat > LAT_HARD:
            return name, f"硬上限击穿: 错误率 {err:.1%} 或 p99 {lat}ms 越红线, 立即回滚"
        streak = streak + 1 if err > ERR_SOFT else 0
        if streak >= CONSECUTIVE:
            return name, f"错误率连续 {streak} 个窗口高于 {ERR_SOFT:.1%}, 判定劣化成立, 自动回滚"
    return windows[-1][0], "观察期结束未触发回滚条件, 发布单正常关闭"


if __name__ == "__main__":
    for name, err, lat in WINDOWS:
        print(f"{name}: 错误率 {err:.1%} p99 {lat}ms")
    w, reason = decide(WINDOWS)
    print(f"决策: 在 {w} 触发 -> {reason}")
    print("要点: 连续性滤噪声, 硬上限防灾难; 触发后进冷却期禁止自动再发布; 误报率先用演练数据验证")
