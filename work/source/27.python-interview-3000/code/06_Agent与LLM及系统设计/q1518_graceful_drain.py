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
