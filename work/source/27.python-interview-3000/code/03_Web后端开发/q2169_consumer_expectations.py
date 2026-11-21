"""消费者期望的记录格式: 契约文件的最小字段集(纯标准库)。"""
import json

EXPECTATION = {
    "consumer": "mobile-app",
    "provider": "order-service",
    "recorded_from": "GET /v1/orders/{id}",
    "interactions": [
        {
            "description": "查一条已支付订单",
            "request": {"method": "GET", "path": "/v1/orders/o-100", "headers": {}},
            "expect": {
                "status": 200,
                "body_has": ["order_id", "total", "state"],
                "body_not_has": ["internal_cost", "supplier_id"],
                "types": {"order_id": "str", "total": "number", "state": "str"},
                "enum": {"state": ["created", "paid", "shipped"]},
            },
        },
        {
            "description": "不存在的订单返回 404 而不是 200 空体",
            "request": {"method": "GET", "path": "/v1/orders/nope"},
            "expect": {"status": 404},
        },
    ],
}

text = json.dumps(EXPECTATION, ensure_ascii=False, indent=2)
print(text)
loaded = json.loads(text)
assert loaded["interactions"][0]["expect"]["enum"]["state"] == ["created", "paid", "shipped"]
print("要点: 期望只描述消费者真正用到的东西; 未记录的字段不算契约, provider 可以自由增改")
