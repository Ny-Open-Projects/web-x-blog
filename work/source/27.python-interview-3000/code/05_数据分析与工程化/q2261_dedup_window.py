"""上游重复投递的去重窗口: TTL 与容量的权衡"""

from collections import OrderedDict


class DedupCache:
    def __init__(self, ttl_events, capacity):
        self.ttl = ttl_events          # 用事件数近似时间窗
        self.capacity = capacity
        self.seen = OrderedDict()      # event_id -> 登记时的 tick

    def is_duplicate(self, event_id, tick):
        if event_id in self.seen:
            return True
        while self.seen and tick - next(iter(self.seen.values())) > self.ttl:
            self.seen.popitem(last=False)          # TTL 淘汰
        while len(self.seen) >= self.capacity:
            self.seen.popitem(last=False)          # 容量淘汰
        self.seen[event_id] = tick
        return False


STREAM = ["e1", "e2", "e3", "e2", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e2", "e12"]
# e2 重复三次: 距首次 2 个事件与 11 个事件

if __name__ == "__main__":
    for ttl, cap in [(2, 100), (15, 100), (15, 5)]:
        cache = DedupCache(ttl, cap)
        passed = [e for i, e in enumerate(STREAM) if not cache.is_duplicate(e, i)]
        print(f"窗口={ttl:>2} 容量={cap:>3}: 拦截重复 {len(STREAM) - len(passed)} 个, 放行 {len(passed)} 个")
    print("权衡: TTL 覆盖上游常见重投间隔, 容量覆盖窗口内峰值事件量; 拦截必须计数并抽样留样")
