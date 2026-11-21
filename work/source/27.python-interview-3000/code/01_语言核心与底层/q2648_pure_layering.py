"""纯函数分层:决策在纯函数,副作用只在边缘薄薄一层。"""
from datetime import datetime, timezone


def calc_shipping(weight_kg, express, base_fee, now_hour):
    """纯函数:所有规则在这里,可离线穷举测试。"""
    fee = base_fee + weight_kg * 5
    if express:
        fee += 20
    if now_hour >= 22 or now_hour < 6:      # 深夜加急费
        fee += 10
    return round(fee, 2)


def ship_order(order, gateway):
    """边缘:只负责取时钟、调外部,不写规则。"""
    now_hour = datetime.now(timezone.utc).hour
    fee = calc_shipping(order["weight"], order["express"],
                        base_fee=8, now_hour=now_hour)
    gateway.charge(order["id"], fee)
    return fee


class FakeGateway:
    def __init__(self):
        self.charged = []

    def charge(self, order_id, amount):
        self.charged.append((order_id, amount))


if __name__ == "__main__":
    # 核心规则:直接测纯函数,无 mock 无环境
    cases = [(1, False, 10, 13), (1, True, 10, 13), (2, False, 10, 13), (1, True, 10, 23)]
    for weight, express, base, hour in cases:
        print(f"calc_shipping({weight}, {express}, h={hour}) =",
              calc_shipping(weight, express, base, hour))

    fake = FakeGateway()
    fee = ship_order({"id": "o1", "weight": 2, "express": True}, fake)
    print("边缘层编排结果:", fee, fake.charged)
