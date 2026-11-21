"""最小 Agent 循环:消息驱动、工具注册、最大轮数保护,全部用 stub。"""
import json


class FakeLoopLLM:
    def __init__(self):
        self.turn = 0

    def chat(self, messages, tools):
        self.turn += 1
        if self.turn == 1:
            return {"type": "tool_call", "name": "add", "args": {"a": 2, "b": 3}}
        tool_result = next(m["content"] for m in messages if m["role"] == "tool")
        return {"type": "final", "content": f"2+3 的结果是 {tool_result}"}


class Agent:
    def __init__(self, llm, tools: dict, max_turns: int = 5):
        self.llm, self.tools, self.max_turns = llm, tools, max_turns

    def run(self, task: str) -> str:
        messages = [{"role": "system", "content": "你是会用工具的助手"},
                    {"role": "user", "content": task}]
        for turn in range(self.max_turns):
            resp = self.llm.chat(messages, tools=list(self.tools))
            if resp["type"] == "final":
                return resp["content"]
            try:
                result = self.tools[resp["name"]](**resp["args"])
            except Exception as exc:  # 工具异常回填给模型自纠
                result = f"工具执行失败: {exc}"
            messages.append({"role": "tool", "content": str(result)})
        return "达到最大轮数,强制终止"


if __name__ == "__main__":
    tools = {"add": lambda a, b: json.dumps(a + b)}
    agent = Agent(FakeLoopLLM(), tools, max_turns=5)
    print(agent.run("帮我算 2 加 3"))
