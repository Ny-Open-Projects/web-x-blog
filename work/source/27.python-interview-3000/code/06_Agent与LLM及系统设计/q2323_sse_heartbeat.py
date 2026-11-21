"""流式心跳保活:上游无 token 时发 SSE 注释帧,网关空闲计时被复位,注释帧不进正文。"""
def sse_frame(event, data=None):
    if event == "ping":
        return ": ping\n\n"
    return "event: %s\ndata: %s\n\n" % (event, data)


def stream_with_heartbeat(token_events, heartbeat_every=2.0, clock_step=1.0):
    out, idle = [], 0.0
    for ev in token_events:
        idle += clock_step
        if idle >= heartbeat_every:
            out.append(sse_frame("ping"))
            idle = 0.0
        if ev is None:
            continue
        out.append(sse_frame("delta", ev))
        idle = 0.0
    if idle >= heartbeat_every:
        out.append(sse_frame("ping"))
    return out


def parse_client(frames):
    body = []
    for f in frames:
        if f.startswith(":"):
            continue
        for line in f.splitlines():
            if line.startswith("data: "):
                body.append(line[6:])
    return "".join(body)


if __name__ == "__main__":
    frames = stream_with_heartbeat(["你", None, None, "好"])
    assert parse_client(frames) == "你好", "注释帧不进正文 token 不重不漏"
    assert any(f.startswith(":") for f in frames), "空闲段有心跳注释帧"
    assert len(frames) == 3, "两个 token 帧加一个心跳"
    long_idle = stream_with_heartbeat([None, None, None])
    assert parse_client(long_idle) == "" and len(long_idle) == 1, "全程空闲只靠心跳续命"
    instant = stream_with_heartbeat(["你", "好"])
    assert ": ping" not in "".join(instant), "无空闲不发心跳"
    print("心跳保活通过:注释帧复位空闲计时 网关不断流 正文干净")
