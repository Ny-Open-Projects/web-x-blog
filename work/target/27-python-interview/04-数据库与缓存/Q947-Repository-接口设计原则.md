---
title: [Q947] Repository 接口设计原则
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q947 · Repository 接口设计原则

> 难度:★★★★ | 标签:架构, Repository

**问**:好的 Repository 接口长什么样?哪些设计是"伪封装"?

**答**:四条原则:一、面向聚合根,接口粒度是领域动作(load_order、mark_paid)而非表操作(update_field_x);二、接口定义在领域层,实现在基础设施层,依赖向内(Python 用 Protocol/ABC 表达);三、方法签名用领域类型(领域对象、值对象)进出,不泄漏 ORM 实体与 Session;四、可测试性优先——同步接口 + 可替换实现。伪封装:返回 QuerySet/Select 让上层继续拼(等于没隔离)、暴露 save(orm_obj) 把 ORM 实体当 DTO、每个方法内部自带事务、方法名直译 SQL(find_by_name_and_status_and...)。判断标准:换掉 ORM,业务代码与测试不需要重写。

```python
# file: code/04_数据库与缓存/q947_repo_interface.py
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
```

**追问**:
- 领域对象与 ORM 实体要分开吗?——重领域逻辑的项目分开并在仓储内做映射;一般 CRUD 项目可共用,但要意识到这是务实取舍而非教条。
- 接口方法太多怎么办?——按用例拆分接口(读写分离),或审视聚合边界是否划错,膨胀的接口通常意味着仓储在管不属于它的聚合。

---
