"""服务注册发现:TTL 心跳 + 超时摘除 + 客户端本地缓存 + 优雅下线。"""
import time


class Registry:
    def __init__(self, ttl=0.3):
        self.instances, self.ttl = {}, ttl        # service -> {inst_id: {addr, last_hb}}

    def register(self, service, inst_id, addr, now):
        self.instances.setdefault(service, {})[inst_id] = {"addr": addr, "last_hb": now}

    def heartbeat(self, service, inst_id, now):
        if inst_id in self.instances.get(service, {}):
            self.instances[service][inst_id]["last_hb"] = now
            return True
        return False

    def deregister(self, service, inst_id):
        self.instances.get(service, {}).pop(inst_id, None)

    def sweep(self, now):
        """心跳超时摘除:软状态淘汰。"""
        removed = []
        for svc, insts in self.instances.items():
            for iid, meta in list(insts.items()):
                if now - meta["last_hb"] > self.ttl:
                    insts.pop(iid)
                    removed.append((svc, iid))
        return removed

    def healthy_list(self, service):
        return [m["addr"] for m in self.instances.get(service, {}).values()]


class ClientCache:
    """客户端本地缓存:注册中心挂了也能用旧列表。"""

    def __init__(self, registry):
        self.registry, self.cache = registry, {}
        self.refreshes = 0

    def refresh(self):
        self.cache = {svc: self.registry.healthy_list(svc) for svc in self.registry.instances}
        self.refreshes += 1

    def resolve(self, service):
        return self.cache.get(service, [])


if __name__ == "__main__":
    reg = Registry(ttl=0.3)
    reg.register("order-svc", "i1", "10.0.0.1:8000", now=0.0)
    reg.register("order-svc", "i2", "10.0.0.2:8000", now=0.0)
    cache = ClientCache(reg)
    cache.refresh()
    print("发现:", cache.resolve("order-svc"))
    assert len(cache.resolve("order-svc")) == 2

    reg.heartbeat("order-svc", "i1", now=0.3)     # i1 续约成功,i2 失联
    removed = reg.sweep(now=0.5)
    print("心跳超时摘除:", removed)
    assert removed == [("order-svc", "i2")], "仅失联实例被摘除"
    cache.refresh()
    assert cache.resolve("order-svc") == ["10.0.0.1:8000"]

    # 优雅下线:i1 先反注册再停进程
    reg.deregister("order-svc", "i1")
    cache.refresh()
    assert cache.resolve("order-svc") == []
    print("优雅下线先摘流量;注册中心不可用时客户端缓存兜底")
