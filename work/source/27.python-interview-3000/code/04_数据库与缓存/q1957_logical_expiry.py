"""逻辑过期与物理过期: 过期瞬间的阻塞与旧值服务"""

class PhysicalCache:
    """物理过期: 过期即删 击穿瞬间的并发请求都要等同一把重建锁"""
    def __init__(self):
        self.store = {}
        self.blocked = 0
    def get_batch(self, key, now, rebuild, n):
        """n 个请求在同一过期时刻并发到达"""
        item = self.store.get(key)
        if item and item[1] > now:
            return [(item[0], "hit")] * n
        results = []
        fresh = None
        for i in range(n):
            if i == 0:
                fresh = rebuild()                 # 只有一个人拿到锁
                self.store[key] = (fresh, now + 10)
                results.append((fresh, "拿到锁 重建后返回"))
            else:
                results.append((fresh, "阻塞等锁后返回"))   # 其余全在等同一把锁
            self.blocked += 1
        return results

class LogicalCache:
    """逻辑过期: 值永不物理删除 条目自带过期时间 过期后单飞异步重建 期间继续供旧值"""
    def __init__(self):
        self.store = {}
        self.rebuild_count = 0
    def preload(self, key, value, now):
        self.store[key] = [value, now + 10, False]
    def get_batch(self, key, now, rebuild, n):
        item = self.store.get(key)
        if item is None:
            return [(None, "miss")] * n
        if item[1] > now:
            return [(item[0], "hit")] * n
        results = []
        if not item[2]:                            # 只放一个请求去重建
            item[2] = True
            self.rebuild_count += 1
            item[0] = rebuild()                    # 模拟异步线程完成后写回
            item[1] = now + 10
            item[2] = False
            results.append((item[0], "触发异步重建"))
        for _ in range(n - 1):
            results.append((item[0], "拿旧值 立即返回"))
        return results

now = 100
counter = [0]
def rebuild():
    counter[0] += 1
    return "v%d" % counter[0]

p = PhysicalCache()
out = p.get_batch("hot", now, rebuild, 5)
print("物理过期 5 个并发请求 ->", out, f" 全部阻塞参与重建 {p.blocked} 次")

l = LogicalCache()
l.preload("hot", "v0", now)
stale_now = 111                               # 已过逻辑过期点
res = l.get_batch("hot", stale_now, rebuild, 5)
print("逻辑过期 5 个并发请求 ->", res, f" 触发重建 {l.rebuild_count} 次 其余拿旧值不阻塞")
print("结论: 物理过期实现简单但击穿瞬间全员等锁 逻辑过期用旧值兜底重建收敛到一次 代价是短暂脏读")
