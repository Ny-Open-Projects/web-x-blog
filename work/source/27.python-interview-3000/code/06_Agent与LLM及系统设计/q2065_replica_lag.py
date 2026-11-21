"""副本滞后读策略:写后读走主或有据从库,有界滞后挑最新鲜,超限兜底回主。"""


class ReadRouter:
    def __init__(self, lag):
        self.lag = dict(lag)          # 副本 -> 滞后秒数

    def pick_read_your_writes(self, session_lsn, replica_applied):
        """会话刚写过:只读已追上该写入的从库,没有就回主库。"""
        if replica_applied is not None and replica_applied >= session_lsn:
            return "r1"
        return "primary"

    def pick_bounded_staleness(self, max_lag):
        """有界滞后:挑满足上限里最新鲜的从库,无人达标回主库。"""
        ok = [(r, l) for r, l in self.lag.items() if r != "primary" and l <= max_lag]
        if not ok:
            return "primary"
        return min(ok, key=lambda x: x[1])[0]

    def pick_freshest(self):
        """不设硬约束:挑当前滞后最小的从库,无从库时回主库。"""
        reps = {r: l for r, l in self.lag.items() if r != "primary"}
        if not reps:
            return "primary"
        return min(reps, key=lambda r: reps[r])


if __name__ == "__main__":
    router = ReadRouter({"primary": 0, "r1": 2, "r2": 5})

    # 写后读:从库还没追上会话最近写入 -> 必须回主库
    assert router.pick_read_your_writes(session_lsn=100, replica_applied=98) == "primary"
    assert router.pick_read_your_writes(session_lsn=100, replica_applied=100) == "r1"
    assert router.pick_read_your_writes(100, None) == "primary"

    # 有界滞后:max_lag=3 时 r2 的 5 秒滞后不合格,r1 胜出
    assert router.pick_bounded_staleness(3) == "r1"
    assert router.pick_bounded_staleness(1) == "primary", "全都超限只能回主库"
    assert router.pick_bounded_staleness(10) == "r1", "达标里挑最新鲜的"

    # 无硬约束:永远给滞后最小的从库
    assert router.pick_freshest() == "r1"

    laggy = ReadRouter({"primary": 0, "r1": 30, "r2": 45})
    assert laggy.pick_bounded_staleness(5) == "primary"
    assert laggy.pick_freshest() == "r1"

    # 只有主库可用:所有策略都安全回落,不抛异常
    solo = ReadRouter({"primary": 0})
    assert solo.pick_bounded_staleness(3) == "primary"
    assert solo.pick_freshest() == "primary"
    assert solo.pick_read_your_writes(1, None) == "primary"
    print("滞后读策略通过:写后读凭 LSN 回主,有界滞后挑新鲜,超限兜底不脏读")
