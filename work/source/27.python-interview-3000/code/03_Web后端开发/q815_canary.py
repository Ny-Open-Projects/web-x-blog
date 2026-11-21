
def route_canary(user_id: str, canary_pct: int) -> str:
    bucket = sum(ord(c) for c in user_id) % 100   # 稳定哈希分桶
    return "canary" if bucket < canary_pct else "stable"

alloc = {"canary": 0, "stable": 0}
for i in range(1000):
    alloc[route_canary(f"user{i}", 10)] += 1
print("灰度分流分布:", alloc)
print("同一用户稳定:", route_canary("user42", 10) == route_canary("user42", 10))
