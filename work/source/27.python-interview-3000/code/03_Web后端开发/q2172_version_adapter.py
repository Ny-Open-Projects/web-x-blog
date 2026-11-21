"""双运行下的版本适配层: 一份领域模型, 多种线格式(纯标准库)。"""
from dataclasses import dataclass, field


@dataclass
class Order:
    id: str
    total_cents: int
    currency: str
    state: str
    risk_score: float = field(default=0.0, repr=False)   # 内部风控字段


def to_v1(order):
    """v1: 金额是元, 不暴露币种与风控内部字段。"""
    return {"id": order.id, "total": round(order.total_cents / 100, 2),
            "state": order.state}


def to_v2(order):
    """v2: 金额改为整数分并显式带币种。"""
    return {"id": order.id, "amount_cents": order.total_cents,
            "currency": order.currency, "state": order.state}


ADAPTERS = {"v1": to_v1, "v2": to_v2}
ORDER_REPOSITORY = {"o-1": Order("o-1", 12345, "CNY", "paid", risk_score=0.17)}


def handle(version, order_id):
    order = ORDER_REPOSITORY[order_id]              # 业务内核只查一次
    return 200, ADAPTERS[version](order)


for version in ["v1", "v2"]:
    print(version, "->", handle(version, "o-1")[1])
assert handle("v1", "o-1")[1]["total"] == 123.45
assert handle("v2", "o-1")[1]["amount_cents"] == 12345
assert "risk_score" not in handle("v1", "o-1")[1]
print("要点: 新版本只是注册一个新适配函数; 适配器只做单位换算与字段取舍, 业务规则禁止进适配层")
