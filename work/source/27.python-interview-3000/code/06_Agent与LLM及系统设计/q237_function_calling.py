"""完整演示 Function calling 循环:模型只返回调用意图,客户端执行并回填。"""
import json


class FakeLLM:
    """第一轮返回 tool_call,第二轮基于工具结果生成回答。"""

    def __init__(self):
        self.turn = 0

    def chat(self, messages, tools=None):
        self.turn += 1
        if self.turn == 1:
            return {"tool_calls": [{"name": "get_weather",
                                    "arguments": {"city": "北京"}}]}
        tool_msg = next(m for m in messages if m["role"] == "tool")
        return f"根据查询结果回答:{tool_msg['content']}"


def get_weather(city: str) -> str:
    return json.dumps({"city": city, "weather": "晴", "temp_c": 12}, ensure_ascii=False)


TOOLS = {"get_weather": get_weather}


def agent_loop(llm, user_input: str, max_turns: int = 3) -> str:
    messages = [{"role": "user", "content": user_input}]
    for _ in range(max_turns):
        resp = llm.chat(messages, tools=list(TOOLS))
        if isinstance(resp, dict) and "tool_calls" in resp:
            for call in resp["tool_calls"]:
                result = TOOLS[call["name"]](**call["arguments"])
                messages.append({"role": "tool", "content": result})
            continue
        return resp
    return "达到最大轮数,终止"


if __name__ == "__main__":
    print(agent_loop(FakeLLM(), "北京天气如何?"))
