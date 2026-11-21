"""流式事件协议:seq 单调 + 生命周期/过程/控制事件 + 断线续传支持。"""
import json


class StreamProtocol:
    def __init__(self):
        self.seq = 0

    def emit(self, event, payload):
        self.seq += 1
        return {"seq": self.seq, "event": event, "payload": payload}

    def render_sse(self, ev):
        return f"event: {ev['event']}\nid: {ev['seq']}\ndata: {json.dumps(ev['payload'], ensure_ascii=False)}\n\n"


class AgentSession:
    def __init__(self, proto):
        self.proto = proto
        self.timeline = []

    def record(self, ev):
        self.timeline.append(ev)

    def run_demo(self, question):
        self.record(self.proto.emit("session_start", {"question": question}))
        self.record(self.proto.emit("status", {"stage": "retrieving"}))
        self.record(self.proto.emit("tool_call", {"tool": "search", "args": {"q": question}}))
        self.record(self.proto.emit("tool_result", {"tool": "search", "summary": "3 条结果"}))
        for piece in ["北京", "明天", "晴,", "15 度。"]:
            self.record(self.proto.emit("delta", {"text": piece}))
        self.record(self.proto.emit("done", {"reason": "completed", "usage": {"tokens": 42}}))

    def resume_from(self, last_seq):
        """断线续传:返回 seq 大于 last_seq 的事件。"""
        return [e for e in self.timeline if e["seq"] > last_seq]


if __name__ == "__main__":
    proto = StreamProtocol()
    session = AgentSession(proto)
    session.run_demo("明天北京天气")
    for ev in session.timeline[:3]:
        print(proto.render_sse(ev).strip())
        print("---")
    kinds = [e["event"] for e in session.timeline]
    assert kinds[0] == "session_start" and kinds[-1] == "done"
    resumed = session.resume_from(last_seq=2)
    print(f"客户端从 seq=2 断线,续传 {len(resumed)} 个事件:", [e["event"] for e in resumed])
    assert resumed[0]["seq"] == 3 and len(resumed) == len(session.timeline) - 2
    seqs = [e["seq"] for e in session.timeline]
    assert seqs == sorted(seqs) and len(set(seqs)) == len(seqs), "seq 必须单调不重复"
