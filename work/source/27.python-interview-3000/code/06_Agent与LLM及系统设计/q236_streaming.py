"""用生成器模拟 SSE 流式输出:FakeLLM 逐 token yield,客户端边收边拼。"""


class FakeStreamingLLM:
    def stream(self, messages: list[dict]):
        answer = f"好的,关于「{messages[-1]['content']}」我分五步给你讲清楚"
        for ch in answer:
            yield ch


def sse_server(llm, messages):
    """模拟服务端:包装为 SSE 帧,并收集全量内容用于审计。"""
    full = []
    for delta in llm.stream(messages):
        full.append(delta)
        yield f"data: {delta}\n\n"
    yield f"event: done\ndata: {len(full)} tokens\n\n"
    print(f"[审计] 完整回复已落库:{''.join(full)[:12]}...")


def client_render(stream):
    buf = []
    for frame in stream:
        if frame.startswith("data: ") and not frame.startswith("data: \n"):
            token = frame[len("data: "):].strip("\n")
            buf.append(token)
            print(f"\r当前渲染:{''.join(buf)}", end="")
    print()


if __name__ == "__main__":
    llm = FakeStreamingLLM()
    client_render(sse_server(llm, [{"role": "user", "content": "如何学习RAG"}]))
