"""工具 mock 层:脚本化应答按序弹出,记录调用参数,支持计数断言与异常脚本。"""


class MockToolLayer:
    def __init__(self):
        self.scripts = {}                        # tool -> [response 或 Exception 实例]
        self.calls = []                          # 记录 (tool, args)

    def given(self, tool, responses):
        self.scripts[tool] = list(responses)

    def call(self, tool, args):
        self.calls.append((tool, dict(args)))
        if tool not in self.scripts or not self.scripts[tool]:
            raise AssertionError("mock 未配置脚本: " + tool)
        item = self.scripts[tool].pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    def assert_called_with(self, tool, args):
        assert (tool, args) in self.calls, "工具 %s 未以 %s 被调用" % (tool, args)

    def call_count(self, tool):
        return sum(1 for t, _ in self.calls if t == tool)


class AgentStub:
    """被测 Agent:只依赖工具层接口,mock 与真实工具可互换。"""

    def __init__(self, tools):
        self.tools = tools

    def answer(self, q):
        try:
            hits = self.tools.call("search", {"q": q})
        except TimeoutError:
            return "搜索超时,请稍后再试"
        return "答案:" + hits["top"]


if __name__ == "__main__":
    mock = MockToolLayer()
    mock.given("search", [{"top": "北京 明 8 度"}, TimeoutError("slow"), {"top": "上海 雨"}])
    agent = AgentStub(mock)

    assert agent.answer("北京天气") == "答案:北京 明 8 度"
    assert agent.answer("北京天气") == "搜索超时,请稍后再试", "异常脚本驱动降级分支"
    mock.assert_called_with("search", {"q": "北京天气"})
    assert mock.call_count("search") == 2
    assert mock.scripts["search"] == [{"top": "上海 雨"}], "未消费的脚本保留"
    print("工具 mock 层通过:应答按序弹出 异常脚本可注入 计数与参数可断言")
