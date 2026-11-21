"""Q2568 锚点的自动选取与失锚检测:定义被逐出要能报警并回捞。

重要性加近因性给消息打分,分高的自动钉成锚点;被保留消息引用了
某个术语,而该术语的定义消息已被逐出,就是失锚,要从归档回捞重钉。
"""
import re

WEIGHT = {"goal": 5.0, "constraint": 4.0, "fact": 2.0, "chat": 1.0}


def score(msg, turn):
    return WEIGHT.get(msg["kind"], 1.0) + max(0.0, 3.0 - (turn - msg["turn"]))


def pick_anchors(history, turn, k):
    ranked = sorted(history, key=lambda m: -score(m, turn))
    return {m["id"] for m in ranked[:k]}


def detect_lost_anchor(kept, evicted):
    defined = {}
    for m in evicted:
        found = re.search(r"定义[:：](\w+)", m["text"])
        if found:
            defined[found.group(1)] = m["id"]
    lost = []
    for m in kept:
        for term, src in defined.items():
            if term in m["text"] and m["id"] != src:
                lost.append((m["id"], term, src))
    return lost


def main():
    history = [
        {"id": "m1", "kind": "goal", "turn": 1, "text": "目标:输出季度复盘"},
        {"id": "m2", "kind": "constraint", "turn": 2, "text": "定义:ACV 为年度合同额"},
        {"id": "m3", "kind": "chat", "turn": 3, "text": "再聊聊 ACV 口径"},
        {"id": "m4", "kind": "chat", "turn": 4, "text": "ACV 记不算服务费"},
    ]
    anchors = pick_anchors(history, turn=4, k=1)
    assert anchors == {"m1"}, anchors
    kept = [m for m in history if m["id"] in anchors] + [history[3]]
    kept_ids = {m["id"] for m in kept}
    evicted = [m for m in history if m["id"] not in kept_ids]
    assert {m["id"] for m in evicted} == {"m2", "m3"}, evicted
    lost = detect_lost_anchor(kept, evicted)
    assert lost == [("m4", "ACV", "m2")], lost
    print("自动锚点:", sorted(anchors), "→ 定义消息 m2 被逐出")
    print("失锚检测:", lost, "→ 从归档回捞 m2 重新钉住")


if __name__ == "__main__":
    main()
