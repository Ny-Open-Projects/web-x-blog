"""读己之写一致性: 复制延迟下按用户水印粘主读取"""

class Router:
    def __init__(self, replica_lag=0.5):
        self.watermark = {}              # user -> 最后一次写的时间戳
        self.replica_lag = replica_lag
        self.now = 1000.0

    def write(self, user, op):
        self.now += 0.01
        self.watermark[user] = self.now
        return f"写 {op} 已提交, 水印 {self.now:.2f}"

    def route_read(self, user):
        last = self.watermark.get(user)
        if last and self.now - last < self.replica_lag:
            return "primary", "最近写过, 会话内粘主, 避免读到旧值"
        return "replica", "超过粘主窗口, 正常走副本"

r = Router()
print(r.write("u1", "改昵称"))
print("u1 立即读:", r.route_read("u1"))
r.now += 0.2
print("u1 0.2s 后读:", r.route_read("u1"), "(仍在窗口)")
r.now += 0.4
print("u1 0.6s 后读:", r.route_read("u1"), "(窗口过期放行副本)")
print("u2 任意时刻读:", r.route_read("u2"), "(其他用户不受影响)")
print("实现层次: 1) 网关按 session 粘主一段时间, 简单但粒度粗;")
print("          2) 记录每用户最后写位点, 读时比对副本 GTID 位点, 粒度细;")
print("          3) 读副本前等待其位点覆盖自己的写入, 用延迟换一致")
print("注意: 粘主窗口要略大于实际复制延迟 p99, 且只对读己之写敏感的路径启用")
