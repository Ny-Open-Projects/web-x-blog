---
title: [Q2844] 子 Agent 产出的验收门:契约校验与限次重派
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2844 · 子 Agent 产出的验收门:契约校验与限次重派

> 难度:★★★★ | 标签:Agent, 多Agent, 契约

**问**:子 Agent 交回来的结果直接信吗?不合格怎么反馈、重派几次该放弃?

**答**:子 Agent 的产出必须过验收门:契约校验逐项检查必填字段、引用真实性,引用了不存在文档的输出比没有输出更糟,因为它披着可信的外壳。不合格要带着具体错因重派——「引用 d9 不存在」比「格式不对」有用得多,子 Agent 修起来才有的放矢;重派必须限次,达到上限整单失败转人工,否则两个 Agent 会互相空转把预算烧光。验收门和工具签名校验的区别在于对象:前者验子 Agent 的自由产出,后者验工具的结构化返回,两者共用同一套契约表达。每次重派的错因要留轨迹,既是调试数据,也是评估子 Agent 质量的素材。

```python
# file: code/06_Agent与LLM及系统设计/q2844_acceptance_gate.py
"""Q2844 子 Agent 产出的验收门:契约校验与限次重派。

子 Agent 的产出不能直接信:缺引用 编造 citation id 是常事。验收门
按契约逐项检查,不合格就带着具体反馈重派,限次内修不好整单失败,
防止两个 Agent 无限互相空转。
"""

SOURCE_POOL = {"d1", "d2"}


def contract_check(out):
    errs = []
    if not out.get("summary"):
        errs.append("缺 summary")
    cites = out.get("citations", [])
    if not cites:
        errs.append("缺引用")
    for c in cites:
        if c not in SOURCE_POOL:
            errs.append("引用不存在:" + c)
    return errs


def gated_delegate(stub, max_attempts=3):
    """带验收门的重派循环,返回产出与尝试次数。"""
    feedback = []
    for i in range(1, max_attempts + 1):
        out = stub(feedback)
        errs = contract_check(out)
        if not errs:
            return out, i
        feedback = errs  # 带着具体错因重派
    raise RuntimeError("子 Agent " + str(max_attempts) + " 次产出仍不合格")


def make_stub():
    """stub:模拟子 Agent,前两版有缺陷,第三版合格。"""
    state = {"n": 0}

    def stub(_feedback):
        state["n"] += 1
        if state["n"] == 1:
            return {"summary": "结论A"}                      # 缺引用
        if state["n"] == 2:
            return {"summary": "结论B", "citations": ["d9"]}  # 编造引用
        return {"summary": "结论C", "citations": ["d1", "d2"]}
    return stub


def main():
    out, n = gated_delegate(make_stub())
    assert n == 3, n
    assert out["citations"] == ["d1", "d2"], out
    # 一直不合格:限次后整单失败,而不是无限重派
    def always_bad(_fb):
        return {"summary": "x"}
    try:
        gated_delegate(always_bad, max_attempts=2)
        raise AssertionError("应当失败")
    except RuntimeError as exc:
        msg = str(exc)
    assert "2 次产出仍不合格" in msg, msg
    print("第 %d 版通过验收:%s" % (n, out["summary"]))
    print("超限处置:", msg)


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:重派时要把失败历史也发给子 Agent 吗? 答:发错因摘要就够,发全量失败轨迹会污染上下文还可能被模仿。
- 追问二:验收规则和业务规则冲突谁说了算? 答:验收门只管契约层,业务判断留给调用方,门里塞业务规则会让它变成第二个业务系统。
