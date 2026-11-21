"""可读性优先的重构:一行流换成有名字的中间步骤。"""

ORDERS = [
    {"user": "u1", "amount": 120, "paid": True},
    {"user": "u2", "amount": 80, "paid": False},
    {"user": "u1", "amount": 200, "paid": True},
    {"user": "u3", "amount": 0, "paid": True},
]


def dense(orders, target="u1"):
    """一行流:口径全部藏在一个表达式里,难评审难调试。"""
    return sum(o["amount"] for o in orders
               if o["paid"] and o["amount"] > 0 and o["user"] == target)


def readable(orders, target="u1"):
    """命名中间步骤:每个口径一行,可单点打断点与单测。"""
    payable = [o for o in orders if o["paid"]]
    positive = [o for o in payable if o["amount"] > 0]
    mine = [o["amount"] for o in positive if o["user"] == target]
    return sum(mine)


if __name__ == "__main__":
    assert dense(ORDERS) == readable(ORDERS)
    print("结果一致:", readable(ORDERS))
    print("参数化复用:", readable(ORDERS, target="u2"))
    print("重构要点:口径提为中间名、条件逐条展开、写死值参数化")
