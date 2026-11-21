"""keyspace 通知: 过期事件何时发出 与 为什么不能当定时器用"""

class FakeRedis:
    def __init__(self):
        self.kv, self.expire_at = {}, {}
        self.events = []
        self.now = 1000.0

    def setex(self, key, ttl):
        self.kv[key] = "v"
        self.expire_at[key] = self.now + ttl

    def advance(self, dt):
        """时间推进; redis 的过期由访问时懒检查与后台周期抽样两条路径触发"""
        self.now += dt
        for k in list(self.kv):
            if self.now >= self.expire_at.get(k, 0):
                del self.kv[k]
                self.events.append(("expired", k, self.now))

r = FakeRedis()
r.setex("job:1", 5)
r.setex("job:2", 5)
r.advance(3)
print("3 秒后事件:", r.events, "-> 没人访问且后台未扫到, 事件还没发")
r.advance(10)
print("13 秒后事件:", r.events)
print("两个不可靠性:")
print("  1) 发出时机取决于到期后被访问或被周期抽样扫到, 延迟不可控")
print("  2) 订阅是 fire-and-forget, 订阅端掉线期间的事件永久丢失, 无重放")
print("正确姿势: keyspace 通知只做旁路观察与清理; 业务定时用延迟队列 zset 或 Stream, 外部调度器兜底对账")
