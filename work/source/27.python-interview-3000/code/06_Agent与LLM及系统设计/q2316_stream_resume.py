"""流式断线续传:每个事件带自增 id,服务端保留窗口,客户端带 Last-Event-ID 续传不重不漏。"""


class StreamServer:
    def __init__(self, window=100):
        self.events = []
        self.window = window

    def emit(self, text):
        eid = len(self.events) + 1
        self.events.append({"id": eid, "data": text})
        return eid

    def resume_from(self, last_event_id):
        if last_event_id < len(self.events) - self.window:
            raise ValueError("事件已超出续传窗口 请全量重建")
        return self.events[last_event_id:]


class StreamClient:
    def __init__(self):
        self.last_id = 0
        self.chunks = []

    def consume(self, events):
        for ev in events:
            if ev["id"] <= self.last_id:
                continue
            self.chunks.append(ev["data"])
            self.last_id = ev["id"]

    def text(self):
        return "".join(self.chunks)


if __name__ == "__main__":
    srv = StreamServer()
    for ch in ["你", "好", "，", "世", "界"]:
        srv.emit(ch)
    cli = StreamClient()
    cli.consume(srv.events[:3])
    assert cli.text() == "你好，" and cli.last_id == 3
    srv.emit("!")
    srv.emit("再见")
    cli.consume(srv.resume_from(cli.last_id))
    assert cli.text() == "你好，世界!再见", "续传不重不漏"
    cli.consume(srv.events)
    assert cli.text() == "你好，世界!再见", "重复投递幂等"
    small = StreamServer(window=3)
    for ch in ["a", "b", "c", "d", "e", "f", "g"]:
        small.emit(ch)
    try:
        small.resume_from(1)
        raise SystemExit("应报超出窗口")
    except ValueError:
        pass
    print("断线续传通过:事件序号 游标续传 幂等去重 窗口保护")
