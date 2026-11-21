---
title: [Q2318] 合规过滤器的编排位置与失效模式:fail-open 与 fail-closed
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2318 · 合规过滤器的编排位置与失效模式:fail-open 与 fail-closed

> 难度:★★★☆ | 标签:LLM 运维, 安全, 架构

**问**:Q1168 讲了过滤规则本身,过滤器引擎挂了怎么办?输入侧和输出侧的策略一样吗?

**答**:过滤器是会故障的组件,失效模式必须显式设计。fail-closed:过滤器异常一律拦截,宁可错杀不可放过,输出侧(给用户看之前)必须用这个——规则引擎挂了还放行内容出去,合规风险不可控。fail-open:异常放行并记 skip 告警,输入侧(用户输入进模型之前)可以用——输入侧拦截率本来低,引擎故障时全面拦截等于全站拒绝服务,可用性优先。编排上过滤器按挂载点顺序执行:任一 block 短路返回,拦截者名字进 verdicts 便于归因。选择不是二选一,是按挂载点分别配置,并且这个配置进变更审批,误把输出侧改成 fail-open 是重大事故。

```python
# file: code/06_Agent与LLM及系统设计/q2318_filter_fail_mode.py
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
```

**追问**:
- 流式输出的过滤器挂载在哪? 答:在分块发往客户端之前,与 Q2322 的滑动缓冲配合,拦截要赶在用户看到之前
- 过滤器自身怎么监控? 答:拦截率、引擎错误率、p99 耗时三个指标,错误率突增即告警,这是 fail 模式的触发现场
