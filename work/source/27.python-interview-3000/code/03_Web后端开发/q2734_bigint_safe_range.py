"""大整数的 JS 安全范围: 超过 2^53-1 就按字符串走(纯标准库)。"""
import json

MAX_SAFE = 2 ** 53 - 1  # JS Number.MAX_SAFE_INTEGER


def js_safe(value):
    """出接口的整数出口: |v| 超过安全范围就转字符串, 调用方无需感知。

    注意 json.dumps 的 default 钩子不会对 int 触发(int 本身可序列化),
    所以必须先递归变换再 dumps, 这是最容易踩的实现坑。
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return str(value) if abs(value) > MAX_SAFE else value
    if isinstance(value, dict):
        return {k: js_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [js_safe(x) for x in value]
    return value


def dump(obj):
    return json.dumps(js_safe(obj), ensure_ascii=False)


def accept_id(raw):
    """入接口宽松收: 字符串与整数都认, 校验后统一成 int 存库。"""
    if isinstance(raw, int):
        return raw
    if isinstance(raw, str) and raw.isdigit():
        return int(raw)
    raise ValueError("非法 id")


snowflake = 7266410535277015041  # 典型雪花 ID, 远超 2^53-1
payload = {"id": snowflake, "count": 42, "parent": -snowflake}
text = dump(payload)
assert '"id": "7266410535277015041"' in text and '"count": 42' in text
parsed = json.loads(text)
assert isinstance(parsed["id"], str)
assert accept_id(parsed["id"]) == snowflake and accept_id(42) == 42
try:
    accept_id("12x")
except ValueError as e:
    print("非法 id 拒收:", e)

as_double = int(float(snowflake))  # JS Number 是 IEEE 754 双精度, 尾数只有 53 位
assert as_double != snowflake, "JS 端 JSON.parse 会静默丢精度"
print("Python 往返无损, 但 JS 拿到 Number 会变成 %d, 字符串传输才无损" % as_double)
print("安全范围 %d; 超限自动转字符串, 双向约定: 出转串, 入两者都收" % MAX_SAFE)
