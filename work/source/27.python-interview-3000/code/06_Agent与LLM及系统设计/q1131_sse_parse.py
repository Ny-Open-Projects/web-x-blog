"""SSE 协议解析:把原始文本流拆成事件帧,处理心跳、多行 data、缺省 event。"""

RAW = (
    'event: delta\ndata: {"text": "你"}\n\n'
    ': keep-alive\n\n'
    'event: delta\ndata: {"text": "好"}\n\n'
    'event: done\ndata: [DONE]\n\n'
)


def parse_sse(stream: str):
    """按空行分帧;注释行跳过;data 多行拼接;event 缺省为 message。"""
    events, event, data = [], None, []
    for line in stream.split("\n"):
        if line == "":
            if data:
                events.append({"event": event or "message", "data": "\n".join(data)})
            event, data = None, []
        elif line.startswith(":"):
            continue
        elif line.startswith("event:"):
            event = line[6:].strip()
        elif line.startswith("data:"):
            data.append(line[5:].strip())
    if data:  # 流末尾没有空行收尾,也要补一帧
        events.append({"event": event or "message", "data": "\n".join(data)})
    return events


if __name__ == "__main__":
    evs = parse_sse(RAW)
    for e in evs:
        print(e)
    assert evs[0]["data"] == '{"text": "你"}'
    assert evs[-1] == {"event": "done", "data": "[DONE]"}
    assert len(evs) == 3, "心跳注释不应产生事件"
    print("解析完成:心跳已忽略,共 3 个有效事件")
