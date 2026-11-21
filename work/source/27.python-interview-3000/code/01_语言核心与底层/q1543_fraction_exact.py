from decimal import Decimal
from fractions import Fraction


def split_profit(total, ratios):
    """按精确比例分摊,最后一份兜底,保证总和精确等于 total。"""
    denom = sum(ratios)
    shares = [total * r / denom for r in ratios[:-1]]
    shares.append(total - sum(shares))
    return shares


if __name__ == "__main__":
    third = Fraction(1, 3)
    print("1/3 * 3 =", third * 3, "| float:", 1 / 3 * 3)

    f = Fraction(0.1)                   # float 的精确分数形态
    print("Fraction(0.1) =", f)
    print("limit_denominator:", f.limit_denominator(),
          "=", float(f.limit_denominator()))

    print("from str  :", Fraction("3/4"), Fraction("0.125"))
    print("from Dec  :", Fraction(Decimal("0.75")))
    print("auto gcd  :", Fraction(6, 8), "->",
          Fraction(6, 8).numerator, "/", Fraction(6, 8).denominator)
    print("compare   :", Fraction(1, 2) == 0.5, Fraction(1, 3) > 0.333)

    ratios = (Fraction(1, 3), Fraction(1, 4), Fraction(5, 12))
    shares = split_profit(Fraction(1000), ratios)
    print("shares:", shares, "sum:", sum(shares))

    try:
        Fraction(1, 2) + Decimal("0.5")
    except TypeError:
        print("Fraction + Decimal -> TypeError, 先构造再算:",
              Fraction(1, 2) + Fraction(Decimal("0.5")))
