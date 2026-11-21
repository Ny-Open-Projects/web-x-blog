"""Q2603 副本选择的路由表:本地优先,权重次之,健康一票否决。

路由表四个字段定一次选择:健康一票否决,同区里挑权重最高的,
本区没有才跨区兜底;流量分配另用加权随机,与确定性选主解耦。
"""
import random
from collections import Counter

TABLE = [
    {"name": "sh-1", "region": "sh", "weight": 5, "healthy": True},
    {"name": "sh-2", "region": "sh", "weight": 3, "healthy": True},
    {"name": "bj-1", "region": "bj", "weight": 9, "healthy": True},
]


def alive_pool(table, region):
    alive = [r for r in table if r["healthy"]]
    if not alive:
        return []
    local = [r for r in alive if r["region"] == region]
    return local or alive


def pick(table, region):
    pool = alive_pool(table, region)
    return max(pool, key=lambda r: r["weight"]) if pool else None


def pick_weighted(table, region, rng):
    pool = alive_pool(table, region)
    if not pool:
        return None
    total = sum(r["weight"] for r in pool)
    x = rng.random() * total
    acc = 0.0
    for r in pool:
        acc += r["weight"]
        if x <= acc:
            return r
    return pool[-1]


def main():
    assert pick(TABLE, "sh")["name"] == "sh-1"   # 本地最高权重
    assert pick(TABLE, "gz")["name"] == "bj-1"   # 无本地,跨区兜底
    TABLE[0]["healthy"] = False
    assert pick(TABLE, "sh")["name"] == "sh-2"
    TABLE[1]["healthy"] = False
    assert pick(TABLE, "sh")["name"] == "bj-1"   # 全城不健康,跨区
    TABLE[0]["healthy"] = TABLE[1]["healthy"] = True
    rng = random.Random(11)
    c = Counter(pick_weighted(TABLE, "sh", rng)["name"] for _ in range(1000))
    assert c["sh-1"] + c["sh-2"] == 1000
    assert 580 < c["sh-1"] < 680, c              # 权重 5:3 → 约 62.5%
    print("确定性选路:本地优先跨区兜底")
    print("千次加权随机分布:", dict(c), "≈ 权重 5:3")


if __name__ == "__main__":
    main()
