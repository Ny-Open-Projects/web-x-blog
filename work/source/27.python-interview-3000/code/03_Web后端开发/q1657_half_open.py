"""半开连接清理: 心跳刷新 last_seen, 周期扫描回收(纯标准库虚拟时钟)。"""

HEARTBEAT, IDLE_TIMEOUT = 3, 10


class Server:
    def __init__(self):
        self.conns = {}              # conn_id -> last_seen

    def accept(self, cid, now=0):
        self.conns[cid] = now

    def heartbeat(self, cid, now):
        if cid in self.conns:
            self.conns[cid] = now

    def sweep(self, now):
        dead = [c for c, seen in self.conns.items() if now - seen > IDLE_TIMEOUT]
        for c in dead:
            del self.conns[c]
        return dead


srv = Server()
srv.accept("clientA", 0)
srv.accept("clientB", 0)
for tick in range(1, 18):
    if tick % HEARTBEAT == 0:
        srv.heartbeat("clientB", tick)       # B 正常心跳
    if tick == 5:
        print("tick5: clientA 崩溃, 从此再无心跳(半开连接)")
    dead = srv.sweep(tick)
    if dead:
        print(f"tick{tick}: 回收半开连接 {dead}, 超过 {IDLE_TIMEOUT} tick 无心跳")
print("存活连接:", list(srv.conns))
print("要点: 半开连接对端不可知, 只能靠空闲超时加应用层心跳推断, 比裸 TCP keepalive 更可控")
