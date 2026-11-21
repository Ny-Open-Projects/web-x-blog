---
title: [Q1761] 工具 mock 层设计:脚本化应答与调用断言
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1761 · 工具 mock 层设计:脚本化应答与调用断言

> 难度:★☆☆☆ | 标签:Agent, 测试, mock

**问**:测 Agent 逻辑时不想真调工具,怎么搭一个可靠的工具 mock 层?

**答**:mock 层只需要三件事:脚本化应答、调用记录、断言接口。given 按工具名预设一串响应,call 按序弹出,弹完再调就显式报错,防止测试悄悄偏离剧本;所有调用按工具名加参数记录,事后可以断言"搜索工具确实以这个 query 被调了一次";响应串里允许放异常实例,弹出时抛出,专门驱动 Agent 的降级分支。被测 Agent 只依赖工具层的 call 接口,mock 与真实实现可互换,这就是测试替身的全部价值。

```python
# file: code/06_Agent与LLM及系统设计/q1761_tool_mock.py
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
```

**追问**:
- mock 脚本耗尽还该报错吗? 答:必须报错,静默返回会让测试在剧本之外继续跑出不可复现的假通过。
- 和录制回放什么关系? 答:mock 适合单元测试的精确剧本,录制回放适合集成测试还原真实工具行为,两者互补。
