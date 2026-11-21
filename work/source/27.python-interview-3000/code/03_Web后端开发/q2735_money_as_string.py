"""浮点金额的字符串传输: Decimal 进出, float 拒收(纯标准库)。"""
import json
import re
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

CENT = Decimal("0.01")
MONEY_RE = re.compile(r"^-?\d+(\.\d+)?$")  # 明令禁止科学计数法与千分位
MONEY_MAX = Decimal("99999999.99")


def money_out(value):
    """出接口: Decimal 量化到分后按字符串给, currency 与 scale 一并声明。"""
    d = Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)
    return {"amount": str(d), "currency": "CNY", "scale": 2}


def money_in(raw):
    """入接口: 只收字符串或整数, float 直接拒收; 规则写进接口文档。"""
    if isinstance(raw, float):
        raise TypeError("金额禁止 float 进接口")
    if isinstance(raw, str):
        if not MONEY_RE.match(raw):
            raise ValueError("非法金额格式")
        d = Decimal(raw)
    elif isinstance(raw, int):
        d = Decimal(raw)
    else:
        raise ValueError("金额必须是字符串或整数")
    if abs(d) > MONEY_MAX:
        raise ValueError("超出金额上限")
    return d.quantize(CENT, rounding=ROUND_HALF_UP)


a = money_in("0.1")
b = money_in("0.2")
assert a + b == Decimal("0.30"), "Decimal 算术精确"
assert float(0.1) + float(0.2) == 0.30000000000000004, "float 的坑留在演示里"

out = money_out(a + b)
assert out == {"amount": "0.30", "currency": "CNY", "scale": 2}
text = json.dumps({"total": out})
back = money_in(json.loads(text)["total"]["amount"])
assert back == Decimal("0.30"), "字符串往返无损"

for bad in (0.1, "12.3.4", "1e3"):
    try:
        money_in(bad)
    except (TypeError, ValueError) as e:
        print("拒收 %-8r -> %s" % (bad, type(e).__name__))
print("约定: 金额一律字符串带币种与小数位, 服务端 Decimal 量化到分后再入库")
