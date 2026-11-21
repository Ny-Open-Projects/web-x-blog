"""字段级过期模拟: hash 没有 HMEXPIRE 时的两种工程解法"""

NOW = 1000.0

class FieldTTLHash:
    """解法一: 值与到期时间戳成对存储, 读时懒清理"""

    def __init__(self):
        self.data, self.expire_at = {}, {}

    def hset(self, field, value, ttl):
        self.data[field] = value
        self.expire_at[field] = NOW + ttl

    def hget(self, field):
        if field in self.data and NOW >= self.expire_at.get(field, NOW + 1):
            self.data.pop(field)              # 懒清理
            self.expire_at.pop(field)
            return None
        return self.data.get(field)

    def purge(self):
        dead = [f for f in self.expire_at if NOW >= self.expire_at[f]]
        for f in dead:
            self.data.pop(f, None)
            self.expire_at.pop(f, None)
        return dead

h = FieldTTLHash()
h.hset("session:a", "tok-a", 60)
h.hset("session:b", "tok-b", 5)
print("立即读 b:", h.hget("session:b"))
h.expire_at = {k: v - 6 for k, v in h.expire_at.items()}   # 时间推进 6 秒
print("6 秒后读 b:", h.hget("session:b"), "(懒清理命中)")
print("6 秒后读 a:", h.hget("session:a"))
print("后台清扫移除:", h.purge())

print("解法二: 用 zset 以到期时间为分值建索引, 周期按分数段批量删除")
deadlines = {1000 + 5: "session:b", 1000 + 60: "session:a"}
due = [f for t, f in sorted(deadlines.items()) if t <= NOW + 6]
print("zrangebyscore 到期字段:", due, "-> HDEL 批删 加 ZREM 索引")
print("要点: 字段级 TTL 是模拟实现, 读路径要懒清理, 后台要有扫描兜底; 强一致过期不要依赖它")
