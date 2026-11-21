"""Q2868 事件溯源的最小实现:追加事件 快照加速与状态重放。

事件溯源的核心承诺:状态 = 初始状态 + 全部事件的折叠。但事件一多
全量重放太慢,标准解法是每隔 N 条落一个快照,重建时从最近快照起
只重放尾部。事件日志不可变,快照只是缓存,错了推倒重算也无妨。
"""

EVENTS = [
    ("open", 100), ("deposit", 50), ("withdraw", 30),
    ("deposit", 10), ("withdraw", 20), ("deposit", 200),
    ("withdraw", 150), ("deposit", 5),
]


def apply(state, event):
    kind, val = event
    if kind == "open":
        return {"balance": val, "ops": 1}
    if kind == "deposit":
        return {"balance": state["balance"] + val, "ops": state["ops"] + 1}
    if kind == "withdraw":
        return {"balance": state["balance"] - val, "ops": state["ops"] + 1}
    raise ValueError("未知事件:" + kind)


def replay_full(events):
    s = None
    for e in events:
        s = apply(s, e)
    return s, len(events)


def replay_from_snapshot(events, snapshots, every=3):
    """snapshots: {已应用事件数: 状态},从最近快照起重放尾部。"""
    starts = [n for n in snapshots if n <= len(events)]
    base_n = max(starts) if starts else 0
    s = snapshots[base_n] if base_n else None
    tail = events[base_n:]
    for e in tail:
        s = apply(s, e)
    return s, base_n + len(tail), base_n


def main():
    full, n = replay_full(EVENTS)
    assert full == {"balance": 165, "ops": 8}, full
    # 追加日志期间每 3 条存一个快照(缓存语义)
    snapshots = {}
    for i in range(3, len(EVENTS) + 1, 3):
        s, _ = replay_full(EVENTS[:i])
        snapshots[i] = s
    assert snapshots[6]["balance"] == 310, snapshots[6]
    # 重建:从快照 6 起只重放 2 条
    s2, applied, base_n = replay_from_snapshot(EVENTS, snapshots, every=3)
    assert base_n == 6 and applied == 8, (base_n, applied)
    assert s2 == full, (s2, full)
    # 事件日志不可变:重放结果永远一致,快照坏了也能重建
    full2, _ = replay_full(EVENTS)
    assert full2 == full
    print("全量重放:", full, "事件数:", n)
    print("快照在 3/6 条处,重建只重放尾部", 8 - 6, "条")
    print("结果一致:", s2 == full2)


if __name__ == "__main__":
    main()
