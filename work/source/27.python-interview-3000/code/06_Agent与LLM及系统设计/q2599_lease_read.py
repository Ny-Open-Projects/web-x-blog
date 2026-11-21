"""Q2599 租约下的读本地化:租约有效期内副本自己答,不用问主。

主给副本签发读租约,租约期内副本可以放心用本地数据应答一致性
读——因为主承诺租约期内不单方面改数据;写入会使租约立即失效,
副本下次读被迫回主续租并同步新值。
"""


class Primary:
    def __init__(self):
        self.data = {"k": "v1"}
        self.lease_until = {}
        self.rpc = 0

    def grant(self, replica, now, ttl=10.0):
        self.rpc += 1
        self.lease_until[replica] = now + ttl
        return self.lease_until[replica]

    def write(self, key, value, now):
        self.data[key] = value
        for r in self.lease_until:      # 写使所有读租约立即失效
            self.lease_until[r] = now


class Replica:
    def __init__(self, name, primary):
        self.name = name
        self.primary = primary
        self.local = dict(primary.data)
        self.local_hits = 0

    def read(self, key, now):
        if now < self.primary.lease_until.get(self.name, 0):
            self.local_hits += 1
            return self.local[key], "local"
        self.primary.grant(self.name, now)   # 续租顺带确认没有新写入
        self.local[key] = self.primary.data[key]
        return self.local[key], "via-primary"


def main():
    p = Primary()
    r = Replica("r1", p)
    trace = []
    for t in (1.0, 2.0, 9.0):
        v, src = r.read("k", t)
        trace.append((t, v, src))
    assert trace[0][2] == "via-primary"
    assert trace[1][2] == "local" and trace[2][2] == "local"
    assert p.rpc == 1 and r.local_hits == 2   # 租约期内只有一次授权
    p.write("k", "v2", now=9.5)
    v, src = r.read("k", 9.7)
    assert v == "v2" and src == "via-primary"
    print("读路径:", trace)
    print("写后租约失效强制回主:", v, src, "| 主 RPC 次数:", p.rpc)


if __name__ == "__main__":
    main()
