---
title: [Q2316] 流式断线续传:事件序号与 Last-Event-ID 重放
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2316 · 流式断线续传:事件序号与 Last-Event-ID 重放

> 难度:★★★★ | 标签:LLM 运维, 流式, 可靠性

**问**:用户看流式回复看到一半网断了,重连后是从头重生成还是接着看?服务端要做什么?

**答**:流式协议天然支持续传:SSE 每个事件带自增 id,客户端记住最后收到的 id,重连时带 Last-Event-ID 头,服务端从该序号之后重放,已生成的内容不用重来。服务端要维护已发出事件的保留窗口——内存或临时存储,窗口外的旧事件拒绝续传并要求客户端全量重建,这是资源保护。客户端消费必须幂等:重叠投递按 id 去重,序号小于等于已消费的丢弃,重放与重发双保险下正文依然不重不漏。续传窗口是成本与体验的权衡:窗口大续传成功率高但内存占用高,业务上多数中断在秒级重连,小窗口就够。

```python
# file: code/06_Agent与LLM及系统设计/q2316_stream_resume.py
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
```

**追问**:
- 断线期间生成还在继续吗? 答:理想是服务端继续生成并进窗口,重连时一并重放;简单实现则断线即取消,重连从头生成
- 与工具调用的流式怎么配合? 答:工具结果事件同样有序号,续传重放时工具调用按幂等键去重,不重复执行副作用
