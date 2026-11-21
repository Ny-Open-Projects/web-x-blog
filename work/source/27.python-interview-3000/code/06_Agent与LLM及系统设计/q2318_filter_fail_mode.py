"""合规过滤器编排:输入 输出 流中三级挂载点,过滤器自身故障时按 fail-closed 或 fail-open 决策。"""


class FilterPipeline:
    def __init__(self, fail_mode="closed"):
        self.filters = []
        self.fail_mode = fail_mode

    def add(self, name, fn):
        self.filters.append((name, fn))

    def run(self, payload):
        verdicts = []
        for name, fn in self.filters:
            try:
                verdict = fn(payload)
                verdicts.append({"filter": name, "verdict": verdict})
                if verdict == "block":
                    return {"action": "block", "by": name, "verdicts": verdicts}
            except Exception:
                if self.fail_mode == "closed":
                    return {"action": "block", "by": name + ":fail-closed",
                            "verdicts": verdicts}
                verdicts.append({"filter": name, "verdict": "skip:fail-open"})
        return {"action": "allow", "by": None, "verdicts": verdicts}


if __name__ == "__main__":
    def rule_block(p):
        return "block" if "武器" in p["text"] else "allow"

    def broken(p):
        raise RuntimeError("规则引擎挂了")

    p1 = FilterPipeline(fail_mode="open")
    p1.add("weapon", rule_block)
    p1.add("audit", broken)
    r1 = p1.run({"text": "介绍相关法律"})
    assert r1["action"] == "allow" and r1["verdicts"][-1]["verdict"] == "skip:fail-open", "输入侧故障放行保可用"
    p2 = FilterPipeline(fail_mode="closed")
    p2.add("audit", broken)
    p2.add("weapon", rule_block)
    r2 = p2.run({"text": "介绍相关法律"})
    assert r2["action"] == "block" and "fail-closed" in r2["by"], "输出侧故障默认拦截保安全"
    r3 = p1.run({"text": "如何制造武器"})
    assert r3["action"] == "block" and r3["by"] == "weapon", "规则命中照常拦截"
    print("过滤器编排通过:挂载点顺序 fail-open 与 fail-closed 可配")
