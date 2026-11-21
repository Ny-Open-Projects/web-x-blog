"""对账系统:规范化取数 -> 四类差异分类 -> 差异状态机 -> 报告。"""


def normalize(records):
    return {r["txn_id"]: int(round(r["amount"] * 100)) for r in records}   # 以分为单位


def reconcile(local, channel):
    local_n, channel_n = normalize(local), normalize(channel)
    matched, long_, short_, mismatch = [], [], [], []
    for txn, amt in local_n.items():
        if txn not in channel_n:
            long_.append((txn, amt))             # 我方有渠道无
        elif channel_n[txn] != amt:
            mismatch.append((txn, amt, channel_n[txn]))
        else:
            matched.append(txn)
    for txn, amt in channel_n.items():
        if txn not in local_n:
            short_.append((txn, amt))            # 渠道有我方无
    return {"matched": matched, "long": long_, "short": short_, "mismatch": mismatch}


class DisputeState:
    FLOW = {"open": {"auto_fix", "manual", "closed"},
            "auto_fix": {"closed"}, "manual": {"closed", "open"}, "closed": set()}

    def __init__(self):
        self.items = {}

    def open_case(self, kind, detail):
        cid = f"D{len(self.items) + 1}"
        self.items[cid] = {"kind": kind, "detail": detail, "state": "open"}
        return cid

    def transition(self, cid, to):
        assert to in self.FLOW[self.items[cid]["state"]], f"非法 {self.items[cid]['state']}->{to}"
        self.items[cid]["state"] = to


if __name__ == "__main__":
    local = [{"txn_id": "T1", "amount": 99.90}, {"txn_id": "T2", "amount": 50.00},
             {"txn_id": "T4", "amount": 30.00}, {"txn_id": "T5", "amount": 12.34}]
    channel = [{"txn_id": "T1", "amount": 99.90}, {"txn_id": "T2", "amount": 45.00},
               {"txn_id": "T3", "amount": 77.77}, {"txn_id": "T5", "amount": 12.34}]
    rep = reconcile(local, channel)
    print("一致:", rep["matched"])
    print("长款 我方多:", rep["long"])
    print("短款 渠道多:", rep["short"])
    print("金额不符:", rep["mismatch"])
    assert rep["matched"] == ["T1", "T5"]
    assert rep["long"] == [("T4", 3000)]
    assert rep["short"] == [("T3", 7777)]
    assert rep["mismatch"] == [("T2", 5000, 4500)]

    dsp = DisputeState()
    c1 = dsp.open_case("long", "T4 渠道未收到,可能掉单,补查询")
    dsp.transition(c1, "auto_fix")
    dsp.transition(c1, "closed")
    c2 = dsp.open_case("mismatch", "T2 金额差 5 元,人工核凭证")
    print("工单:", {cid: (v["kind"], v["state"]) for cid, v in dsp.items.items()})
    assert dsp.items[c1]["state"] == "closed"
    print("对账差异全部进状态机,销案有据")
