
_counter = {"n": 0}

def make_user(**overrides):
    _counter["n"] += 1
    n = _counter["n"]
    user = {"id": n, "email": f"user{n}@t.io", "role": "member"}
    user.update(overrides)
    return user

def make_order(**overrides):
    order = {
        "id": len(overrides) + 1000,
        "user": overrides.pop("user", None) or make_user(),
        "amount": 9.9,
        "status": "paid",
    }
    order.update(overrides)
    return order

if __name__ == "__main__":
    orders = [make_order(amount=i) for i in range(1, 4)]
    for o in orders:
        print(o["id"], o["user"]["email"], o["amount"], o["status"])
    assert orders[0]["user"]["email"] != orders[1]["user"]["email"], "序列保证唯一"
    print("子工厂自动造用户,覆盖参数只写关心的字段")
