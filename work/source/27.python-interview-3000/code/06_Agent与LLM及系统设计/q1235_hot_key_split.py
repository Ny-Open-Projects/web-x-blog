"""热点 key 打散:逻辑 key 加盐为 N 物理键,读随机分摊,统计打散效果。"""
import random
from collections import Counter


class ShardCache:
    def __init__(self, nodes=4):
        self.nodes = {f"node{i}": {} for i in range(nodes)}

    def write_hot(self, logical_key, value, salt_n):
        for i in range(salt_n):
            pk = f"{logical_key}#{i}"
            node = f"node{i % len(self.nodes)}"      # 盐键按序号均匀落节点
            self.nodes[node][pk] = value

    def read_hot(self, logical_key, salt_n):
        i = random.randrange(salt_n)               # 读随机选一份
        pk = f"{logical_key}#{i}"
        return self.nodes[f"node{i % len(self.nodes)}"].get(pk)


if __name__ == "__main__":
    random.seed(2)
    cache = ShardCache(nodes=4)

    # 不加盐:1000 次读全打同一物理 key 所在节点
    cache.write_hot("sku-1", "爆款详情", salt_n=1)
    print("不加盐: 单节点承受 1000 次读")

    # 加盐 8:读随机分摊到 8 个物理键、4 个节点
    cache.write_hot("sku-2", "爆款详情", salt_n=8)
    access = Counter()
    for _ in range(1000):
        i = random.randrange(8)
        access[f"node{i % 4}"] += 1
    print("加盐后各节点读压力:", dict(access))
    assert max(access.values()) < 400, "压力必须明显摊开"
    assert cache.read_hot("sku-2", 8) == "爆款详情"

    # 更新:全量刷 N 份保持一致
    cache.write_hot("sku-2", "新版详情", salt_n=8)
    vals = {cache.read_hot("sku-2", 8) for _ in range(16)}
    assert vals == {"新版详情"}, "更新后读到新值"
    print("写全量刷 N 份,读随机,一致性与分摊兼得(读多写少场景)")
