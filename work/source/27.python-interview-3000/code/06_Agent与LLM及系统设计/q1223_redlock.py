"""Redlock 桩:多数派获取 + 时钟漂移演示 + fencing token 兜底。"""


class RedisInstance:
    def __init__(self, name, clock_skew=0.0):
        self.name, self.holder, self.skew = name, None, clock_skew

    def lock(self, token, ttl):
        if self.holder is None:
            self.holder = (token, ttl * (1 + self.skew))   # 时钟漂移影响实际时长
            return True
        return False

    def unlock(self, token):
        if self.holder and self.holder[0] == token:
            self.holder = None
            return True
        return False


class Redlock:
    def __init__(self, instances, quorum=3):
        self.instances, self.quorum = instances, quorum

    def acquire(self, token, ttl):
        got = sum(1 for r in self.instances if r.lock(token, ttl))
        return got >= self.quorum

    def release(self, token):
        for r in self.instances:
            r.unlock(token)


class Resource:
    """受保护资源:用单调递增 fencing token 拒绝过期持有者。"""

    def __init__(self):
        self.state, self.fencing = "init", 0

    def write(self, token_id, fencing_token):
        if fencing_token < self.fencing:
            return f"rejected: fencing {fencing_token} < {self.fencing}"
        self.state, self.fencing = f"by-{token_id}", fencing_token
        return f"accepted fencing={fencing_token}"


if __name__ == "__main__":
    instances = [RedisInstance(f"r{i}") for i in range(5)]
    rl = Redlock(instances)
    ok = rl.acquire("client-A", ttl=10)
    print("client-A 获取:", ok)
    assert ok
    rl.release("client-A")
    ok2 = rl.acquire("client-B", ttl=10)
    print("client-B 接管:", ok2)
    assert ok2

    # GC 停顿场景:A 醒来以为自己仍持锁继续写
    res = Resource()
    res.write("B", fencing_token=2)          # B 用更大 token 写入
    out = res.write("A", fencing_token=1)    # A 的旧 token 被 fencing 拒绝
    print("A 携带过期锁写入:", out)
    assert "rejected" in out, "存储侧 fencing token 必须兜底"
    print("结论: Redlock 管效率,正确性由 fencing/幂等兜底")
