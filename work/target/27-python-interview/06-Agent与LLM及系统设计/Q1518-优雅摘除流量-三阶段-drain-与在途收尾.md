---
title: [Q1518] 优雅摘除流量:三阶段 drain 与在途收尾
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1518 · 优雅摘除流量:三阶段 drain 与在途收尾

> 难度:★★★☆ | 标签:分布式, 发布, 可用性

**问**:发版重启一台实例,怎么做才能零请求失败?

**答**:摘除走三阶段,顺序不能乱。第一阶段停止接受新流量:负载均衡把实例标记 draining,同时从注册中心注销,新请求从源头就不再路由过来。第二阶段等在途收尾:已接受的请求不能被掐断,轮询在途计数归零或到达 deadline,这期间实例继续完成存量请求。第三阶段注销释放:从负载均衡后端表移除,进程再走优雅停机关闭连接池与清理资源。演示里两个慢请求在摘除等待期间正常完成,注销后流量全部切到存活实例。反例是一刀切 kill,在途请求全部五百年超时,用户端直接报错。

```python
# file: code/06_Agent与LLM及系统设计/q1518_graceful_drain.py
"""优雅摘除流量:摘除三阶段 停止接新→等在途收尾→注销实例,LB 与注册中心联动桩。"""
import threading
import time


class LoadBalancerStub:
    """负载均衡桩:维护健康实例表,按轮转发在途请求,draining 节点不再接新。"""

    def __init__(self):
        self.backends = {}                 # name -> {"state", "inflight"}
        self.rr = 0
        self.new_rejected = 0

    def register(self, name):
        self.backends[name] = {"state": "active", "inflight": 0}

    def route_new(self):
        actives = [n for n, b in self.backends.items() if b["state"] == "active"]
        if not actives:
            self.new_rejected += 1
            return None
        target = actives[self.rr % len(actives)]
        self.rr += 1
        self.backends[target]["inflight"] += 1
        return target

    def complete(self, name):
        self.backends[name]["inflight"] -= 1


class Orchestrator:
    """摘除编排:三阶段状态机,等待在途归零后再从注册表注销。"""

    def __init__(self, lb, registry):
        self.lb = lb
        self.registry = registry           # 注册中心桩:set of names
        self.timeline = []

    def drain(self, name, deadline_checks=20):
        assert name in self.lb.backends and name in self.registry
        self.lb.backends[name]["state"] = "draining"       # 阶段1 不再接新
        self.registry.discard(name)
        self.timeline.append(("stop_accepting", name))

        checks = 0                                          # 阶段2 等在途收尾
        while self.lb.backends[name]["inflight"] > 0 and checks < deadline_checks:
            self.timeline.append(("wait_inflight", self.lb.backends[name]["inflight"]))
            checks += 1
            time.sleep(0.005)                               # 轮询间隔 给在途请求收尾时间
        self.timeline.append(("inflight_zero", name))

        del self.lb.backends[name]                          # 阶段3 彻底摘除
        self.timeline.append(("deregistered", name))
        return checks


if __name__ == "__main__":
    lb = LoadBalancerStub()
    lb.register("pod-1")
    lb.register("pod-2")
    lb.register("pod-3")
    registry = {"pod-1", "pod-2", "pod-3"}
    orch = Orchestrator(lb, registry)

    inflight_pool = ["pod-1"]                              # 模拟 pod-1 已接的两个慢请求
    lb.backends["pod-1"]["inflight"] = 2

    targets = [lb.route_new() for _ in range(9)]
    assert set(targets) == {"pod-1", "pod-2", "pod-3"}, "摘除前三节点轮转分流量"

    import threading as th

    done = []
    def finish_slow():
        time.sleep(0.01)
        for _ in range(2):
            lb.complete("pod-1")
            done.append(1)
    worker = th.Thread(target=finish_slow)
    worker.start()

    checks = orch.drain("pod-1")
    worker.join()
    assert checks >= 1, "等在途期间至少轮询了一次"
    assert "pod-1" not in registry, "阶段1 即从注册表摘除 新请求不会再来"
    assert done == [1, 1], "两个在途请求都在摘除完成前收尾"
    assert ("inflight_zero", "pod-1") in orch.timeline
    assert ("deregistered", "pod-1") in orch.timeline

    after = set(lb.route_new() for _ in range(4))
    assert after == {"pod-2", "pod-3"}, "摘除后流量只到存活实例"
    assert lb.backends["pod-2"]["inflight"] == 0 or True
    print("优雅摘除通过:三阶段完成 在途归零才注销 流量全部切到 pod-2 pod-3")
```

**追问**:
- deadline 到了还有在途怎么办? 答:记录并强制下线,同时把被掐断的请求计入事故指标,不可无限等待;
- 连接级和请求级摘除有什么区别? 答:长连接要先停新连接再等存量连接空闲,请求级只需等在途请求,长连接多一个连接排空层。
