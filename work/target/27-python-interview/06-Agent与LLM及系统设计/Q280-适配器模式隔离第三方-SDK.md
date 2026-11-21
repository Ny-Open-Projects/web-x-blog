---
title: [Q280] 适配器模式隔离第三方 SDK
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q280 · 适配器模式隔离第三方 SDK
> 难度:★★★ | 标签:设计模式, 隔离

**问**:项目直接调用第三方支付 SDK,对方 API 一变全项目要改,怎么治理?

**答**:用适配器模式定义自己领域的接口(如 `PaymentGateway.pay`),为每家三方写一个适配器把它的 API 翻译成内部接口。收益:三方变化被限制在适配器内;换供应商只换适配器;测试用内存适配器。这是防腐层(Anti-Corruption Layer)思想的落地。

```python
# file: code/06_Agent与LLM及系统设计/q280_adapter.py
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """内部统一支付接口,业务只认它。"""
    @abstractmethod
    def pay(self, order_id: str, amount_cents: int) -> str: ...


class ThirdPartySDK:
    """模拟一家风格古怪的三方 SDK。"""
    def do_transaction(self, oid: str, money_fen: int) -> dict:
        return {"ret": 0, "trade_no": "TP-" + oid, "fee": money_fen}


class ThirdPartyAdapter(PaymentGateway):
    def __init__(self, sdk: ThirdPartySDK):
        self._sdk = sdk

    def pay(self, order_id: str, amount_cents: int) -> str:
        res = self._sdk.do_transaction(order_id, amount_cents)
        if res["ret"] != 0:
            raise RuntimeError("pay failed")
        return res["trade_no"]


class FakeGateway(PaymentGateway):
    def pay(self, order_id: str, amount_cents: int) -> str:
        return f"FAKE-{order_id}-{amount_cents}"


if __name__ == "__main__":
    gw = ThirdPartyAdapter(ThirdPartySDK())
    print(gw.pay("o1", 9900))
    print(FakeGateway().pay("o1", 9900))
```

**追问**:
- 适配器层该多薄?——只做参数/响应格式翻译与错误码映射,不含业务逻辑;业务漏进适配器,防腐层就名存实亡。
- 三方接口变更怎么监控?——契约测试(响应结构断言)+ 灰度探活;SDK 大版本升级在适配器内消化,业务无感。
- 测试怎么用内存适配器?——实现同一接口的 InMemory 版,单测不碰网络;行为细节(错误、超时)也模拟出来。

---
