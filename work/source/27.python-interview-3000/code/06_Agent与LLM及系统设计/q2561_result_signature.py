"""Q2561 工具调用结果的签名校验:类型指纹与字段契约。

工具返回值进入 Agent 上下文前先过一道签名校验:逐字段比对类型指纹,
缺失、多出、类型不符都要留痕,坏结果不允许混进推理上下文。
"""
import json

CONTRACT = {"name": "str", "score": "float", "tags": "list[str]"}


def type_tag(v):
    """把一个值映射成类型指纹字符串。"""
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, int):
        return "int"
    if isinstance(v, float):
        return "float"
    if isinstance(v, str):
        return "str"
    if isinstance(v, list):
        inner = type_tag(v[0]) if v else "?"
        return "list[" + inner + "]"
    if isinstance(v, dict):
        return "dict"
    return "unknown"


def check_signature(result, contract):
    """返回错误列表,空列表表示签名通过。"""
    errors = []
    for key in sorted(contract):
        if key not in result:
            errors.append("missing:" + key)
        elif type_tag(result[key]) != contract[key]:
            errors.append("type:" + key + ":" + type_tag(result[key]) + "!=" + contract[key])
    extra = sorted(set(result) - set(contract))
    if extra:
        errors.append("extra:" + ",".join(extra))
    return errors


def fake_tool_call(payload):
    """stub:模拟工具返回,真实场景这里是 HTTP 或 SDK 调用。"""
    return json.loads(payload)


def main():
    good = fake_tool_call('{"name": "订单A", "score": 0.92, "tags": ["vip"]}')
    bad = fake_tool_call('{"name": 7, "tags": "vip", "bonus": 1}')
    errs_good = check_signature(good, CONTRACT)
    errs_bad = check_signature(bad, CONTRACT)
    assert errs_good == [], errs_good
    assert "type:name:int!=str" in errs_bad, errs_bad
    assert "type:tags:str!=list[str]" in errs_bad, errs_bad
    assert "missing:score" in errs_bad, errs_bad
    assert "extra:bonus" in errs_bad, errs_bad
    print("正常结果签名通过:", errs_good)
    print("异常结果拒收原因:", errs_bad)


if __name__ == "__main__":
    main()
