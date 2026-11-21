ledger: dict = {}

def charge(order_id: str, amount: int) -> str:
    if order_id in ledger:
        return f"幂等命中 {order_id}"
    ledger[order_id] = amount
    return f"扣款 {amount}"

print(charge("o1", 100))
print(charge("o1", 100))   # broker 重投也安全
print(charge("o2", 50))
