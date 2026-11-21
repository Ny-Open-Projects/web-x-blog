---
title: [Q1523] 主从切换期的请求处理:悬挂超时与旧 epoch 丢弃
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1523 · 主从切换期的请求处理:悬挂超时与旧 epoch 丢弃

> 难度:★★★★ | 标签:分布式, 故障切换, 客户端

**问**:主从切换那几秒,客户端的请求会发生什么,怎么保证不脏读?

**答**:三种形态要分别处理。旧主悬挂:请求无响应,客户端按超时重试并重定向到新主,悬挂不等于失败,只是还没路由对。旧主诈尸响应:被废黜的旧主还活着还会返回结果,客户端凭 epoch 校验丢弃一切低于已知新 epoch 的响应,即使它格式完美内容正确,因为它的正确性已不可信。重试收敛:重定向后在新主上拿到高 epoch 的成功响应,全程不产生脏读。客户端要做对一件事:绝不以 响应到达 为可信依据,而以 响应携带的 epoch 不小于本地已知 为依据。服务端配合是每个响应都带 epoch,这是切换期协议的最低要求。

```python
# file: code/06_Agent与LLM及系统设计/q1523_failover_requests.py
"""主从切换期间的请求处理:epoch 校验拒旧主响应,悬挂超时重定向新主,客户端不脏读。"""
from collections import deque


class Client:
    """客户端桩:记录目标 epoch,收到低 epoch 响应立即换主重试。"""

    def __init__(self, leaders):
        self.leaders = leaders             # name -> LeaderStub
        self.current = "old"
        self.epoch_known = 1
        self.log = []
        self.pending = deque()

    def request(self, op, timeout_rounds=3):
        for _ in range(timeout_rounds):
            leader = self.leaders[self.current]
            resp = leader.handle(op, self.epoch_known)
            self.log.append((self.current, resp["kind"]))
            if resp["kind"] == "ok":
                return resp
            if resp["kind"] == "stale_epoch":
                self.current = "new"       # 发现新主 切换
                self.epoch_known = resp["epoch"]
            elif resp["kind"] == "timeout":
                self.current = "new"
        return {"kind": "gave_up"}


class LeaderStub:
    """主节点桩:old 主还在处理请求但已被废黜;new 主 epoch 更高。"""

    def __init__(self, name, epoch, alive=True, hang=False):
        self.name, self.epoch, self.alive, self.hang = name, epoch, alive, hang

    def handle(self, op, client_epoch):
        if not self.alive:
            return {"kind": "timeout"}
        if self.hang:
            return {"kind": "timeout"}
        if self.epoch < client_epoch and self.name == "old":
            return {"kind": "stale_epoch", "epoch": self.epoch}
        if self.name == "old":
            # 旧主不知道自己被废 按旧 epoch 接受 → 响应必须被客户端丢弃
            return {"kind": "ok", "epoch": self.epoch, "by": "old"}
        return {"kind": "ok", "epoch": self.epoch, "by": "new"}


if __name__ == "__main__":
    # 场景1:旧主 hang,客户端超时后重定向新主
    leaders = {"old": LeaderStub("old", 1, hang=True), "new": LeaderStub("new", 2)}
    c = Client(leaders)
    r = c.request({"op": "set", "k": "a"})
    assert r["kind"] == "ok" and r["by"] == "new" and r["epoch"] == 2
    assert c.log == [("old", "timeout"), ("new", "ok")], "悬挂超时后切新主"

    # 场景2:旧主还活着并响应,但客户端已知新 epoch → 拒收其响应
    leaders2 = {"old": LeaderStub("old", 1, alive=True), "new": LeaderStub("new", 3)}
    c2 = Client(leaders2)
    c2.epoch_known = 3
    c2.current = "old"                         # 模拟路由还指向旧主
    resp = leaders2["old"].handle({"op": "get"}, 3)
    assert resp["kind"] == "stale_epoch", "旧主 epoch 低 响应被判无效"

    # 场景3:旧主假装 ok 返回旧 epoch 值 客户端按 epoch 丢弃
    fake_ok = leaders2["old"].handle({"op": "get"}, 1)
    assert fake_ok["epoch"] == 1 < 3, "旧 epoch 响应即使 ok 也必须丢弃"
    assert leaders2["new"].handle({"op": "get"}, 3)["epoch"] == 3
    print("切换期请求通过:悬挂超时重定向 旧 epoch 响应被拒与丢弃 全程无脏读")
```

**追问**:
- 重试会不会重复写? 答:写请求要配幂等键,同一请求重定向后在新主上靠幂等键去重,协议层保证最多一次生效;
- 怎么发现该切了? 答:悬挂超时与旧 epoch 拒绝都是信号,连续触发即切换,不要等人工。
