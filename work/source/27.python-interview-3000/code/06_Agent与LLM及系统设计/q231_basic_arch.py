"""用一次最小化调用演示 LLM 应用四层结构:应用层组装消息、模型层返回、编排层处理。"""


class FakeLLM:
    """模拟模型层,替代真实 API。"""

    def chat(self, messages: list[dict]) -> str:
        last = messages[-1]["content"]
        return f"[模型回复] 已收到消息:{last}"


class Application:
    """应用层 + 编排层:会话维护、Prompt 组装、调用模型。"""

    def __init__(self, llm):
        self.llm = llm
        self.history: list[dict] = [{"role": "system", "content": "你是一个助手"}]

    def handle(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})
        answer = self.llm.chat(self.history)
        self.history.append({"role": "assistant", "content": answer})
        return answer


if __name__ == "__main__":
    app = Application(FakeLLM())
    print(app.handle("你好,介绍一下你自己"))
    print(f"会话消息数:{len(app.history)}")
