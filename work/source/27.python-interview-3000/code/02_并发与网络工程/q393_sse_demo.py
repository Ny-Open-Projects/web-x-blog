"""SSE 服务端响应格式与客户端解析(标准库演示协议本身)。"""
from typing import Optional


def sse_format(data: str, event: Optional[str] = None, msg_id: Optional[str] = None) -> str:
    """把一条消息编码成 SSE 帧。注意: data 多行要拆成多个 data: 行。

    注: str | None(PEP 604)写法运行时求值要 3.10+, 参数默认值注解
    在 3.9 直接 TypeError, 兼容写法用 Optional 或 future annotations。
    """
    lines = []
    if msg_id:
        lines.append(f"id: {msg_id}")
    if event:
        lines.append(f"event: {event}")
    for chunk in data.splitlines() or [""]:
        lines.append(f"data: {chunk}")
    return "\n".join(lines) + "\n\n"  # 空行表示事件结束


def parse_sse_stream(chunks):
    """客户端侧: 按 空行 分帧解析。"""
    event = {}
    for raw in chunks:
        for line in raw.splitlines():
            if not line:
                if event:
                    yield event
                event = {}
                continue
            field, _, value = line.partition(": ")
            event[field] = value


if __name__ == "__main__":
    frames = [
        sse_format("进度 30%", event="progress", msg_id="1"),
        sse_format("进度 100%\n完成", event="progress", msg_id="2"),
    ]
    print("SSE 响应体样例:\n" + frames[0], end="")
    for ev in parse_sse_stream(frames):
        print("客户端收到:", ev)
