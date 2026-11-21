
class PriceClient:
    def get_price(self, sku):
        raise RuntimeError("真实网络调用")

def total_price(client, items):
    return sum(client.get_price(sku) * qty for sku, qty in items)

class MonkeyPatch:
    """模拟 pytest 的 monkeypatch:退出自动还原"""

    def __init__(self):
        self._undo = []

    def setattr(self, obj, name, value):
        old = getattr(obj, name)
        setattr(obj, name, value)
        self._undo.append(lambda: setattr(obj, name, old))

    def undo(self):
        for fn in reversed(self._undo):
            fn()

class SpyClient:
    """spy 记录调用,供交互断言,mocker 的典型用法"""

    def __init__(self):
        self.calls = []

    def get_price(self, sku):
        self.calls.append(sku)
        return 100

if __name__ == "__main__":
    items = [("A", 2), ("B", 1)]
    patch = MonkeyPatch()
    patch.setattr(PriceClient, "get_price", lambda self, sku: 10)
    assert total_price(PriceClient(), items) == 30
    patch.undo()
    spy = SpyClient()
    total_price(spy, items)
    assert spy.calls == ["A", "B"]
    print("monkeypatch 换行为,spy/mocker 验证交互,边界清晰")
