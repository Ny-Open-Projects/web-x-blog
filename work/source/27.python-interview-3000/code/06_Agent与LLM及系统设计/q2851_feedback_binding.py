"""Q2851 点踩反馈的归因绑定:反馈必须关联回检索轨迹。

孤立的一个点踩没有价值:不知道当时喂了哪些来源 用的哪些块,就定位
不了是检索的锅还是生成的锅。反馈事件必须绑定检索轨迹,按来源聚合
负反馈,「哪个来源总在贡献坏答案」自然浮出水面。
"""


def bind_feedback(feedbacks, traces):
    """feedbacks: [{answer_id, vote}],traces: {answer_id: {sources}}。"""
    per_source = {}
    orphan = []
    for fb in feedbacks:
        tr = traces.get(fb["answer_id"])
        if not tr:
            orphan.append(fb)
            continue
        kind = "down" if fb["vote"] < 0 else "up"
        for s in tr["sources"]:
            slot = per_source.setdefault(s, {"up": 0, "down": 0})
            slot[kind] += 1
    return per_source, orphan


def main():
    traces = {
        "a1": {"sources": ["help.example.com", "forum.example.com"]},
        "a2": {"sources": ["forum.example.com"]},
        "a3": {"sources": ["help.example.com"]},
    }
    feedbacks = [
        {"answer_id": "a1", "vote": -1},
        {"answer_id": "a2", "vote": -1},
        {"answer_id": "a3", "vote": 1},
        {"answer_id": "a9", "vote": -1},   # 轨迹丢失,无法归因
    ]
    per_source, orphan = bind_feedback(feedbacks, traces)
    assert per_source == {
        "help.example.com": {"up": 1, "down": 1},
        "forum.example.com": {"up": 0, "down": 2},
    }, per_source
    assert orphan == [{"answer_id": "a9", "vote": -1}], orphan
    forum = per_source["forum.example.com"]
    assert forum["down"] == 2 and forum["up"] == 0, forum
    print("来源级聚合:", per_source)
    print("论坛来源 0 赞 2 踩,进入语料治理清单")
    print("无法归因的反馈单独留痕:", orphan)


if __name__ == "__main__":
    main()
