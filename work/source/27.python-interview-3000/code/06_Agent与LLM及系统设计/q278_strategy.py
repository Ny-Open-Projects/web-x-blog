from decimal import Decimal


def vip_price(price: Decimal) -> Decimal:
    return price * Decimal("0.8")


def new_user_price(price: Decimal) -> Decimal:
    return price * Decimal("0.9")


def default_price(price: Decimal) -> Decimal:
    return price


STRATEGIES = {
    "vip": vip_price,
    "new": new_user_price,
    "default": default_price,
}


def calc_price(user_type: str, price: Decimal) -> Decimal:
    return STRATEGIES.get(user_type, default_price)(price)


class DiscountStrategy:
    """面向对象的策略写法,适合策略本身有状态的场景。"""
    def apply(self, price: Decimal) -> Decimal:
        raise NotImplementedError


class FullCut(DiscountStrategy):
    def __init__(self, threshold: Decimal, cut: Decimal):
        self.threshold, self.cut = threshold, cut

    def apply(self, price: Decimal) -> Decimal:
        return price - self.cut if price >= self.threshold else price


if __name__ == "__main__":
    print(calc_price("vip", Decimal("100")))   # 80.0
    print(calc_price("xxx", Decimal("100")))   # 100
    print(FullCut(Decimal("100"), Decimal("20")).apply(Decimal("120")))
