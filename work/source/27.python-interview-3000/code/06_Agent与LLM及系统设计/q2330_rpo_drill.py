"""RPO 演练:主机房秒级写 连副本异步追,故障时刻切主,实测丢失条数对照 RPO 目标。"""
class DrillRig:
    def __init__(self, rpo_target_ms=500):
        self.rpo_target = rpo_target_ms
        self.wal = []
        self.replica_seq = 0
        self.now = 0

    def primary_write(self, key, val):
        self.now += 100
        self.wal.append({"ts": self.now, "key": key, "val": val})
        return len(self.wal)

    def replica_catch_up(self, lag_ms=300):
        horizon = self.now - lag_ms
        while self.replica_seq < len(self.wal) and self.wal[self.replica_seq]["ts"] <= horizon:
            self.replica_seq += 1

    def failover(self):
        lost = self.wal[self.replica_seq:]
        return {"lost_count": len(lost),
                "lost_window_ms": (self.now - lost[0]["ts"]) if lost else 0,
                "within_rpo": (self.now - lost[0]["ts"]) <= self.rpo_target if lost else True}


if __name__ == "__main__":
    rig = DrillRig(rpo_target_ms=500)
    for i in range(10):
        rig.primary_write("k%d" % i, i)
    rig.replica_catch_up(lag_ms=300)
    r = rig.failover()
    assert r["lost_count"] == 3 and r["lost_window_ms"] == 200 and r["within_rpo"], "滞后 300ms 丢 3 条 200ms 窗口"
    rig2 = DrillRig(rpo_target_ms=500)
    for i in range(10):
        rig2.primary_write("k%d" % i, i)
    rig2.replica_catch_up(lag_ms=700)
    r2 = rig2.failover()
    assert r2["lost_count"] == 7 and r2["lost_window_ms"] == 600 and not r2["within_rpo"], "滞后 700ms 突破 RPO 目标"
    rig3 = DrillRig(rpo_target_ms=500)
    for i in range(4):
        rig3.primary_write("k%d" % i, i)
    rig3.replica_catch_up(lag_ms=50)
    r3 = rig3.failover()
    assert r3["lost_count"] <= 1, "低滞后几乎零丢失"
    print("RPO 演练通过:丢失条数与窗口实测 目标对赌成立")
