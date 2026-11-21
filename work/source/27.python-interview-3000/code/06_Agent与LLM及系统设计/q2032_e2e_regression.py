"""Agent 端到端回归脚本:脚本化 FakeLLM,断言工具序列与终答,输出汇总报告。"""


class FakeLLM:
    def __init__(self, script):
        self.script = list(script)

    def chat(self, messages):
        self.calls = getattr(self, "calls", 0) + 1
        if not self.script:
            raise RuntimeError("脚本耗尽:Agent 循环超出预期步数")
        return self.script.pop(0)


def run_agent(llm, tools, task):
    """两步小 Agent:先决策是否调工具,带观察再给终答。"""
    reply = llm.chat([{"role": "user", "content": task}])
    if reply["content"].startswith("TOOL:"):
        _, name, args = reply["content"].split(":", 2)
        if name not in tools:
            raise RuntimeError("调用了未注册工具 " + name)
        obs = tools[name](args)
        final = llm.chat([{"role": "user", "content": "观察:" + obs}])
        return {"tool": name, "args": args, "answer": final["content"]}
    return {"tool": None, "args": None, "answer": reply["content"]}


SCENARIOS = [
    {"name": "查订单走工具",
     "llm": [{"role": "assistant", "content": "TOOL:query_order:A100"},
             {"role": "assistant", "content": "订单已发货"}],
     "tools": {"query_order": lambda a: "状态=已发货"},
     "expect_tool": "query_order", "expect_answer": "订单已发货"},
    {"name": "闲聊直答",
     "llm": [{"role": "assistant", "content": "你好,需要什么帮助"}],
     "tools": {},
     "expect_tool": None, "expect_answer": "你好,需要什么帮助"},
    {"name": "预期失败样例",           # 故意让答案错,验证回归脚本能抓住
     "llm": [{"role": "assistant", "content": "随便答的"}],
     "tools": {},
     "expect_tool": None, "expect_answer": "标准答案"},
]


def run_scenarios(scenarios):
    report = []
    for sc in scenarios:
        llm = FakeLLM(sc["llm"])
        try:
            out = run_agent(llm, sc["tools"], "任务")
            problems = []
            if out["tool"] != sc["expect_tool"]:
                problems.append("工具调用不符")
            if out["answer"] != sc["expect_answer"]:
                problems.append("终答不符")
            report.append({"name": sc["name"], "pass": not problems,
                           "detail": ",".join(problems) or "ok"})
        except Exception as e:
            report.append({"name": sc["name"], "pass": False,
                           "detail": "异常:" + str(e)})
    return report


if __name__ == "__main__":
    report = run_scenarios(SCENARIOS)
    passed = [r for r in report if r["pass"]]
    failed = [r for r in report if not r["pass"]]
    assert len(report) == 3 and len(passed) == 2 and len(failed) == 1
    assert failed[0]["name"] == "预期失败样例" and "终答不符" in failed[0]["detail"]

    # 脚本耗尽防护:Agent 多走一步会被抓住而不是死循环
    runaway = [{"name": "失控", "llm": [{"role": "assistant", "content": "TOOL:query_order:A"}],
                "tools": {"query_order": lambda a: "x"},
                "expect_tool": "query_order", "expect_answer": "y"}]
    r = run_scenarios(runaway)[0]
    assert not r["pass"] and "异常" in r["detail"]
    print("端到端回归通过:3 场景 2 过 1 抓,失控循环被脚本耗尽防护拦截")
