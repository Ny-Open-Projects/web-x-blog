"""WAL 检查点与截断:定期固化状态,截掉旧日志,恢复只需检查点加尾部重放。"""


class WALWithCheckpoint:
    def __init__(self):
        self.log = []
        self.checkpoint = {}
        self.ckpt_lsn = 0
        self.next_lsn = 1

    def append(self, op, key, value=None):
        rec = {"lsn": self.next_lsn, "op": op, "key": key, "value": value}
        self.next_lsn += 1
        self.log.append(rec)
        return rec["lsn"]

    def state_now(self):
        st = dict(self.checkpoint)
        for rec in self.log:
            if rec["op"] == "set":
                st[rec["key"]] = rec["value"]
            elif rec["op"] == "del":
                st.pop(rec["key"], None)
        return st

    def checkpoint_now(self):
        """固化当前状态,截掉检查点之前的日志段。"""
        self.checkpoint = self.state_now()
        self.ckpt_lsn = self.next_lsn - 1
        self.log = [r for r in self.log if r["lsn"] > self.ckpt_lsn]
        return self.ckpt_lsn

    def recover(self):
        """崩溃恢复:装载检查点,重放尾部日志。"""
        st = dict(self.checkpoint)
        replayed = 0
        for rec in self.log:
            if rec["lsn"] <= self.ckpt_lsn:
                continue
            if rec["op"] == "set":
                st[rec["key"]] = rec["value"]
            elif rec["op"] == "del":
                st.pop(rec["key"], None)
            replayed += 1
        return st, replayed


if __name__ == "__main__":
    db = WALWithCheckpoint()
    for i in range(50):
        db.append("set", "k%d" % (i % 10), i)
    db.checkpoint_now()
    ckpt_size = len(db.log)
    assert ckpt_size == 0 and db.ckpt_lsn == 50, "截断后日志只剩尾部空段"

    for i in range(5):
        db.append("set", "hot", i)
    db.append("del", "k0")

    live = db.state_now()
    assert live["hot"] == 4 and "k0" not in live and live["k1"] == 41

    recovered, replayed = db.recover()
    assert recovered == live, "检查点加尾部重放必须等于活状态"
    assert replayed == 6, "只重放了检查点之后的 6 条"
    assert db.next_lsn - 1 - db.ckpt_lsn == 6

    # 再做一次检查点:日志再次收敛
    db.checkpoint_now()
    assert len(db.log) == 0 and db.checkpoint == live
    st, r = db.recover()
    assert st == live and r == 0
    print("检查点通过:固化截断后恢复只重放 6 条,二次检查点后重放为 0")
