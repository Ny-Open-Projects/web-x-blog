---
title: [Q2705] SSE 的 retry 字段与 Last-Event-ID 续播
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2705 · SSE 的 retry 字段与 Last-Event-ID 续播

> 难度:★★★★ | 标签:SSE, 推送, 重连

**问**:SSE 断线重连的节奏谁说了算?客户端刷新后怎么从断点继续收?

**答**:两个机制配合。服务端在事件流里下发 `retry: 3000`,告诉浏览器断线后等多久再连,负载高时动态调大,这是服务端控制重连风暴的阀门;每个事件带 `id:`,浏览器记住最后收到的 id,重连时通过 Last-Event-ID 请求头带回来,服务端按游标从积压日志续播。工程细节三条:id 用单调递增序号即可;重放窗口(积压条数)要明确定界,游标比最老积压还旧说明缺口补不齐,只能回全量或让客户端重拉;多行 data 拆成多行 data 字段,帧内字段顺序按 retry、id、event、data 排最稳。重连协议是 SSE 可靠性的全部,没有 id 就只有全量重发。

```python
# file: code/03_Web后端开发/q2705_sse_retry.py
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
```

**追问**:
- Last-Event-ID 能被客户端伪造吗?——能,它就是普通请求头,服务端要按会话校验游标归属与可见范围,不能盲信。
- retry 能对单个事件单独设置吗?——retry 是流级状态,设置后对后续所有重连生效,想调整就在需要的事件帧里重发一次 retry 行。
