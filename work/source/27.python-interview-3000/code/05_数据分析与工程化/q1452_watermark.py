"""水位线与迟到数据:事件时间窗口的关闭与迟到修正"""

ALLOWED_LATENESS = 2
WINDOW_SIZE = 5

EVENTS = [
    # 到达顺序: user, event_time, 处理序号
    ("u1", 1, 1), ("u2", 3, 2), ("u3", 4, 3),
    ("u4", 9, 4),               # 推进 watermark 到 7,窗口 [0,5) 关闭
    ("u5", 2, 5),               # 迟到事件,落在已关闭窗口
    ("u6", 6, 6), ("u7", 11, 7),
]


def run(events, allowed_lateness=ALLOWED_LATENESS):
    watermark = float("-inf")
    max_event_time = float("-inf")
    windows = {}
    late = []
    for user, t, seq in events:
        max_event_time = max(max_event_time, t)
        watermark = max_event_time - allowed_lateness
        start = t // WINDOW_SIZE * WINDOW_SIZE
        if watermark >= start + WINDOW_SIZE:
            late.append((user, t, start))  # 窗口已关闭 -> 进侧输出修正
        else:
            windows.setdefault(start, []).append(user)
        print(f"  处理 {user} 事件时间 {t} -> watermark {watermark}")
    return windows, late


if __name__ == "__main__":
    print("按到达顺序处理:")
    windows, late = run(EVENTS)
    print("\n窗口结果:", {k: len(v) for k, v in sorted(windows.items())})
    print("迟到事件:", late)
    print("工程做法:迟到数据写入修正表并与主表 union,保证可重放和可追溯")
