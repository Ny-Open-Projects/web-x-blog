"""本地缓存广播失效的丢消息兜底: 广播会丢, TTL 与版本轮询补位"""

class NodeCache:
    def __init__(self, name, ttl_ticks, poll_every):
        self.name = name
        self.ttl_ticks = ttl_ticks            # 本地缓存自己的 TTL
        self.poll_every = poll_every          # 版本轮询周期, 0 表示未开启兜底
        self.data_v = 0
        self.loaded_at = 0

    def read(self, tick, central_version):
        expired = tick - self.loaded_at >= self.ttl_ticks
        due_poll = self.poll_every and tick % self.poll_every == 0
        if expired:
            self.data_v = central_version     # 过期回源到中心版本
            self.loaded_at = tick
        elif due_poll and self.data_v < central_version:
            self.data_v = central_version     # 轮询兜底: 补上丢掉的广播
            self.loaded_at = tick
        return self.data_v

# 中心版本推进 5 次, 其中 3 次广播模拟丢失
CENTRAL_EVENTS = {1: True, 2: False, 3: False, 4: True, 5: False}
central = {"version": 0}
a = NodeCache("A", ttl_ticks=10, poll_every=0)   # 长 TTL + 仅广播, 无兜底
b = NodeCache("B", ttl_ticks=2, poll_every=3)    # 短 TTL + 版本轮询兜底

stale_a = stale_b = 0
for tick in range(1, 13):
    if tick in CENTRAL_EVENTS:
        central["version"] = tick
        if CENTRAL_EVENTS[tick]:                 # 广播送达
            a.data_v = a.loaded_at = tick
            b.data_v = b.loaded_at = tick
        # 丢弃: 两个节点都收不到
    if a.read(tick, central["version"]) < central["version"]:
        stale_a += 1
    if b.read(tick, central["version"]) < central["version"]:
        stale_b += 1

print("12 个 tick, 版本推进 5 次, 其中 3 次广播被丢")
print("A (长TTL+仅广播):    陈旧读 %d 次, 最坏陈旧窗口贴着 TTL=10" % stale_a)
print("B (短TTL+版本轮询):  陈旧读 %d 次, 最坏窗口被压到轮询周期 3" % stale_b)
assert stale_b < stale_a
print("结论: 多实例本地缓存必须假设广播会丢, 短 TTL 限定最坏陈旧窗口的上限,")
print("      版本轮询把兜底窗口从'TTL 边界'压到'轮询周期', 两层都有才敢说最终一致")
