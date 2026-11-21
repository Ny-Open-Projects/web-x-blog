"""写前日志 WAL 概念实现:先落日志再改状态,崩溃后按 LSN 重放,撕裂写止步。"""


def crc(rec):
    return sum(len(str(k)) + len(str(v)) for k, v in sorted(rec.items())) % 9973


class WAL:
    def __init__(self):
        self.log = []

    def append(self, op, key, value=None):
        rec = {"lsn": len(self.log) + 1, "op": op, "key": key, "value": value}
        rec["crc"] = crc({k: v for k, v in rec.items()})
        self.log.append(rec)          # 现实里这一步是顺序写盘加 fsync
        return rec["lsn"]

    def apply_one(self, state, rec):
        if rec["op"] == "set":
            state[rec["key"]] = rec["value"]
        elif rec["op"] == "del":
            state.pop(rec["key"], None)

    def replay(self, state, start_lsn=1):
        """从 start_lsn 重放;校验失败的记录视为撕裂写,到此为止。"""
        applied = 0
        for rec in self.log:
            if rec["lsn"] < start_lsn:
                continue
            body = {k: v for k, v in rec.items() if k != "crc"}
            if rec.get("crc") != crc(body):
                break
            self.apply_one(state, rec)
            applied += 1
        return applied


if __name__ == "__main__":
    wal = WAL()
    live = {}
    for op, k, v in [("set", "a", 1), ("set", "b", 2), ("del", "a", None), ("set", "c", 3)]:
        wal.append(op, k, v)
        wal.apply_one(live, {"lsn": len(wal.log), "op": op, "key": k, "value": v})
    assert live == {"b": 2, "c": 3}

    # 崩溃恢复:状态全丢,凭日志重放重建
    recovered = {}
    n = wal.replay(recovered)
    assert n == 4 and recovered == live, "重放结果必须与崩溃前一致"

    # 从任意 LSN 续放:检查点场景
    partial = {"b": 2, "c": 3}
    assert wal.replay(partial, start_lsn=3) == 2, "已应用的前缀不重复执行"

    # 撕裂写:最后一条被写坏,重放在它之前止步,状态仍是干净前缀
    wal.log[-1]["value"] = 999              # 模拟半截写入改了数据
    torn = {}
    n2 = wal.replay(torn)
    assert n2 == 3 and torn == {"b": 2}, "坏记录及之后不得应用"
    print("WAL 通过:重放重建一致 前缀续放不重做 撕裂写止步保干净前缀")
