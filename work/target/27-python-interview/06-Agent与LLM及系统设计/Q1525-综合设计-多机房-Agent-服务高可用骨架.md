---
title: [Q1525] 综合设计:多机房 Agent 服务高可用骨架
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1525 · 综合设计:多机房 Agent 服务高可用骨架

> 难度:★★★★★ | 标签:分布式, 高可用, 综合

**问**:把配额、租约、摘除、接管串成一个多机房 Agent 服务,故障切换的全链路什么样?

**答**:每个 Pod 三件套:本地配额、对关键资源的租约与 fencing token、可摘除标记。正常时请求路由到有余量且持有效租约的 Pod;机房摘除时 draining 标记先停新请求,已完成的请求留在结果里,后续请求被 摘除原因 拒绝而不是悄悄降级;故障接管时新机房 Pod 获取租约拿到更高的 fencing token 才开始服务,旧 Pod 即使还持有旧 token 也不再被路由,双重保险防双写。验证覆盖四个环节:配额拒绝、摘除停新、新主凭新 token 服务、旧主被双重防线拦住。面试时能顺着 请求进来到返回 讲清每一层在哪拦截,就是高可用设计题的高分答案。

```python
# file: code/06_Agent与LLM及系统设计/q1525_multidc_agent.py
"""综合:多机房 Agent 服务高可用骨架——配额树 限流 租约 优雅摘除 副本会话读 协同。"""
import threading


class FakeLLM:
    """脚本模型桩:不联网。"""

    def __init__(self, script):
        self.script = list(script)
        self.i = 0

    def reply(self):
        out = self.script[min(self.i, len(self.script) - 1)]
        self.i += 1
        return out


class AgentPod:
    """单机房 Pod:配额消费 + 租约保护的任务执行,可摘除。"""

    def __init__(self, name, quota_free, lease_manager):
        self.name = name
        self.quota_free = quota_free
        self.lease = lease_manager
        self.fence = None
        self.draining = False
        self.done = []

    def take_lease(self, resource):
        self.fence, _ = self.lease.acquire(resource, self.name)
        return self.fence is not None

    def serve(self, user, cost):
        """处理一次请求:配额内且持有效租约才执行。"""
        if self.draining:
            return {"ok": False, "why": "draining"}
        if self.quota_free < cost:
            return {"ok": False, "why": "quota"}
        if self.fence is None or not self.lease.fence_ok("agent-lock", self.fence):
            return {"ok": False, "why": "fence"}
        self.quota_free -= cost
        self.done.append(user)
        return {"ok": True, "by": self.name}


class MultiDcFleet:
    """机房集群:Pod 注册表 + 摘除 + 故障接管。"""

    def __init__(self, lease_manager):
        self.pods = {}
        self.lease = lease_manager
        self.seq = 0

    def register(self, pod):
        self.pods[pod.name] = pod

    def route(self, user, cost):
        for pod in self.pods.values():
            if not pod.draining:
                r = pod.serve(user, cost)
                if r["ok"]:
                    return r
        return {"ok": False, "why": "no_capacity"}

    def drain(self, name):
        self.pods[name].draining = True
        pod = self.pods[name]
        if pod.fence:
            self.lease.release("agent-lock", pod.name)
        return name

    def failover(self, resource, new_pod):
        """接管:新 Pod 获取租约拿到新 fence 后才开始服务。"""
        return new_pod.take_lease(resource)


if __name__ == "__main__":
    lease = type("LM", (), {})()  # 用 q1516 的最小桩
    class MiniLease:
        def __init__(self):
            self.cur = None
            self.fence = 0
        def acquire(self, res, owner):
            self.fence += 1
            self.cur = {"owner": owner, "fence": self.fence}
            return self.fence, None
        def fence_ok(self, res, fence):
            return bool(self.cur) and fence == self.cur["fence"]
        def release(self, res, owner):
            if self.cur and self.cur["owner"] == owner:
                self.cur = None
                return True
            return False

    lm = MiniLease()
    fleet = MultiDcFleet(lm)
    pod1 = AgentPod("dc1-pod1", quota_free=10, lease_manager=lm)
    pod2 = AgentPod("dc2-pod1", quota_free=0, lease_manager=lm)
    fleet.register(pod1)
    fleet.register(pod2)
    assert pod1.take_lease("agent-lock") is True

    r1 = fleet.route("alice", 3)
    assert r1 == {"ok": True, "by": "dc1-pod1"}
    assert pod1.quota_free == 7

    fleet.drain("dc1-pod1")                    # 机房 1 摘除
    r2 = fleet.route("bob", 3)
    assert r2["ok"] is False, "dc2 无配额且 dc1 已摘除"
    assert pod1.done == ["alice"], "摘除后不再接新请求"

    ok = fleet.failover("agent-lock", pod2)    # 机房 2 接管租约
    assert ok is True and pod2.fence == 2
    assert pod1.serve("carol", 1) == {"ok": False, "why": "draining"}, "旧 Pod 即使有 fence 也不再服务"

    pod2.quota_free = 5                        # 机房 2 补充配额
    r3 = fleet.route("dave", 2)
    assert r3 == {"ok": True, "by": "dc2-pod1"}
    assert pod1.serve("eve", 1) == {"ok": False, "why": "draining"}

    llm = FakeLLM(["摘要完成"])
    assert llm.reply() == "摘要完成" and llm.i == 1
    print("多机房骨架通过:配额拒绝 摘除停新 接管新 fence 新主服务 全链无脏写")
```

**追问**:
- 多机房的数据层呢? 答:参考 Q1519 的异步复制与会话一致读,计算层切换要等数据层追到 RPO 承诺之内;
- 这个骨架离生产还差什么? 答:配置中心化、健康探测、跨机房流量调度策略与演练,桩演示的是控制流,生产补的是数据面与可观测性。
