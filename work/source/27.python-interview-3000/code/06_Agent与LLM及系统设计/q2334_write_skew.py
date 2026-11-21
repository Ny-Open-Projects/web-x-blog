"""写倾斜:两个事务各读同一守卫条件 各写不相交的行 合计违反约束,快照隔离防不住。"""
class Doctor:
    def __init__(self, name, on_call):
        self.name, self.on_call = name, on_call


class ClinicDB:
    def __init__(self, doctors):
        self.doctors = {d.name: d for d in doctors}
        self.committed = []

    def snapshot(self):
        return {n: d.on_call for n, d in self.doctors.items()}

    def txn(self, txn_id, read_fn, writes, snap=None):
        if snap is None:
            snap = self.snapshot()
        if not read_fn(snap):
            return {"txn": txn_id, "committed": False, "reason": "guard"}
        for name, on_call in writes.items():
            self.doctors[name].on_call = on_call
        self.committed.append(txn_id)
        return {"txn": txn_id, "committed": True}

    def on_call_count(self):
        return sum(1 for d in self.doctors.values() if d.on_call)


def guard_off(name):
    """我想下线 必须别人还在值班 只看快照 不看对方未提交的意图。"""
    def g(snap):
        return sum(1 for n, v in snap.items() if v and n != name) >= 1
    return g


if __name__ == "__main__":
    db = ClinicDB([Doctor("alice", True), Doctor("bob", True)])
    snap0 = db.snapshot()
    r1 = db.txn("t1", guard_off("alice"), {"alice": False}, snap=snap0)
    r2 = db.txn("t2", guard_off("bob"), {"bob": False}, snap=snap0)
    assert r1["committed"] and r2["committed"], "同一旧快照 各自守卫都过"
    assert db.on_call_count() == 0, "写倾斜 值班约束被破坏"
    db2 = ClinicDB([Doctor("alice", True), Doctor("bob", True)])
    r1b = db2.txn("t1", guard_off("alice"), {"alice": False})
    r2b = db2.txn("t2", guard_off("bob"), {"bob": False})
    assert r1b["committed"] and not r2b["committed"], "串行化后 t2 读到 t1 的提交 被守卫拦截"
    assert db2.on_call_count() == 1
    print("写倾斜演示通过:快照隔离双双提交破坏约束 串行化读取可拦截")
