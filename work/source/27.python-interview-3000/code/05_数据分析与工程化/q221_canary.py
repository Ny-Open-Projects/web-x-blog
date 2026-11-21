import hashlib


def assign_bucket(user_id: str, canary_percent: int = 5) -> str:
    # 稳定哈希分桶:同一用户永远落同一桶
    h = int(hashlib.md5(user_id.encode()).hexdigest(), 16) % 100
    return "canary" if h < canary_percent else "stable"


def test_bucket_stable():
    assert assign_bucket("u1", 5) == assign_bucket("u1", 5)

def test_bucket_ratio():
    users = [f"user-{i}" for i in range(1000)]
    canary = sum(1 for u in users if assign_bucket(u, 5) == "canary")
    assert 30 <= canary <= 70  # 约 5%
