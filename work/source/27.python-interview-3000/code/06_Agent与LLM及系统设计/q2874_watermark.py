"""Q2874 乱序事件的水位线:窗口推进 迟到处理与收尾冲刷。

多分区流式系统里,事件到达顺序和事件时间顺序无关。水位线取各分区
最大事件时间的最小值:水位没过窗口末沿,窗口不敢出结果;水位一过,
窗口立即触发;水位之后才姗姗来迟的事件,只能进迟到清单另行处理。
"""

from collections import defaultdict


def run_watermark(events, window, partitions):
    """events: [(partition, ts, payload)],返回 (触发, 迟到, 未触发)。"""
    last = {p: -1 for p in partitions}
    wm_seen = 0
    buffered = defaultdict(list)
    fired = []
    late = []
    for p, ts, payload in events:
        if ts < wm_seen:               # 早于已推进的水位:迟到
            late.append(payload)
            continue
        last[p] = max(last[p], ts)
        start = ts // window
        buffered[start].append(payload)
        wm = min(last[p] for p in partitions)
        for s in sorted(list(buffered)):
            if (s + 1) * window <= wm:
                fired.append((s, buffered.pop(s)))
        wm_seen = max(wm_seen, wm)
    return fired, late, dict(buffered)


def main():
    parts = ("p0", "p1", "p2")
    events = [
        ("p0", 5, "A"),
        ("p1", 12, "B"),
        ("p2", 18, "C"),
        ("p0", 25, "D"),
        ("p1", 3, "E"),    # p1 乱序回退,且水位已过 10:迟到
        ("p2", 40, "F"),
        ("p1", 30, "G"),
    ]
    fired, late, pending = run_watermark(events, window=10, partitions=parts)
    assert fired[0] == (0, ["A"]), fired    # 水位到 12,窗口 0 立即触发
    assert (1, ["B", "C"]) in fired, fired  # 水位到 25 后窗口 1 触发
    assert late == ["E"], late              # 水位已过 10,E 只能记迟到
    assert pending == {2: ["D"], 3: ["G"], 4: ["F"]}, pending  # 等水位
    assert len(fired) == 2, fired
    print("已触发窗口:", fired)
    print("迟到事件:", late)
    print("未触发窗口 2/3/4 在等水位,最慢分区 p0 停在 25 不敢出结果")


if __name__ == "__main__":
    main()
