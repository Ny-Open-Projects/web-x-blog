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
