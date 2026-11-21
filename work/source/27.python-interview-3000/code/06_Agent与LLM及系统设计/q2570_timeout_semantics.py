"""Q2570 超时的失败语义:部分结果也要有结构化的身份。

子任务超时不该只是抛异常:能部分交付的任务返回 partial 加已得
条目,父端按最低需求决定收下还是丢弃;全有或全无的任务超时即
失败,父端捕获后跳过并继续,绝不让一个子任务拖垮整棵树。
"""


class Clock:
    def __init__(self):
        self.t = 0.0

    def advance(self, dt):
        self.t += dt
        return self.t


def run_child(clock, deadline, per_item, limit):
    items = []
    while True:
        if clock.t + per_item > deadline:
            return {"status": "partial", "items": items, "spent": clock.t}
        clock.advance(per_item)
        items.append(len(items) + 1)
        if len(items) >= limit:
            return {"status": "done", "items": items, "spent": clock.t}


def handle(result, min_needed):
    if result["status"] == "done":
        return "accept-full"
    if result["status"] == "partial" and len(result["items"]) >= min_needed:
        return "accept-partial"
    return "skip"


def main():
    clock = Clock()
    r1 = run_child(clock, deadline=2.5, per_item=1.0, limit=10)
    assert r1["status"] == "partial" and r1["items"] == [1, 2], r1
    assert handle(r1, min_needed=2) == "accept-partial"
    clock2 = Clock()
    r2 = run_child(clock2, deadline=2.5, per_item=1.0, limit=2)
    assert r2["status"] == "done"
    assert handle(r2, min_needed=2) == "accept-full"
    assert handle(r1, min_needed=3) == "skip"  # 部分结果太少也不收
    # 不可部分交付的任务:超时即失败,父端捕获并跳过
    verdict = None
    try:
        raise TimeoutError("all-or-nothing 子任务超时")
    except TimeoutError as exc:
        verdict = "skip:" + str(exc)
    assert verdict.startswith("skip:")
    print("partial:", r1)
    print("done:", r2)
    print("硬失败处置:", verdict)


if __name__ == "__main__":
    main()
