import json


def show(label: str, fn) -> None:
    try:
        print(f"  [{label}] {fn()}")
    except Exception as e:
        print(f"  [{label}] 异常: {e!r}")


if __name__ == "__main__":
    print("1) 大整数精度 (JS 消费方视角):")
    big = 2 ** 53 + 1
    show("python roundtrip", lambda: json.loads(json.dumps(big)) == big)
    show("JS 相当于 Number",
         lambda: float(big) == float(2 ** 53), )  # 9007199254740992 分不清
    print("     → 订单号/雪花ID 跨语言请传字符串")

    print("2) float 精度:")
    show("0.1+0.2", lambda: json.loads(json.dumps(0.1 + 0.2)))
    show("金额建议分", lambda: json.dumps({"cents": 1050}))

    print("3) dict 非字符串 key:")
    show("int key roundtrip",
         lambda: json.loads(json.dumps({1: "a", 2: "b"})))
    show("tuple key", lambda: json.dumps({(1, 2): "x"}))

    print("4) NaN/Infinity 非 JSON 标准:")
    show("默认 dumps NaN", lambda: json.dumps(float("nan")))
    show("严格模式", lambda: json.dumps(float("nan"), allow_nan=False))

    print("5) 中文与 ensure_ascii:")
    zh = json.dumps({"city": "上海"})
    print(f"     默认: {zh} ({len(zh)} 字节)")
    print(f"     关闭转义: {json.dumps({'city': '上海'}, ensure_ascii=False)}")

    print("6) 重复键: 解析取最后一个 (校验绕过风险)")
    show("dup key", lambda: json.loads('{"role": "user", "role": "admin"}'))

    print("\n工程建议: 入口 schema 校验 + 显式序列化参数 + 金额/ID 字符串化")
