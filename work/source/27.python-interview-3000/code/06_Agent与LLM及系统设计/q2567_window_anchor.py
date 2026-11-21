"""Q2567 长会话的滚动窗口加锚点:窗口滑动但关键帧不丢。

朴素滚动窗口会把系统规则、任务目标一并挤掉;给关键消息打锚点,
逐出时锚点豁免,宁可短暂超窗也不丢关键帧。
"""


def advance(history, anchors, new_msg, window):
    """追加消息并按窗口逐出最旧的非锚点消息,返回被逐出的 id 列表。"""
    history.append(dict(new_msg))
    evicted = []
    while len(history) > window:
        idx = next((i for i, m in enumerate(history) if m["id"] not in anchors), None)
        if idx is None:
            break  # 窗口内全是锚点:宁可超窗也不丢锚
        evicted.append(history.pop(idx)["id"])
    return evicted


def main():
    history = [{"id": "m1", "text": "系统规则"}]
    anchors = {"m1"}
    for i in range(2, 8):
        ev = advance(history, anchors, {"id": "m" + str(i), "text": "对话" + str(i)}, window=4)
    ids = [m["id"] for m in history]
    assert "m1" in ids, ids            # 锚点在多轮滚动后仍在
    assert len(ids) <= 4, ids
    # 中途把 m6 钉成锚点,再滚 4 轮,m6 依然幸存
    anchors.add("m6")
    for i in range(8, 12):
        advance(history, anchors, {"id": "m" + str(i), "text": "对话" + str(i)}, window=4)
    ids2 = [m["id"] for m in history]
    assert "m1" in ids2 and "m6" in ids2, ids2
    print("第一轮保留:", ids)
    print("钉住 m6 后保留:", ids2, "← 两个锚点都幸存")


if __name__ == "__main__":
    main()
