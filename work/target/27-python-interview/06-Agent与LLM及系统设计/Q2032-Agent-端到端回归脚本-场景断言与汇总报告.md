---
title: [Q2032] Agent 端到端回归脚本:场景断言与汇总报告
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2032 · Agent 端到端回归脚本:场景断言与汇总报告

> 难度:★★★☆ | 标签:Agent, 测试, 回归

**问**:改了一版系统提示,怎么确认所有 Agent 场景的行为没有回归?

**答**:把典型会话固化成场景集,每个场景三件套:脚本化 FakeLLM 的应答序列、工具桩、期望断言——工具序列对不对、终答对不对。回归脚本逐场景跑,把异常也捕获成失败项而不是中断整个跑批,最后输出通过数、失败数与失败原因,一条命令出报告。脚本耗尽是关键防护:Agent 循环超出预期步数会撞上空脚本报错,死循环被自然拦截。预期失败样例要留在场景集里,验证回归器自己没有失明。

```python
# file: code/06_Agent与LLM及系统设计/q2032_e2e_regression.py
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
```

**追问**:
- 场景集怎么维护? 答:线上 badcase 沉淀为新场景,修复后固化为回归用例,场景集只增不减
- 和单元测试什么区别? 答:单测验证部件,端到端回归验证装配后的行为,提示词这类改一处动全身的变更只有后者能兜住
