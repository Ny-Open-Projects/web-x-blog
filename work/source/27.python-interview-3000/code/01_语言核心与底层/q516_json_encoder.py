import json
from datetime import datetime
from decimal import Decimal
from enum import Enum

class Status(Enum):
    OK = "ok"
    FAIL = "fail"

class AppEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, Decimal):
            return str(o)                     # 不转 float:保精度
        if isinstance(o, Enum):
            return o.value
        return super().default(o)

if __name__ == "__main__":
    payload = {
        "at": datetime(2026, 11, 1, 10, 0),
        "price": Decimal("19.99"),
        "status": Status.OK,
    }
    print(json.dumps(payload, cls=AppEncoder, sort_keys=True, ensure_ascii=False))
    try:
        json.dumps(payload)
    except TypeError as e:
        print("plain encoder:", e)
