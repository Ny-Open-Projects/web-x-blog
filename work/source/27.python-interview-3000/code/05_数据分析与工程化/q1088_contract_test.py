
CONTRACT = {
    "type": "order",
    "fields": {
        "order_id": str,
        "user_id": int,
        "amount": float,
        "status": {"paid", "refund"},
    },
}

def validate_contract(payload):
    errors = []
    if payload.get("type") != CONTRACT["type"]:
        errors.append("type 不符")
    for k, t in CONTRACT["fields"].items():
        if k not in payload:
            errors.append(f"缺少字段 {k}")
        elif isinstance(t, set):
            if payload[k] not in t:
                errors.append(f"{k} 取值非法: {payload[k]}")
        elif not isinstance(payload[k], t):
            errors.append(f"{k} 类型应为 {t.__name__}")
    return errors

def provider_response():
    return {"type": "order", "order_id": "O1", "user_id": 7, "amount": 9.9, "status": "paid"}

if __name__ == "__main__":
    errs = validate_contract(provider_response())
    print("当前响应:", errs or "满足消费方契约")
    breaking = provider_response()
    breaking["status"] = "PAID"
    print("破坏性变更:", validate_contract(breaking))
