"""用 Protocol 定义领域接口: 实现可替换, 业务零感知"""
from __future__ import annotations
from typing import Protocol
from dataclasses import dataclass

@dataclass(frozen=True)
class OrderId:
    value: int

@dataclass
class Order:                      # 领域对象, 不是 ORM 模型
    id: OrderId | None
    sku: str
    status: str = "created"

class OrderRepository(Protocol):
    def load(self, oid: OrderId) -> Order | None: ...
    def save(self, order: Order) -> None: ...
    def next_identity(self) -> OrderId: ...

class MemoryOrderRepo:            # 测试实现
    def __init__(self):
        self._data, self._seq = {}, 0
    def load(self, oid):
        return self._data.get(oid.value)
    def save(self, order):
        self._data[order.id.value] = order
    def next_identity(self):
        self._seq += 1
        return OrderId(self._seq)

def ship(repo: OrderRepository, oid: OrderId):
    order = repo.load(oid)
    assert order and order.status == "created", "订单不可发货"
    order.status = "shipped"
    repo.save(order)

if __name__ == "__main__":
    repo = MemoryOrderRepo()
    oid = repo.next_identity()
    repo.save(Order(id=oid, sku="x"))
    ship(repo, oid)
    print("发货成功:", repo.load(oid).status, "<- 业务代码不依赖任何 ORM")
