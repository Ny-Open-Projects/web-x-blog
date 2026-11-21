---
title: [Q1223] Redlock 思想与争议
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1223 · Redlock 思想与争议

> 难度:★★★★ | 标签:分布式锁, 一致性

**问**:Redlock 是什么?Kleppmann 为什么要挑战它?你会在什么场景用它?

**答**:Redlock:在 N 个(通常 5)独立 Redis 实例上加同一把锁,单个实例超时短,拿过半(≥3)且总耗时小于锁 TTL 才算成功;失败则向全部实例发释放。目的:单实例主从切换丢锁的问题用多数派缓解。Kleppmann 的批评:一是锁的正确性依赖时钟假设(GC 停顿/时钟跳变会让持锁方"以为自己还有锁");二是它仍不是 fencing token 体系,持有过期锁的客户端可能继续写。共识: Redlock 适合"效率锁"(防重复劳动,错了损失小);正确性关键路径(资金)要靠下游幂等/fencing token 兜底,不能只靠锁。

```python
# file: code/06_Agent与LLM及系统设计/q1223_redlock.py
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
```

**追问**:
- fencing token 的值从哪来?答:锁服务在授予锁时发单调递增序号,存储层记住见过的最大值,小值写入直接拒绝——它把"锁的正确性"转化为"存储的幂等校验"。
- 效率锁怎么用最稳?答:接受偶发双跑,下游幂等去重(同 job id 只执行一次),锁只做"减少重复"的优化,正确性永不依赖它。
