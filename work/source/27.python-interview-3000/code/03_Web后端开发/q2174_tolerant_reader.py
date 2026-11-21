"""容错读取者: 未知字段与未知枚举值的兼容策略(纯标准库)。"""


class StrictError(Exception):
    pass


def tolerant_parse(payload, known_fields):
    """忽略未知字段: provider 加字段不破坏老客户端。"""
    return {k: v for k, v in payload.items() if k in known_fields}


def strict_parse(payload, known_fields):
    for k in payload:
        if k not in known_fields:
            raise StrictError("未知字段: " + k)
    return dict(payload)


def parse_state(value, known_states, policy):
    """未知枚举值: 宽容策略归一到兜底值, 严格策略抛错; 禁止静默当默认值。"""
    if value in known_states:
        return value
    if policy == "tolerant":
        return "unknown"
    raise StrictError("未知状态: " + value)


OLD_FIELDS = {"id", "state"}
new_response = {"id": "o-1", "state": "paid", "tax_cents": 900, "loyalty_points": 30}
print("宽容解析:", tolerant_parse(new_response, OLD_FIELDS))
try:
    strict_parse(new_response, OLD_FIELDS)
except StrictError as exc:
    print("严格解析崩了:", exc)

states = {"created", "paid", "shipped"}
print("未知枚举 refunded -> 宽容:", parse_state("refunded", states, "tolerant"), end="")
try:
    parse_state("refunded", states, "strict")
except StrictError:
    print(" | 严格: 抛错")
print("要点: 容错读取者是'加字段无害'承诺的前提; 字段可忽略, 枚举必须归一兜底并打点, 不能静默")
