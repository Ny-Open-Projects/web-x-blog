"""预演与实跑对账:对比计划与实际执行记录,分类出多跑 少跑 参数漂移。"""
import json


def canon(args):
    """参数签名:排序后序列化,比较时与键序无关。"""
    return json.dumps(args, ensure_ascii=False, sort_keys=True)


def reconcile(plan_steps, actual_steps):
    p_by_tool, a_by_tool = {}, {}
    for s in plan_steps:
        p_by_tool.setdefault(s["tool"], []).append(canon(s["args"]))
    for a in actual_steps:
        a_by_tool.setdefault(a["tool"], []).append(canon(a["args"]))

    extra, missing = [], []
    for tool in sorted(set(p_by_tool) | set(a_by_tool)):
        p = list(p_by_tool.get(tool, []))
        a = list(a_by_tool.get(tool, []))
        for sig in a[:]:
            if sig in p:
                p.remove(sig)
                a.remove(sig)
        extra.extend({"tool": tool, "args": json.loads(s)} for s in a)
        missing.extend({"tool": tool, "args": json.loads(s)} for s in p)

    # 同一工具既多跑又少跑 -> 判定为参数漂移而不是两类问题
    drift = []
    extra_tools = {e["tool"] for e in extra}
    missing_tools = {m["tool"] for m in missing}
    for t in sorted(extra_tools & missing_tools):
        drift.append(t)
    extra = [e for e in extra if e["tool"] not in drift]
    missing = [m for m in missing if m["tool"] not in drift]
    return {"match": not (extra or missing or drift),
            "extra": extra, "missing": missing, "drift": drift}


if __name__ == "__main__":
    plan = [{"tool": "search", "args": {"q": "退货"}},
            {"tool": "send_mail", "args": {"to": "a@x.com"}}]

    same = reconcile(plan, [{"tool": "search", "args": {"q": "退货"}},
                            {"tool": "send_mail", "args": {"to": "a@x.com"}}])
    assert same["match"] and same == {"match": True, "extra": [], "missing": [], "drift": []}

    # 参数漂移:mail 发给了别人;计划外多跑了一次 delete
    dirty = reconcile(plan, [{"tool": "search", "args": {"q": "退货"}},
                             {"tool": "send_mail", "args": {"to": "evil@x.com"}},
                             {"tool": "delete_doc", "args": {"id": "d1"}}])
    assert not dirty["match"]
    assert dirty["drift"] == ["send_mail"], "同工具目标变了应判漂移"
    assert dirty["extra"] == [{"tool": "delete_doc", "args": {"id": "d1"}}]

    # 计划了但没执行
    lazy = reconcile(plan, [{"tool": "search", "args": {"q": "退货"}}])
    assert lazy["missing"] == [{"tool": "send_mail", "args": {"to": "a@x.com"}}]
    assert not lazy["drift"]
    print("对账通过:完全一致放行,参数漂移与计划外执行被分类上报")
