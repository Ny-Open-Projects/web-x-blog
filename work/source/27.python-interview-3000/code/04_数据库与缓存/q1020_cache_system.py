"""商品详情缓存体系骨架: 两级缓存 + 逻辑过期 + singleflight + 防穿透"""
import time

class ProductCacheSystem:
    def __init__(self, db, capacity=2):
        self.db = db
        self.l1, self.l2 = {}, {}
        self.logic_expire = {}                   # 逻辑过期时间
        self.null_cache = set()                  # 空值防穿透
        self.bloom = set()                       # 演示用简化布隆
        self.sf_locks = {}

    def warm(self, ids):
        self.bloom.update(ids)

    def get(self, pid):
        if pid not in self.bloom or pid in self.null_cache:
            return None                          # 防穿透: 肯定不存在
        now = time.monotonic()
        if pid in self.l1:
            return self.l1[pid], "L1"
        if pid in self.l2 and self.logic_expire[pid] > now:
            self.l1[pid] = self.l2[pid]          # 未到期直接用
            return self.l2[pid], "L2"
        # 到期: 逻辑过期异步重建(演示为同步 + 合并)
        v = self.db[pid]
        self.l2[pid], self.logic_expire[pid] = v, now + 5
        self.l1[pid] = v
        return v, "DB 回源"

    def update_price(self, pid, price):
        self.db[pid] = {**self.db[pid], "price": price}
        self.l2.pop(pid, None)                   # 删 L2
        self.l1.pop(pid, None)                   # 广播失效 L1(同进程演示)

if __name__ == "__main__":
    db = {1001: {"name": "键盘", "price": 199}}
    sys_ = ProductCacheSystem(db)
    sys_.warm([1001])
    print("首次读:", sys_.get(1001))
    print("二次读:", sys_.get(1001), "<- L1 命中")
    sys_.update_price(1001, 179)
    print("改价后读:", sys_.get(1001), "<- 回源新值")
    print("不存在商品:", sys_.get(9999), "<- 布隆拦截, 不打 DB")
    print("生产还需: binlog 兜底删除 / 熔断限流 / 对账 / 多分片容量规划")
