"""CAP 演示:网络分区时两副本各自处理写,按策略选 CP 或 AP,恢复后收敛。"""


class Replica:
    def __init__(self, name):
        self.name, self.data, self.version = name, {}, 0

    def write(self, key, value):
        self.data[key] = value
        self.version += 1
        return self.version


class Cluster:
    def __init__(self, strategy):
        self.strategy = strategy              # "CP" or "AP"
        self.a, self.b = Replica("A"), Replica("B")
        self.partitioned = False
        self.rejected = 0

    def write(self, replica, key, value):
        if self.partitioned:
            if self.strategy == "CP":
                if replica.name == "A":        # 只有多数派可用
                    return replica.write(key, value)
                self.rejected += 1
                raise PermissionError("分区期间拒绝写入 保一致性")
            return replica.write(key, value)   # AP:两个副本都接受,允许分叉
        return replica.write(key, value)

    def heal(self):
        """分区恢复:CP 天然一致;AP 按 last-writer-wins 收敛到相同值。"""
        for k in set(self.a.data) | set(self.b.data):
            if self.a.data.get(k) != self.b.data.get(k):
                winner = max((self.a, self.b), key=lambda r: r.version)
                loser = self.b if winner is self.a else self.a
                loser.data[k] = winner.data[k]
                loser.version = winner.version


if __name__ == "__main__":
    rejected_counts = {}
    for strategy in ("CP", "AP"):
        c = Cluster(strategy)
        c.partitioned = True
        out_a = c.write(c.a, "stock", 99)
        try:
            c.write(c.b, "stock", 99)
        except PermissionError:
            pass
        print(f"[{strategy}] 分区期间 A 写成功 v={out_a}, B 被拒 {c.rejected} 次")
        rejected_counts[strategy] = c.rejected
        c.partitioned = False
        c.heal()
        assert c.a.data == c.b.data, "恢复后必须收敛"
        print(f"[{strategy}] 恢复后收敛: {c.a.data}")
    assert rejected_counts == {"CP": 1, "AP": 0}
    print("CP 拒写保一致,AP 收敛保可用,取舍被代码化")
