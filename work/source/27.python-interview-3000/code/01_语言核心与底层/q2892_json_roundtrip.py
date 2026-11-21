"""序列化往返的一致性测试:json 往返会丢什么、改什么。"""
import json
from datetime import datetime


def roundtrip(obj):
    return json.loads(json.dumps(obj))


def check(label, original, expect_equal=True):
    try:
        back = roundtrip(original)
    except (TypeError, ValueError) as e:
        print(f"{label:<18} 序列化直接失败:{type(e).__name__}")
        return
    same = back == original
    note = "往返相等" if same else f"往返变形 {original!r} -> {back!r}"
    flag = "符合预期" if same == expect_equal else "预期外"
    print(f"{label:<18} {note} [{flag}]")


if __name__ == "__main__":
    check("dict 与 list", {"a": [1, 2, {"b": None}]})
    check("tuple 变 list", (1, 2), expect_equal=False)
    check("int 键变字符串", {1: "x"}, expect_equal=False)
    check("键碰撞静默丢数据", {1: "int", "1": "str"}, expect_equal=False)
    check("float 精度", 0.1 + 0.2)
    check("NaN 的往返", float("nan"), expect_equal=False)
    check("set 不受支持", {1, 2})
    check("datetime 不受支持", datetime(2026, 1, 1))

    # 一致性测试的工程写法:规范化负载先断言无变形,已知变形白名单化
    payload = {"id": 7, "tags": ["a", "b"], "score": 0.25}
    assert roundtrip(payload) == payload
    print("规范化负载往返相等:断言通过")
