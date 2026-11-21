"""Q2831 工具参数的最小权限构造:身份字段由服务端注入,LLM 只填业务字段。

LLM 不可信:它可能编造 operator、越权填 tenant_id。参数构造器按 schema
把字段分成 llm_fillable 与 server_injected 两类,身份字段永远以服务端
安全上下文为准,LLM 多填的身份字段直接判越权,未声明字段也要拦。
"""

TOOL_SCHEMA = {
    "tool": "pay.refund",
    "llm_fillable": ["order_id", "amount"],
    "server_injected": ["tenant_id", "operator"],
}


def build_args(llm_args, sec_ctx):
    """合并 LLM 参数与服务端安全上下文,返回最终参数与错误列表。"""
    errors = []
    args = {}
    for k in TOOL_SCHEMA["server_injected"]:
        if k not in sec_ctx:
            errors.append("安全上下文缺失:" + k)
        else:
            args[k] = sec_ctx[k]
    for k in TOOL_SCHEMA["llm_fillable"]:
        if k in llm_args:
            args[k] = llm_args[k]
        else:
            errors.append("LLM 缺填:" + k)
    rogue = sorted(set(llm_args) & set(TOOL_SCHEMA["server_injected"]))
    if rogue:
        errors.append("LLM 越权填写身份字段:" + ",".join(rogue))
    extra = sorted(set(llm_args) - set(TOOL_SCHEMA["llm_fillable"])
                   - set(TOOL_SCHEMA["server_injected"]))
    if extra:
        errors.append("LLM 填了未声明字段:" + ",".join(extra))
    return args, errors


def main():
    sec = {"tenant_id": "t_acme", "operator": "u_42"}
    # 正常:LLM 只填业务字段,身份由服务端注入
    args, errs = build_args({"order_id": "o_1", "amount": 99}, sec)
    assert errs == [], errs
    assert args == {"tenant_id": "t_acme", "operator": "u_42",
                    "order_id": "o_1", "amount": 99}, args
    # 越权:LLM 试图冒充操作者并夹带未声明字段
    args2, errs2 = build_args(
        {"order_id": "o_1", "operator": "root", "memo": "x"}, sec)
    assert args2["operator"] == "u_42", args2   # 身份字段以服务端为准
    assert any("越权" in e for e in errs2), errs2
    assert any("未声明" in e for e in errs2), errs2
    print("正常构造:", args)
    print("越权拦截:", errs2)


if __name__ == "__main__":
    main()
