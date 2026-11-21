"""浮点误差演示与两种金额方案: Decimal 与整数分"""
from decimal import Decimal

if __name__ == "__main__":
    print("浮点:", 0.1 + 0.2, "== 0.3 ?", (0.1 + 0.2) == 0.3)
    print("Decimal:", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

    price = Decimal("19.99")
    qty = 3
    print("Decimal 金额:", price * qty)

    cents = 1999                       # 库里存分
    print("整数分金额:", cents * qty, "分 =", cents * qty / 100, "元")
    print("浮点做账的坑: 19.99 * 3 =", 19.99 * 3)
