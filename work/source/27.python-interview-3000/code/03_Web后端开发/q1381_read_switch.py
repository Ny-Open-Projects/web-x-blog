"""读切放量:按主键确定性哈希的百分比开关(纯标准库)。"""
import hashlib


def bucket(key, percent):
    if percent >= 100:
        return "new"
    if percent <= 0:
        return "old"
    h = int(hashlib.md5(key.encode()).hexdigest(), 16) % 100
    return "new" if h < percent else "old"


users = [f"user{i}" for i in range(200)]
for percent in (0, 10, 50, 100):
    switched = sum(1 for u in users if bucket(u, percent) == "new")
    print(f"percent={percent:3d} -> 新库承载 {switched}/200")

print("同一用户多次判定:", [bucket("user42", 30) for _ in range(3)], "确定性,可稳定回切")
