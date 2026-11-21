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
