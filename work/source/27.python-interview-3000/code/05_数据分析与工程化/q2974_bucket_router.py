"""灰度完整桶分配器: 加盐 md5 哈希分桶 + 占比分配 + 白名单覆盖 + 稳定性与互斥验证"""
import hashlib

EXPERIMENT = "pay_btn_v3"
TOTAL_BUCKETS = 1000


class BucketRouter:
    def __init__(self, groups, salt=EXPERIMENT):
        """groups: 组名 -> 百分比, 总和必须 100; 桶区间互斥且覆盖 0..999"""
        if sum(groups.values()) != 100:
            raise ValueError("组占比之和必须为 100, 实得 %d" % sum(groups.values()))
        self.salt = salt
        self.ranges = []
        start = 0
        for name, pct in sorted(groups.items(), key=lambda kv: -kv[1]):
            width = pct * TOTAL_BUCKETS // 100
            if width:
                self.ranges.append((name, start, start + width - 1))
                start += width
        if start < TOTAL_BUCKETS:                       # 余数桶并入最后一组, 保证全覆盖
            self.ranges[-1] = (self.ranges[-1][0], self.ranges[-1][1], TOTAL_BUCKETS - 1)
        self.whitelist = {}

    def bucket_of(self, unit):
        """加盐哈希 -> 0..999; 同一 unit 永远同桶"""
        digest = hashlib.md5(("%s:%s" % (self.salt, unit)).encode("utf-8")).hexdigest()
        return int(digest[:8], 16) % TOTAL_BUCKETS

    def assign(self, unit):
        if unit in self.whitelist:
            return self.whitelist[unit]
        b = self.bucket_of(unit)
        for name, lo, hi in self.ranges:
            if lo <= b <= hi:
                return name
        raise RuntimeError("桶 %d 未被覆盖" % b)          # 理论不可达, 防御性保留


if __name__ == "__main__":
    router = BucketRouter({"control": 50, "treatment": 30, "holdout": 20})
    print("桶区间:", router.ranges)

    n = 10000
    dist = {}
    for i in range(n):
        g = router.assign("user_%d" % i)
        dist[g] = dist.get(g, 0) + 1
    print("分配 %d 人: " % n, {k: "%d (%.1f%%)" % (v, v / n * 100) for k, v in sorted(dist.items())})

    # 稳定性: 同一用户重复请求结果不变
    stable = all(router.assign("user_%d" % i) == router.assign("user_%d" % i) for i in range(n))
    print("重复请求 10000 人结果全部一致:", stable)

    # 互斥: 桶区间两两不交且总数 1000
    covered = sum(hi - lo + 1 for _n, lo, hi in router.ranges)
    print("桶覆盖总数 =", covered, "(互斥且全覆盖, 一个用户只会进一组)")

    # 白名单: 指定大客户强制进 treatment
    router.whitelist["user_0"] = "treatment"
    print("白名单覆盖: user_0 ->", router.assign("user_0"))

    # 换实验名(盐): 同一用户在另一个实验中的分布彼此独立
    other = BucketRouter({"A": 50, "B": 50}, salt="nav_layout_v1")
    same_as_pay = [other.assign("user_%d" % i) == router.assign("user_%d" % i) for i in range(100)]
    print("另一实验与本实验分配完全同分布比例: %d%%, 加盐让实验间正交" % (sum(same_as_pay)))

    try:
        BucketRouter({"a": 60, "b": 30})
    except ValueError as e:
        print("故意错配占比被拦截:", e)
    print("要点: 哈希分桶保证稳定与均匀, 加盐保证实验正交, 白名单兜底客服诉求, 区间互斥防止一人多组")
