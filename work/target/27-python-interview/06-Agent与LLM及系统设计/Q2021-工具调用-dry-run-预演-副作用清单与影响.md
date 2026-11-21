---
title: [Q2021] 工具调用 dry-run 预演:副作用清单与影响摘要
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2021 · 工具调用 dry-run 预演:副作用清单与影响摘要

> 难度:★★☆☆ | 标签:Agent, dry-run, 工具安全

**问**:Agent 要替用户执行发邮件、删数据这类危险工具,上线前你敢让它直接跑吗?怎么让危险操作先过目再执行?

**答**:不敢直接跑,标准做法是加一层 dry-run 预演。预演只读工具注册表的元数据:每个工具声明自己会触碰的外部状态,比如 write:email、delete:doc;预演按计划逐个查表,产出步骤清单、副作用清单和一句人话摘要,绝不调用工具本体。计划里没有任何副作用就直接放行;有副作用就把摘要交给人工确认或策略引擎裁决,确认后才进入实跑。收益是危险操作从「跑了才知道」变成「跑前可审计」,而且预演是纯函数,单测成本极低。

```python
# file: code/06_Agent与LLM及系统设计/q2021_tool_dry_run.py
"""工具调用 dry-run 预演:不真正执行,产出副作用清单与影响摘要,确认后才实跑。"""


class Tool:
    """工具元数据:side_effects 声明该工具会改动哪些外部状态。"""

    def __init__(self, name, side_effects, func):
        self.name = name
        self.side_effects = list(side_effects)
        self.func = func


REGISTRY = {}


def register(tool):
    REGISTRY[tool.name] = tool


def plan_step(name, args):
    tool = REGISTRY[name]
    return {"tool": name, "args": dict(args), "side_effects": list(tool.side_effects)}


def dry_run(names_and_args):
    """预演:只查注册表与元数据,绝不调用工具本体。"""
    steps = [plan_step(n, a) for n, a in names_and_args]
    risky = [s for s in steps if s["side_effects"]]
    if risky:
        summary = "计划 %d 步,其中 %d 步有副作用:%s" % (
            len(steps), len(risky), ",".join(s["tool"] for s in risky))
    else:
        summary = "计划 %d 步,全部只读,可直接执行" % len(steps)
    return {"steps": steps, "has_side_effects": bool(risky), "summary": summary}


def execute(plan):
    """确认后的实跑:按计划顺序调用,返回结果。"""
    return [REGISTRY[s["tool"]].func(**s["args"]) for s in plan["steps"]]


if __name__ == "__main__":
    executed = []

    def search(q):
        return {"hits": 2}

    def send_mail(to, body):
        executed.append(("mail", to))
        return {"sent": True}

    register(Tool("search", [], search))
    register(Tool("send_mail", ["write:email"], send_mail))

    plan = dry_run([("search", {"q": "退货政策"}),
                    ("send_mail", {"to": "ops@x.com", "body": "周报"})])
    assert executed == [], "dry-run 阶段不允许真的发出邮件"
    assert plan["has_side_effects"] is True
    assert plan["steps"][1]["side_effects"] == ["write:email"]
    assert "send_mail" in plan["summary"], "摘要要点名有副作用的工具"

    results = execute(plan)
    assert results == [{"hits": 2}, {"sent": True}], "确认后实跑结果正确"
    assert executed == [("mail", "ops@x.com")]

    safe = dry_run([("search", {"q": "x"})])
    assert safe["has_side_effects"] is False and "只读" in safe["summary"]
    print("dry-run 预演通过:预演零执行,副作用清单与摘要正确,确认后才实跑")
```

**追问**:
- 模型计划里有个注册表没有的工具怎么办? 答:预演阶段直接报未知工具并中止,实跑前任何计划外工具都是注入嫌疑
- 预演和实跑之间计划被改了怎么办? 答:预演产出物是实跑的唯一输入,实跑只认计划不认模型的新输出,篡改会在对账里暴露
