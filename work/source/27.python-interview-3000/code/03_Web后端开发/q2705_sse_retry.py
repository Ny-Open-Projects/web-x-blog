"""SSE 的事件重试字段: retry 与 Last-Event-ID 的重连协议(纯标准库)。"""
import time


def sse_event(data, event_id=None, event_type=None, retry_ms=None):
    """把一帧业务数据编成 SSE 报文, 字段顺序固定: retry 在前最稳。

    retry: 告诉浏览器断线后的重连等待, 服务端可按负载动态加大;
    id:   客户端重连时通过 Last-Event-ID 头带回来, 服务端从此序号续播。
    """
    lines = []
    if retry_ms is not None:
        lines.append("retry: %d" % retry_ms)
    if event_id is not None:
        lines.append("id: %s" % event_id)
    if event_type is not None:
        lines.append("event: %s" % event_type)
    for row in str(data).splitlines() or [""]:
        lines.append("data: %s" % row)
    return "\n".join(lines) + "\n\n"


class SseServer:
    """带重放窗口的推送源: 记住每个事件的 id, 断线重连按游标续播。"""

    def __init__(self, backlog=100):
        self.backlog = backlog
        self.log = []
        self.seq = 0

    def publish(self, data, retry_ms=None):
        self.seq += 1
        frame = sse_event(data, event_id=str(self.seq), retry_ms=retry_ms)
        self.log.append((self.seq, frame))
        if len(self.log) > self.backlog:
            self.log.pop(0)
        return frame

    def replay_from(self, last_event_id):
        """Last-Event-ID 比最老积压还旧就说明缺口补不齐, 只能回全量或让客户端重拉。"""
        if last_event_id is None:
            return [f for _, f in self.log]
        cursor = int(last_event_id)
        if self.log and cursor < self.log[0][0]:
            return None  # 缺口超出积压
        return [f for sid, f in self.log if sid > cursor]


srv = SseServer()
frames = [srv.publish("msg%d" % (i + 1), retry_ms=3000 if i == 0 else None) for i in range(5)]
assert frames[0].startswith("retry: 3000\nid: 1\ndata: msg1\n\n"), frames[0]
assert frames[-1].startswith("id: 5\ndata: msg5\n\n"), frames[-1]

client_state = "3"  # 浏览器崩在收到 id=3 之后
missed = srv.replay_from(client_state)
assert len(missed) == 2 and missed[0].startswith("id: 4"), missed
gap = srv.replay_from("0")
assert gap is None, "游标早于积压窗口应判缺口"
print("重连续播 2 帧:", [f.splitlines()[0] for f in missed])
print("多行 data 会被拆成多行 data 字段:",
      sse_event("a\nb").count("data:") == 2)
