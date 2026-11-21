from decimal import Decimal, ROUND_HALF_UP, getcontext

if __name__ == "__main__":
    print("exact addition:", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

    total = Decimal("19.99") * 3
    print("total:", total)
    print("per 7:", (total / 7).quantize(Decimal("0.01"), ROUND_HALF_UP))

    getcontext().prec = 4
    print("precision 4:", Decimal(2) / Decimal(3))
    getcontext().prec = 28

    print("float ctor keeps error:", Decimal(0.1))
    print("str ctor is exact   :", Decimal("0.1"))
