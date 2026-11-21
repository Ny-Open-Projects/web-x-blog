"""跨机房数据同步:主机房写日志 从机房异步拉取应用,滞后窗口内读旧值,RPO 可计算。"""
from collections import deque


class DcPrimary:
    """主机房:每个写操作记入 binlog 序列,seq 单调递增,写时可带时间戳。"""

    def __init__(self):
        self.data = {}
        self.ts_map = {}
        self.binlog = deque()
        self.seq = 0

    def write(self, key, value, ts=None):
        self.seq += 1
        self.binlog.append({"seq": self.seq, "key": key, "value": value})
        self.data[key] = value
        self.ts_map[key] = self.seq if ts is None else ts
        return self.seq


class DcReplica:
    """从机房:按 seq 拉取并应用,applied 落后于主 即复制滞后。"""

    def __init__(self, name):
        self.name = name
        self.data = {}
        self.applied = 0
        self.conflicts = []

    def pull(self, primary, up_to=None):
        """拉取同步:只应用 applied 之后的日志,可指定追赶目标。"""
        target = up_to if up_to is not None else primary.seq
        n = 0
        for entry in primary.binlog:
            if self.applied < entry["seq"] <= target:
                self.data[entry["key"]] = entry["value"]
                self.applied = entry["seq"]
                n += 1
        return n

    def read(self, key):
        return self.data.get(key)


class CrossDcSync:
    """同步编排:滞后条数与 RPO 计算,冲突写(双活)以 时间戳新者胜 并标记。"""

    def __init__(self, primary, replicas):
        self.primary = primary
        self.replicas = replicas
        self.conflict_log = []

    def lag(self, replica):
        return self.primary.seq - replica.applied

    def rpo_entries(self, replica):
        """RPO 以条数衡量:故障切换时最多丢这么多条写。"""
        return self.lag(replica)

    def apply_conflict(self, replica, key, local_value, local_ts):
        """双活冲突:比较主侧时间戳与本地时间戳 新者胜,记录冲突。"""
        remote_ts = self.primary.ts_map.get(key, 0)
        winner = local_value if local_ts > remote_ts else self.primary.data.get(key)
        self.conflict_log.append({"key": key, "winner": winner,
                                  "local_ts": local_ts, "remote_ts": remote_ts})
        return winner


if __name__ == "__main__":
    primary = DcPrimary()
    bj = DcReplica("beijing")
    sh = DcReplica("shanghai")
    sync = CrossDcSync(primary, [bj, sh])

    s1 = primary.write("price", 100)
    s2 = primary.write("price", 110)
    primary.write("stock", 5, ts=100)          # 主侧带时间戳写
    assert primary.seq == 3

    n = bj.pull(primary)                       # 北京全量追平
    assert n == 3 and bj.applied == 3 and sync.lag(bj) == 0
    assert bj.read("price") == 110

    sh.pull(primary)                           # 上海追平前 3 条
    assert sync.lag(sh) == 0
    primary.write("price", 120)                # 主又写 上海还没拉 → 滞后 1
    assert sync.lag(sh) == 1 and sh.read("price") == 110, "滞后窗口内读旧值"
    assert sync.rpo_entries(sh) == 1, "此刻切换到上海 最多丢 1 条"

    gz = DcReplica("guangzhou")                # 新副本按 up_to 部分追赶
    assert gz.pull(primary, up_to=s2) == 2 and gz.applied == 2
    assert gz.read("price") == 110 and sync.lag(gz) == 2

    sh.pull(primary)                           # 追平
    assert sync.lag(sh) == 0 and sh.read("price") == 120

    w = sync.apply_conflict(bj, "stock", local_value=9, local_ts=200)
    assert w == 9 and sync.conflict_log[0]["winner"] == 9
    w2 = sync.apply_conflict(bj, "stock", local_value=7, local_ts=50)
    assert w2 == 5, "本地时间戳 50 旧于主侧 100 主侧值胜出"
    assert len(sync.conflict_log) == 2
    print("跨机房同步通过:滞后 0→1→0 RPO 1 条 冲突新者胜两条留痕")
