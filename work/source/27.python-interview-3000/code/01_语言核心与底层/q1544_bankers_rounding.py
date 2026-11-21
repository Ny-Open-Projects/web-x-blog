from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

CASES = [0.5, 1.5, 2.5, 3.5, -0.5, -2.5]


def show_half_even():
    return [round(x) for x in CASES]


if __name__ == "__main__":
    print("round cases:", list(zip(CASES, show_half_even())))

    print("2.675 ->", round(2.675, 2), "| stored as:", Decimal(2.675))
    print("format same:", f"{2.675:.2f}")

    # ndigits 为负:舍到十位百位
    print("round(1234, -2):", round(1234, -2),
          "| round(1250, -2):", round(1250, -2), " 半到偶")

    # 财务口径:Decimal 显式 HALF_UP
    money = Decimal("2.675")
    print("decimal half_up  :", money.quantize(Decimal("0.01"), ROUND_HALF_UP))
    print("decimal half_even:", money.quantize(Decimal("0.01"), ROUND_HALF_EVEN))

    # Decimal 的 round 也走 half-even(上下文舍入)
    print("round(Decimal):", round(Decimal("2.5")), round(Decimal("3.5")))
