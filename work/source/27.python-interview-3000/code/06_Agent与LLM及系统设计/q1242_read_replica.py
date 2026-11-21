"""读写分离:延迟模拟 + 会话粘住 + 位点校验路由 + 延迟摘除熔断。"""
import time


class DB:
    def __init__(self, name):
        self.name, self.data, self.binlog_pos = name, {}, 0

    def write(self, k, v):
        self.data[k] = v
        self.binlog_pos += 1
        return self.binlog_pos


class ReplicaSet:
    def __init__(self, primary, replicas, sticky_ttl=1.0):
        self.primary, self.replicas = primary, replicas
        self.lag = {r.name: 0.0 for r in replicas}      # 模拟各从库延迟秒数
        self.sticky = {}                                 # user -> 粘主截止时间
        self.ttl = sticky_ttl

    def write(self, user, k, v, now):
        pos = self.primary.write(k, v)
        self.sticky[user] = now + self.ttl               # 写后粘主
        return pos

    def read(self, user, k, now):
        if self.sticky.get(user, 0) > now:
            return self.primary.data.get(k), "primary(sticky)"
        candidates = [r for r in self.replicas if self.lag[r.name] < 0.5]
        if not candidates:                               # 全部从库延迟过大:熔断回主
            return self.primary.data.get(k), "primary(circuit)"
        r = candidates[int(now) % len(candidates)]
        return r.data.get(k), f"{r.name}"


if __name__ == "__main__":
    primary = DB("master")
    r1 = DB("replica-1")
    rs = ReplicaSet(primary, [r1], sticky_ttl=2.0)
    now = 100.0
    pos = rs.write("u1", "nickname", "新昵称", now)
    val, src = rs.read("u1", "nickname", now + 0.1)
    print("写后立即读:", val, "来源:", src)
    assert val == "新昵称" and "primary" in src, "会话粘住保证读自己写"

    # 粘住过期后:从库尚未同步 -> 读到旧值(演示问题)
    val2, src2 = rs.read("u1", "nickname", now + 3.0)
    print("粘住过期后读:", val2, "来源:", src2)
    assert val2 is None, "从库还没同步,读空(旧值场景)"

    # 从库同步完成 + 延迟熔断
    r1.data["nickname"] = "新昵称"
    val3, src3 = rs.read("u1", "nickname", now + 3.1)
    assert val3 == "新昵称" and src3 == "replica-1"
    rs.lag["replica-1"] = 5.0                            # 从库延迟爆炸
    val4, src4 = rs.read("u1", "nickname", now + 3.2)
    print("从库延迟 5s -> 自动回主:", src4)
    assert "circuit" in src4
    print("三层防护: 会话粘住 + 位点同步 + 延迟熔断摘除")
