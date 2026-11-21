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
