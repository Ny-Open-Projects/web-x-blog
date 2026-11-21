"""流式增量聚合器:delta 事件拼成完整消息,支持序号去重、节流渲染与终止校验。"""


class StreamAggregator:
    def __init__(self, render_every=2):
        self.text = ""
        self.done = False
        self.last_seq = 0          # 最近已消费的序号,用于去重
        self.chunks = 0
        self.render_every = render_every
        self.rendered = []         # 模拟 UI 渲染的快照

    def feed(self, seq: int, delta: str, is_done=False):
        if seq <= self.last_seq:   # 乱序或重复,直接丢弃
            return None
        self.last_seq = seq
        if is_done:
            self.done = True
            return self.finish()
        self.text += delta
        self.chunks += 1
        if self.chunks % self.render_every == 0:  # 节流:攒够 N 片才渲染
            self.rendered.append(self.text)
        return self.text

    def finish(self):
        assert self.done, "未收到终止事件不能收尾"
        self.rendered.append(self.text)
        return self.text


if __name__ == "__main__":
    agg = StreamAggregator()
    chunks = ["今天", "天气", "不错", ",", "适合", "散步。"]
    for i, c in enumerate(chunks, 1):
        agg.feed(i, c)
    final = agg.feed(len(chunks) + 1, "", is_done=True)
    print("最终消息:", final)
    print("渲染次数:", len(agg.rendered), "片数:", agg.chunks)
    agg.feed(2, "重复片")  # 重复 seq 应被忽略
    assert agg.text == final, "重复事件不应污染结果"
    print("节流渲染生效,重复事件被去重")
