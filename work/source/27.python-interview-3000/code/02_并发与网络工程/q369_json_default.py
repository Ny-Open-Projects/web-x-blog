"""json 自定义序列化与反序列化。"""
import datetime as dt
import json
from decimal import Decimal


def json_default(obj):
    if isinstance(obj, (dt.datetime, dt.date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return str(obj)  # 金额转字符串,防浮点精度丢失
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def _revive(d: dict):
    if "created_at" in d:
        d["created_at"] = dt.datetime.fromisoformat(d["created_at"])
    return d


class Order:
    def __init__(self):
        self.id = "A001"
        self.amount = Decimal("19.99")
        self.tags = {"vip", "paid"}
        self.created_at = dt.datetime(2026, 11, 1, 10, 0, 0)


if __name__ == "__main__":
    order = Order()
    text = json.dumps(order.__dict__, default=json_default, ensure_ascii=False, indent=2)
    print(text)
    back = json.loads(text, object_hook=_revive)
    print(type(back["created_at"]), back["amount"])
